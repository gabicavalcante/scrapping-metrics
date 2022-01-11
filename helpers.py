import json
import pandas as pd

FILEPATH = "./metrics.json"

def get_merge_rate_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], i["merge_rate"]["merge_rate"], len(i["merge_rate"]["total_prs"])] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Merge Rate", "Total PRs"])
    return df

def get_merge_time_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], i["merge_time"]["mean"], i["merge_time"]["median"], i["merge_time"]["percentile_95"], i["merge_time"]["merged_pr_rate"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95", "Merge Rate"])
    return df

def get_merge_time_week_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = []
    for week in content["metrics"]:
        for pr in week["merge_time"]["total_prs"]:
            row = [week["key"], pr["duration_in_hours"]]
            data.append(row)

    df = pd.DataFrame(data, columns=["Week", "Duration in hours"])
    return df

def get_pr_size_week_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = []
    for week in content["metrics"]:
        for pr in week["pr_size"]["total_prs"]:
            row = [week["key"], pr["additions"], pr["deletions"]]
            data.append(row)

    df = pd.DataFrame(data, columns=["Week", "Additions", "Deletions"])
    return df

def get_pr_size_metrics_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], i["pr_size"]["total_mean"], i["pr_size"]["total_median"], i["pr_size"]["total_percentile_95"], max([pr["additions"] for pr in  i["pr_size"]["total_prs"]])] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95", "Max"])
    return df


def get_time_to_review_metrics_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], len(i["time_to_review"]["total_prs"]), i["time_to_review"]["unreviewed_prs"], i["time_to_review"]["prs_over_24h"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Total PRs", "Unreviewed PRs", "PRs Over 24 hours"])
    return df