import json
import pandas as pd

FILEPATH = "./metrics.json"

def get_merge_rate_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], i["merge_rate"]["merge_rate"], len(i["merge_rate"]["total_prs"])] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Merge Rate", "Total PRs"])
    return df

def get_open_to_merge_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], i["open_to_merge"]["mean_duration_in_hours"], i["open_to_merge"]["median_duration_in_hours"], i["open_to_merge"]["percentile_95_duration_in_hours"], i["open_to_merge"]["merged_pr_rate"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95", "Merge Rate"])
    return df

def get_open_to_merge_week_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = []
    for week in content["metrics"]:
        for pr in week["open_to_merge"]["total_prs"]:
            row = [week["key"], pr["duration_in_hours"]]
            data.append(row)

    df = pd.DataFrame(data, columns=["Week", "Duration in hours"])
    return df

def get_open_to_merge_for_last_week_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = []
    for week in content["metrics"]:
        for pr in week["open_to_merge"]["total_prs"]:
            row = [week["key"], pr["duration_in_hours"], pr["author"]]
            data.append(row)

    df = pd.DataFrame(data, columns=["Week", "Duration in hours", "Author"])
    df = df[df["Week"] == df['Week'].max()]
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
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95", "Max Additions"])
    return df


def get_time_to_review_metrics_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], len(i["time_to_review"]["total_prs"]), i["time_to_review"]["unreviewed_prs"], i["time_to_review"]["prs_over_24h"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Total PRs", "Unreviewed PRs", "PRs Over 24 hours"])
    return df


def get_time_to_review_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], i["time_to_review"]["mean_duration_in_hours"], i["time_to_review"]["median_duration_in_hours"], i["time_to_review"]["percentile_95_duration_in_hours"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95"])
    return df


def get_time_to_open_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], i["time_to_open"]["mean_duration_in_hours"], i["time_to_open"]["median_duration_in_hours"], i["time_to_open"]["percentile_95_duration_in_hours"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95"])
    return df


def get_time_to_merge_dataframe():
    with open(FILEPATH) as f:
        content = json.load(f)

    data = [[i["key"], i["time_to_merge"]["mean_duration_in_hours"], i["time_to_merge"]["median_duration_in_hours"], i["time_to_merge"]["percentile_95_duration_in_hours"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95"])
    return df


