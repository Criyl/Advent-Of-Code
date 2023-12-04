import sys
import anyio
import dagger
import re
from solve_strategy import (
    PyStrategy,
    GoLangStrategy,
    RustStrategy,
    JavaStrategy,
    JSStrategy,
    KotlinStrategy,
    handle,
)
from reporting import generate_report


DAY_REGEX = r"^day"
YEAR_REGEX = r"^AoC"
SUPPORTED_LANGUAGE = {
    "python": PyStrategy,
    "golang": GoLangStrategy,
    "rust": RustStrategy,
    "java": JavaStrategy,
    "kotlin": KotlinStrategy,
    "js": JSStrategy,
}
DAY_REPORTS = []
LANG_CONTAINER = {}


async def build_containers(client):
    async with anyio.create_task_group() as taskgroup:
        for language, strategy in SUPPORTED_LANGUAGE.items():
            if strategy is None:
                break

            async def temp(language):
                image_dir = client.host().directory(f"images/{language}")
                LANG_CONTAINER[language] = client.container().build(image_dir)

            taskgroup.start_soon(temp, language)


async def run_day(year, day, day_dir, taskgroup):
    entries = await day_dir.entries()
    for language, strategy in SUPPORTED_LANGUAGE.items():
        if language not in entries or strategy is None:
            continue
        working_dir = day_dir.directory(f"{language}")
        strategy = SUPPORTED_LANGUAGE[language](year, day, language)
        global DAY_REPORTS
        DAY_REPORTS += [strategy]
        container = (
            LANG_CONTAINER[language]
            .with_directory("/src", working_dir)
            .with_workdir("/src")
        )
        container = strategy.before(container)
        taskgroup.start_soon(handle, strategy, container)


async def run_year(client, taskgroup):
    src = client.host().directory(".")

    entries = await src.entries()
    years = [e for e in entries if re.match(YEAR_REGEX, e)]
    for year in years:
        year_dir = src.directory(f"{year}")

        entries = await year_dir.entries()
        days = [e for e in entries if re.match(DAY_REGEX, e)]

        for day in days:
            day_dir = year_dir.directory(f"{day}")
            taskgroup.start_soon(run_day, year, day, day_dir, taskgroup)


async def run():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        await build_containers(client)

        async with anyio.create_task_group() as taskgroup:
            taskgroup.start_soon(run_year, client, taskgroup)


if __name__ == "__main__":
    try:
        anyio.run(run)
    except dagger.ExecError as e:
        print(e)
    finally:
        reports = list(map(lambda strategy: strategy.report, DAY_REPORTS))

        print(generate_report(reports))

        for report in reports:
            if not report.passed():
                sys.exit(1)
