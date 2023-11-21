import ci
import anyio
import dagger


ci.DAY_REGEX = r"^bad"

if __name__ == "__main__":
    try:
        anyio.run(ci.run_year)
    except dagger.ExecError as e:
        print(e)
    finally:
        for report in map(lambda strategy: strategy.report, ci.DAY_REPORTS):
            assert report.passed() is not True