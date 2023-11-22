import ci
import anyio
import dagger


if __name__ == "__main__":
    ci.DAY_REGEX = r"^bad"
    try:
        anyio.run(ci.run)
    except dagger.ExecError as e:
        print(e)
    finally:
        for report in list(map(lambda strategy: strategy.report, ci.DAY_REPORTS)):
            assert report.passed() is not True
