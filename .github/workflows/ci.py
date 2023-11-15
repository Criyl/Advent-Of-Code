import sys
import anyio
import dagger
import re


async def solves(client: dagger.Client, container: dagger.Container):
    src = client.host().directory(".")
    entries = await src.entries()
    days = [e for e in entries if re.match(r'day_', e)]
    python = (container)
    for day in days:
        python = python.with_exec(["python3", f"{day}/main.py"])

    await python.sync()
    print(f"{await python.stdout()}")

async def pytest(client: dagger.Client, container: dagger.Container):
    python = (
        container
        .with_exec(["pytest"])
    )

    print(f"Starting tests for Python")
    await python.sync()
    print(f"{await python.stdout()}")


async def flake8(client: dagger.Client, container: dagger.Container):
    python = (
        container
        .with_exec(["flake8"])
    )

    await python.sync()
    print(f"{await python.stdout()}")

async def run_year():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        src = client.host().directory(".")


        entries = await src.entries()
        years = [e for e in entries if re.match(r'AC', e)]
        for year in years:
            year_dir = client.host().directory(f"{year}")
            container = (
                client.container()
                .build(src)
                .with_directory("/src", year_dir)
                .with_workdir("/src")
            )
            async with anyio.create_task_group() as tg:
                tg.start_soon(solves, client, container)
                tg.start_soon(pytest, client, container)
                tg.start_soon(flake8, client, container)

if __name__ == "__main__":
    try:
        anyio.run(run_year)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)