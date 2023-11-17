import sys
import anyio
import dagger
import re
import pysolve


async def run_year():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        src = client.host().directory(".")

        entries = await src.entries()
        years = [e for e in entries if re.match(r'AoC', e)]

        for year in years:
            year_dir = src.directory(f"{year}")

            entries = await year_dir.entries()
            days = [e for e in entries if re.match(r'day', e)]
            for day in days:
                day_dir = year_dir.directory(f"{day}")

                entries = await day_dir.entries()
                pythonssss = [e for e in entries if re.match(r'python', e)]
                for python in pythonssss:
                    working_dir = day_dir.directory(f"{python}")
                    container = (
                        pysolve
                            .image(client)
                            .with_directory("/src", working_dir)
                            .with_workdir("/src")
                    )
                    async with anyio.create_task_group() as tg:
                        tg.start_soon(pysolve.solve, container)
                        tg.start_soon(pysolve.test, container)

if __name__ == "__main__":
    try:
        anyio.run(run_year)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)