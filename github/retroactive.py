import arrow

from github.metrics import fetch_all


def fetch(start_date, final_date=arrow.now(), freq: str="2W"):
    sprints = [
        sprint
        for sprint in arrow.Arrow.interval(
            frame="weeks", start=start_date, end=final_date, interval=2, exact=True
        )
    ]

    for start, end in sprints:
        sprint_metrics = fetch_all(
            start, end.date()
        )
        yield sprint_metrics

