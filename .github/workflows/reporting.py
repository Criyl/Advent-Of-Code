from dataclasses import dataclass, replace
from typing import Optional

@dataclass(frozen=True)
class DayReport:
    year: str
    day: str
    language: str
    out: str = ""
    err: str = ""
    passing: Optional[bool]  = None

    def passed(self) -> bool:
        return self.passing


def mutate(self, stdout, stderr, passed = True) -> DayReport:
    if self.passing == None:
        did_pass = passed
    else:
        did_pass = self.passing and passed

    copy = replace(
        self, 
        out = self.out+stdout, 
        err = self.err+stderr, 
        passing = did_pass
    )

    return copy
        
DayReport.mutate = mutate

def generate_report(reports):
    result = ""
    for report in reports:
        passed = report.passed()
        if passed:
            mark = f"⭐"
        else:
            mark = f"🚫\nERROR: {report.err}"

        result += f"{report.year}/{report.day}/{report.language} {mark}\n"
    return result