import dagger


class PyStrategy:
    def before(container: dagger.Container) -> dagger.Container:
        return container
    
    async def test(container: dagger.Container):
        result = container.with_exec(["pytest"])
        await result.sync()

    async def solve(container: dagger.Container):
        result = container.with_exec(["python3", "main.py"])
        await result.sync()


class GoLangStrategy:
    def before(container: dagger.Container) -> dagger.Container:
        return container
    
    async def test(container: dagger.Container):
        result = container.with_exec(["go", "test", "."])
        await result.sync()
        print(f"Test:\n{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = container.with_exec(["go", "run", "main.go"])
        await result.sync()
        print(f"Solve:\n{await result.stdout()}")


class RustStrategy:
    def before(container: dagger.Container) -> dagger.Container:
        return container
    
    async def test(container: dagger.Container):
        result = container.with_exec(["cargo", "test"])
        await result.sync()
        print(f"Test:\n{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = container.with_workdir("/").with_exec(["cargo", "run"])
        await result.sync()
        print(f"Solve:\n{await result.stdout()}")


class JavaStrategy:
    def before(container: dagger.Container) -> dagger.Container:
        return container.with_workdir("/").with_exec(
            ["mvn", "install", "-q"]
        )
    
    async def test(container: dagger.Container):
        result = container.with_workdir("/").with_exec(["mvn", "test"])
        await result.sync()
        print(f"Test:\n{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = (
            container.with_workdir("/")
            .with_exec(["mvn", "package"])
            .with_exec(["java", "-cp", "target/main-0.1.0.jar", "solve.Main"])
        )

        await result.sync()
        print(f"Solve:\n{await result.stdout()}")

class JSStrategy:
    def before(container: dagger.Container) -> dagger.Container:
        return container
    
    async def test(container: dagger.Container):
        result = container.with_workdir("/").with_exec(["npm", "test"])
        await result.sync()
        print(f"Test:\n{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = (
            container.with_workdir("/")
            .with_exec(["java", "-cp", "target/main-0.1.0.jar", "solve.Main"])
        )

        await result.sync()
        print(f"Solve:\n{await result.stdout()}")
