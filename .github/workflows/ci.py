import sys
import anyio
import dagger
import re
from solve_strategy import PyStrategy, GoLangStrategy, RustStrategy, JavaStrategy, JSStrategy, handle
from reporting import generate_report


DAY_REGEX = r"^day"
YEAR_REGEX = r"^AoC"
SUPPORTED_LANGUAGE = {
    "python": PyStrategy,
    "golang": GoLangStrategy,
    "rust": RustStrategy,
    "java": JavaStrategy,
    "js": JSStrategy,
}
DAY_REPORTS = []
LANG_CONTAINER = {}


def build_containers(client):
    for language, strategy in SUPPORTED_LANGUAGE.items():
        if strategy is None:
            break
        image_dir = client.host().directory(f"images/{language}")

        LANG_CONTAINER[language] = client.container().build(image_dir)

async def run_day(year, day, day_dir,taskgroup):
    entries = await day_dir.entries()
    for language, strategy in SUPPORTED_LANGUAGE.items():
        if language not in entries or strategy is None:
            break
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

async def run_year():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        build_containers(client)

        src = client.host().directory(".")

        entries = await src.entries()
        years = [e for e in entries if re.match(YEAR_REGEX, e)]

        for year in years:
            year_dir = src.directory(f"{year}")

            entries = await year_dir.entries()
            days = [e for e in entries if re.match(DAY_REGEX, e)]

            async with anyio.create_task_group() as tg:
                for day in days:
                    day_dir = year_dir.directory(f"{day}")
                    await run_day(year, day, day_dir, tg)
    

if __name__ == "__main__":
    try:
        anyio.run(run_year)
    except dagger.ExecError as e:
        print(e)
    finally:
        print(generate_report(map(lambda strategy: strategy.report, DAY_REPORTS)))