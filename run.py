import json
import arrow

from github_metrics.metrics.hotfixes_count import get_hotfixes_data
from github_metrics.metrics.merge_rate import get_merge_rate_data
from github_metrics.metrics.open_to_merge import get_open_to_merge_time_data
from github_metrics.metrics.pr_size import get_pr_size_data
from github_metrics.metrics.time_to_merge import get_time_to_merge_data
from github_metrics.metrics.time_to_open import get_time_to_open_data
from github_metrics.metrics.time_to_review import get_time_to_review_data
from github_metrics.request import fetch_prs_between

start_date = "2021-10-25"
end_date = "2021-10-24"
include_hotfixes = False
exclude_weekends = True
exclude_authors = []
filter_authors = []

def get_all_github_metrics(start_date, end_date, include_hotfixes, exclude_weekends, exclude_authors, filter_authors):
    key = f"{start_date}-{end_date}"
    start_date = arrow.get(start_date)
    end_date = arrow.get(f"{end_date}T23:59:59")

    exclude_user_list = []
    if exclude_authors:
        exclude_user_list = exclude_authors.split(",")

    filter_user_list = []
    if filter_authors:
        filter_user_list = filter_authors.split(",")

    pr_list = fetch_prs_between(start_date, end_date)

    merge_rate = get_merge_rate_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_authors,
        filter_authors=filter_authors,
    )
    hotfixes = get_hotfixes_data(
        pr_list=pr_list, exclude_authors=exclude_authors, filter_authors=filter_authors
    )
    merge_time = get_open_to_merge_time_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_authors,
        filter_authors=filter_authors,
        exclude_weekends=exclude_weekends,
    )
    pr_size = get_pr_size_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_authors,
        filter_authors=filter_authors,
    )
    time_to_merge = get_time_to_merge_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_authors,
        filter_authors=filter_authors,
        exclude_weekends=exclude_weekends,
    )
    time_to_open = get_time_to_open_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_authors,
        filter_authors=filter_authors,
        exclude_weekends=exclude_weekends,
    )
    time_to_review = get_time_to_review_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_authors,
        filter_authors=filter_authors,
        exclude_weekends=exclude_weekends,
    )
    merge_time["mean"] = merge_time["mean"].total_seconds() / 3600
    merge_time["median"] = merge_time["median"].total_seconds() / 3600
    merge_time["percentile_95"] = merge_time["percentile_95"].total_seconds() / 3600
    week_result = {
        "key": f"{start_date.isocalendar()[0]}/{start_date.isocalendar()[1]}",
        "merge_rate": merge_rate,
        "hotfixes": hotfixes,
        "merge_time": merge_time,
        "pr_size": pr_size,
        "time_to_merge": time_to_merge,
        "time_to_open": time_to_open,
        "time_to_review": time_to_review,
    }

    with open("metrics.json") as f:
        old_file_content = json.load(f)
        if old_file_content == {}:
            old_file_content = {"metrics": []}

    old_file_content["metrics"].append(week_result)

    with open("metrics.json", 'w') as f:
        json.dump(old_file_content, f, indent=4, default=str)



sprints = [["2020-09-14", "2020-09-27"],
["2020-09-28", "2020-10-11"],
["2020-10-12", "2020-10-25"],
["2020-10-26", "2020-11-08"],
["2020-11-09", "2020-11-22"],
["2020-11-23", "2020-12-06"],
["2020-12-07", "2020-12-20"],
["2020-12-21", "2021-01-03"],
["2021-01-04", "2021-01-17"],
["2021-01-18", "2021-01-31"],
["2021-02-01", "2021-02-14"],
["2021-02-15", "2021-02-28"],
["2021-03-01", "2021-03-14"],
["2021-03-15", "2021-03-28"],
["2021-03-29", "2021-04-11"],
["2021-04-12", "2021-04-25"],
["2021-04-26", "2021-05-09"],
["2021-05-10", "2021-05-23"],
["2021-05-24", "2021-06-06"],
["2021-06-07", "2021-06-20"],
["2021-06-21", "2021-07-04"],
["2021-07-05", "2021-07-18"],
["2021-07-19", "2021-08-01"],
["2021-08-02", "2021-08-15"],
["2021-08-16", "2021-08-29"],
["2021-08-30", "2021-09-12"],
["2021-09-13", "2021-09-26"],
["2021-09-27", "2021-10-10"],
["2021-10-11", "2021-10-24"],
["2021-10-25", "2021-11-07"],
["2021-11-08", "2021-11-21"],
["2021-11-22", "2021-12-05"],
["2021-12-06", "2021-12-19"]]

for x, y in sprints:
    get_all_github_metrics(x, y, include_hotfixes, exclude_weekends, exclude_authors, filter_authors)
