import arrow

from github_metrics.metrics.hotfixes_count import get_hotfixes_data
from github_metrics.metrics.merge_rate import get_merge_rate_data
from github_metrics.metrics.open_to_merge import get_open_to_merge_time_data
from github_metrics.metrics.pr_size import get_pr_size_data
from github_metrics.metrics.time_to_merge import get_time_to_merge_data
from github_metrics.metrics.time_to_open import get_time_to_open_data
from github_metrics.metrics.time_to_review import get_time_to_review_data
from github_metrics.request import fetch_prs_between

start_date = "2021-06-22"
end_date = "2021-06-24"
include_hotfixes = False
exclude_weekends = True
exclude_authors = []
filter_authors = []
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

print(merge_rate)
print(hotfixes)
print(merge_time)
print(pr_size)
print(time_to_merge)
print(time_to_open)
print(time_to_review)
