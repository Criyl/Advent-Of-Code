import sys
import anyio
import dagger
import re

def image(client: dagger.Client):
    return client.container().build(
        client.host()
            .directory(".")
            .directory("images/python")
    )

async def test(container: dagger.Container):
    result = container.with_exec(["pytest"])
    await result.sync()
    print(f"{await result.stdout()}")

async def solve(container: dagger.Container):
    result = container.with_exec(["python3", f"main.py"])
    await result.sync()
    print(f"{await result.stdout()}")
