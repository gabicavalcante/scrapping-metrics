from datetime import datetime, timedelta
import os
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
    open_to_merge = get_open_to_merge_time_data(
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

    week_result = {
        "key": f"{start_date.isocalendar()[0]}/{start_date.isocalendar()[1]}",
        "merge_rate": merge_rate,
        "hotfixes": hotfixes,
        "open_to_merge": open_to_merge,
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



if __name__ == "__main__":
    now = arrow.now()
    if now.weekday() == 0:
        include_hotfixes = False
        exclude_weekends = True
        filter_authors = ""
        exclude_authors = os.getenv('EXCLUDE_AUTHORS')

        with open("./last_run.txt") as f:
            content = f.read()

        if not content:
            start_date = str(now.date())
            end_date = (now.date() + timedelta(days=14))
        else:
            date = datetime.strptime(content, '%y-%m-%d')
            start_date = content
            end_date = date + timedelta(days=14)

        if now.date() > end_date.date():
            end_date = str(end_date.date())
            get_all_github_metrics(start_date, end_date, include_hotfixes, exclude_weekends, exclude_authors, filter_authors)
            with open("./last_run.txt", "w") as f:
                f.write(str(now.date()))
        else:
            pass

    else:
        pass
