import dagger
from reporting import DayReport


class SolveStrategy:
    report: DayReport

    def __init__(self, year, day, language) -> None:
        self.report = DayReport(year, day, language)

    def before(self, container: dagger.Container) -> dagger.Container:
        return container

    async def test(self, container: dagger.Container):
        ...

    async def solve(self, container: dagger.Container):
        ...


class PyStrategy(SolveStrategy):
    async def test(self, container: dagger.Container):
        result = container.with_exec(["pytest"])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)

    async def solve(self, container: dagger.Container):
        result = container.with_exec(["python3", "main.py"])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)


class GoLangStrategy(SolveStrategy):
    async def test(self, container: dagger.Container):
        result = container.with_exec(["go", "test", "."])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)

    async def solve(self, container: dagger.Container):
        result = container.with_exec(["go", "run", "main.go"])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)


class RustStrategy(SolveStrategy):
    def before(self, container: dagger.Container) -> dagger.Container:
        return container.with_workdir("/").with_exec(
            ["cargo", "install", "--path", "."]
        )

    async def test(self, container: dagger.Container):
        result = container.with_exec(["cargo", "test"])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)

    async def solve(self, container: dagger.Container):
        result = container.with_exec(["cargo", "run"])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)


class JavaStrategy(SolveStrategy):
    def before(self, container: dagger.Container) -> dagger.Container:
        return container.with_workdir("/")

    async def test(self, container: dagger.Container):
        result = container.with_workdir("/").with_exec(["mvn", "test"])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)

    async def solve(self, container: dagger.Container):
        result = (
            container.with_workdir("/")
            .with_exec(["mvn", "package"])
            .with_exec(["java", "-cp", "target/main-0.1.0.jar", "solve.Main"])
        )
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)


class JSStrategy(SolveStrategy):
    def before(self, container: dagger.Container) -> dagger.Container:
        return container.with_workdir("/")

    async def test(self, container: dagger.Container):
        result = container.with_exec(["npm", "test"])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)

    async def solve(self, container: dagger.Container):
        result = container.with_exec(["npm", "run", "solve"])
        result = await result.sync()
        stdout = await result.stdout()
        stderr = await result.stderr()
        self.report = self.report.mutate(stdout, stderr)


async def handle(strategy, container):
    try:
        await strategy.test(container)
        await strategy.solve(container)
    except dagger.QueryError as e:
        strategy.report = strategy.report.mutate("", f"{e}", passed=False)
