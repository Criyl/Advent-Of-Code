import dagger


class PyStrategy:
    async def test(container: dagger.Container):
        result = container.with_exec(["pytest"])
        await result.sync()
        print(f"Test:\n{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = container.with_exec(["python3", f"main.py"])
        await result.sync()
        print(f"Solve:\n{await result.stdout()}")


class GoLangStrategy:
    async def test(container: dagger.Container):
        result = container.with_exec(["go", "test", "."])
        await result.sync()
        print(f"Test:\n{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = container.with_exec(["go", "run", "main.go"])
        await result.sync()
        print(f"Solve:\n{await result.stdout()}")


class RustStrategy:
    async def test(container: dagger.Container):
        result = container.with_exec(["cargo", "test"])
        await result.sync()
        print(f"Test:\n{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = container.with_workdir("/").with_exec(["cargo", "run"])
        await result.sync()
        print(f"Solve:\n{await result.stdout()}")


class JavaStrategy:
    async def test(container: dagger.Container):
        result = container.with_workdir("/").with_exec(["mvn", "test"])
        await result.sync()
        print(f"Test:\n{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = container.with_workdir("/").with_exec(["mvn", "-v"])
        await result.sync()
        print(f"Solve:\n{await result.stdout()}")
