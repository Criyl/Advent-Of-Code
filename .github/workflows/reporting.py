from dataclasses import dataclass, replace
from typing import Optional


@dataclass(frozen=True)
class DayReport:
    year: str
    day: str
    language: str
    out: str = ""
    err: str = ""
    passing: Optional[bool] = None

    def passed(self) -> bool:
        return self.passing

    def alt_name(self) -> str:
        return f"{self.year}/{self.day}/{self.language}"

    def __lt__(self, other):
        return self.alt_name() < other.alt_name()


def mutate(self, stdout, stderr, passed=True) -> DayReport:
    if self.passing is None:
        did_pass = passed
    else:
        did_pass = self.passing and passed

    copy = replace(self, out=self.out + stdout, err=self.err + stderr, passing=did_pass)

    return copy


DayReport.mutate = mutate


def generate_report(reports, sorted=True):
    result = ""
    passed_count = 0
    total_count = 0

    if sorted:
        reports.sort()

    for report in reports:
        total_count += 1

        if report.passed():
            mark = f"⭐"
            passed_count += 1
        else:
            mark = f"🚫\n{report.err}\n"

        result += "{0:30}{1}\n".format(f"{report.alt_name()}", mark)
    return f"""
{result}
---------------------------------
{passed_count}/{total_count} passed"""
