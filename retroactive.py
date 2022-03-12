import pandas as pd

from run import get_all_github_metrics
from datetime import timedelta

sprint_inits = list(pd.date_range(start='2021-10-30', end='2022-01-11', freq='2W'))
sprint_ranges = []
_max = len(sprint_inits) - 1
for i, date in enumerate(sprint_inits):
    if i == _max:
        sprint_ranges.append(
            [
                str(date.date()),
                str(date.date() + timedelta(days=14))
            ]
        )
        break
    sprint_ranges.append(
        [
            str(date.date()),
            str(sprint_inits[i + 1].date() - timedelta(days=1))
        ]
    )

include_hotfixes = False
exclude_weekends = True
exclude_authors = []
filter_authors = []
for x, y in sprint_ranges:
    get_all_github_metrics(x, y, include_hotfixes, exclude_weekends, exclude_authors, filter_authors)
    print("Finished ", x, y)
