import sys
import anyio
import dagger
import re
from solve_strategy import PyStrategy, GoLangStrategy, RustStrategy, JavaStrategy

SUPPORTED_LANGUAGE = {
    "python": PyStrategy,
    "golang": GoLangStrategy,
    "rust": RustStrategy,
    "java": JavaStrategy,
    "js": None,
}

LANG_CONTAINER = {}


def build_containers(client):
    for language, strategy in SUPPORTED_LANGUAGE.items():
        if strategy is None:
            break
        image_dir = client.host().directory(f"images/{language}")

        LANG_CONTAINER[language] = client.container().build(image_dir)


async def run_year():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        build_containers(client)

        src = client.host().directory(".")

        entries = await src.entries()
        years = [e for e in entries if re.match(r"AoC", e)]

        for year in years:
            year_dir = src.directory(f"{year}")

            entries = await year_dir.entries()
            days = [e for e in entries if re.match(r"day", e)]

            async with anyio.create_task_group() as tg:
                for day in days:
                    day_dir = year_dir.directory(f"{day}")

                    entries = await day_dir.entries()

                    for language, strategy in SUPPORTED_LANGUAGE.items():
                        if language not in entries or strategy is None:
                            break
                        working_dir = day_dir.directory(f"{language}")
                        print(f"{year}/{day}/{language}")
                        strategy = SUPPORTED_LANGUAGE[language]
                        container = (
                            LANG_CONTAINER[language]
                            .with_directory("/src", working_dir)
                            .with_workdir("/src")
                        )

                        if language == "java":
                            container = container.with_workdir("/").with_exec(
                                ["mvn", "install", "-q"]
                            )

                        tg.start_soon(
                            strategy.solve, container, name=f"{language}-solve"
                        )
                        tg.start_soon(strategy.test, container, name=f"{language}-test")


if __name__ == "__main__":
    try:
        anyio.run(run_year)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
