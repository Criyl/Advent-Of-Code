import dagger

class PyStrategy():
    async def test(container: dagger.Container):
        result = container.with_exec(["pytest"])
        await result.sync()
        print(f"{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = container.with_exec(["python3", f"main.py"])
        await result.sync()
        print(f"{await result.stdout()}")


class GoLangStrategy():
    async def test(container: dagger.Container): 
        result = container.with_exec(["go","test","."])
        await result.sync()
        print(f"{await result.stdout()}")

    async def solve(container: dagger.Container):
        result = container.with_exec(["go","run","main.go"])
        await result.sync()
        print(f"{await result.stdout()}")
