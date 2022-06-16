import arrow

from datetime import date

from github_metrics.metrics.hotfixes_count import get_hotfixes_data
from github_metrics.metrics.merge_rate import get_merge_rate_data
from github_metrics.metrics.open_to_merge import get_open_to_merge_time_data
from github_metrics.metrics.pr_size import get_pr_size_data
from github_metrics.metrics.time_to_merge import get_time_to_merge_data
from github_metrics.metrics.time_to_open import get_time_to_open_data
from github_metrics.metrics.time_to_review import get_time_to_review_data
from github_metrics.request import fetch_prs_between


def fetch_all(
    start_date: date,
    end_date: date,
    include_hotfixes: bool = False,
    exclude_weekends: bool = True,
    exclude_authors: str = "",
    filter_authors: str = "",
):
    start_datetime = arrow.get(start_date)
    end_datetime = arrow.get(f"{end_date}T23:59:59")
    
    pr_list = fetch_prs_between(start_datetime, end_datetime)

    exclude_user_list = []
    if exclude_authors:
        exclude_user_list = exclude_authors.split(",")

    filter_user_list = []
    if filter_authors:
        filter_user_list = filter_authors.split(",")
    
    merge_rate = get_merge_rate_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_user_list,
        filter_authors=filter_user_list,
    ) 

    hotfixes = get_hotfixes_data(
        pr_list=pr_list,
        exclude_authors=exclude_user_list,
        filter_authors=filter_user_list,
    )

    open_to_merge = get_open_to_merge_time_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_user_list,
        filter_authors=filter_user_list,
        exclude_weekends=exclude_weekends,
    )

    pr_size = get_pr_size_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_user_list,
        filter_authors=filter_user_list,
    )

    time_to_merge = get_time_to_merge_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_user_list,
        filter_authors=filter_user_list,
        exclude_weekends=exclude_weekends,
    )

    time_to_open = get_time_to_open_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_user_list,
        filter_authors=filter_user_list,
        exclude_weekends=exclude_weekends,
    )

    time_to_review = get_time_to_review_data(
        pr_list=pr_list,
        include_hotfixes=include_hotfixes,
        exclude_authors=exclude_user_list,
        filter_authors=filter_user_list,
        exclude_weekends=exclude_weekends,
    )

    week_result = {
        "key": f"{start_datetime.isocalendar()[0]}/{start_datetime.isocalendar()[1]}",
        "merge_rate": merge_rate,
        "hotfixes": hotfixes,
        "open_to_merge": open_to_merge,
        "pr_size": pr_size,
        "time_to_merge": time_to_merge,
        "time_to_open": time_to_open,
        "time_to_review": time_to_review,
    }

    return week_result
