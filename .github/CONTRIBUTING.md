## How to add new Languages

#### The Container
Dockerfile's under `images/<language>` will be built with each individual challenges code mounted at `/src`

#####The Strategy
We use the [Strategy Design Pattern](https://refactoring.guru/design-patterns/strategy) to allow for flexibility in language support

See the example below on how to add your desired language

> Create a Strategy under `.github/workflows/solve_strategy.py`

```python
class PyStrategy:
    def before(container: dagger.Container) -> dagger.Container:
        # do operations on containers before the test or solve steps
        return container.with_workdir("/")
    
    async def test(container: dagger.Container):
        # do the test step
        result = container.with_exec(["pytest"])
        await result.sync()

    async def solve(container: dagger.Container):
        # do the solve step
        result = container.with_exec(["python3", "main.py"])
        await result.sync()
```

> Make sure to include your new strategy in the `SUPPORTED_LANGUAGE` dictionary located in `.github/workflows/ci.py`  
```python
SUPPORTED_LANGUAGE = {
    ...,
    "python": PyStrategy,
}
```

##### The Example
Include under `AoC0000/day_00/<language>` a main entry point and test files where applicable

##### The README
Finally update the support table on the `README.md` to include the new language

## Pull Request
Once all requirements under [How to add new Languages](#how-to-add-new-languages) are completed you can create a pull request which will be manually reviewed after all builds pass.

## Inquiry
If you need further guidance, you can contact me at `chris@carroll.codes`
