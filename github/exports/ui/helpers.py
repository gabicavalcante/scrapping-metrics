import json
import pandas as pd

def get_raw_metrics_from_file():
    FILEPATH = "./metrics.json"
    with open(FILEPATH) as f:
        content = json.load(f)
    return content

def get_merge_rate_dataframe(content):
    data = [[i["key"], i["merge_rate"]["merge_rate"], len(i["merge_rate"]["total_prs"])] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Merge Rate", "Total PRs"])
    return df

def get_open_to_merge_dataframe(content):
    data = [[i["key"], i["open_to_merge"]["mean_duration_in_hours"], i["open_to_merge"]["median_duration_in_hours"], i["open_to_merge"]["percentile_95_duration_in_hours"], i["open_to_merge"]["merged_pr_rate"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95", "Merge Rate"])
    return df

def get_open_to_merge_week_dataframe(content):
    data = []
    for week in content["metrics"]:
        for pr in week["open_to_merge"]["total_prs"]:
            row = [week["key"], pr["duration_in_hours"]]
            data.append(row)

    df = pd.DataFrame(data, columns=["Week", "Duration in hours"])
    return df

def get_open_to_merge_for_last_week_dataframe(content):
    data = []
    for week in content["metrics"]:
        for pr in week["open_to_merge"]["total_prs"]:
            row = [week["key"], pr["duration_in_hours"], pr["author"]]
            data.append(row)

    df = pd.DataFrame(data, columns=["Week", "Duration in hours", "Author"])
    df = df[df["Week"] == df['Week'].max()]
    return df

def get_pr_size_week_dataframe(content):
    data = []
    for week in content["metrics"]:
        for pr in week["pr_size"]["total_prs"]:
            row = [week["key"], pr["additions"], pr["deletions"]]
            data.append(row)

    df = pd.DataFrame(data, columns=["Week", "Additions", "Deletions"])
    return df

def get_pr_size_metrics_dataframe(content):
    data = [[i["key"], i["pr_size"]["total_mean"], i["pr_size"]["total_median"], i["pr_size"]["total_percentile_95"], max([pr["additions"] for pr in  i["pr_size"]["total_prs"]])] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95", "Max Additions"])
    return df


def get_time_to_review_metrics_dataframe(content):
    data = [[i["key"], len(i["time_to_review"]["total_prs"]), i["time_to_review"]["unreviewed_prs"], i["time_to_review"]["prs_over_24h"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Total PRs", "Unreviewed PRs", "PRs Over 24 hours"])
    return df


def get_time_to_review_dataframe(content):
    data = [[i["key"], i["time_to_review"]["mean_duration_in_hours"], i["time_to_review"]["median_duration_in_hours"], i["time_to_review"]["percentile_95_duration_in_hours"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95"])
    return df


def get_time_to_open_dataframe(content):
    data = [[i["key"], i["time_to_open"]["mean_duration_in_hours"], i["time_to_open"]["median_duration_in_hours"], i["time_to_open"]["percentile_95_duration_in_hours"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95"])
    return df


def get_time_to_merge_dataframe(content):
    data = [[i["key"], i["time_to_merge"]["mean_duration_in_hours"], i["time_to_merge"]["median_duration_in_hours"], i["time_to_merge"]["percentile_95_duration_in_hours"]] for i in content["metrics"]]
    df = pd.DataFrame(data, columns=["Week", "Mean", "Median", "Percentile 95"])
    return df


def get_prs_table_dataframe(content):
    data = []
    lastest = content["metrics"][-1]
    for pr in lastest["time_to_review"]["total_prs"]:
        reviewer_names = ", ".join([i["login"] for i in pr["reviewers"]]) if pr["reviewers"] else ""
        data.append([lastest["key"], pr["title"], pr["author"], reviewer_names, pr["duration_in_hours"]])
    df = pd.DataFrame(data, columns=["Week", "Title", "Author", "Reviewer(s)", "Time to Review"])
    return df


def get_team_stats_dataframe(content):
    data = []
    lastest = content["metrics"][-1]

    reviewed_prs = lastest["time_to_review"]["total_prs"]
    pr_size = lastest["pr_size"]["total_prs"]
    merged_prs = lastest["time_to_merge"]["merged_prs"]
    team = []
    team += [pr["author"] for pr in pr_size]
    team += [review["author"] for review in reviewed_prs]
    team += [m_pr["author"] for m_pr in merged_prs]
    team += [reviewer["login"] for review in reviewed_prs if review.get("reviewers") for reviewer in review.get("reviewers")]
    team = list(set(team))

    for person in team:
        prs = [pr["additions"] + pr["deletions"] for pr in pr_size if pr["author"] == person]
        loc = sum(prs)
        amount_prs = len(prs)
        reviewer_reviews = [
            reviewer
            for review in reviewed_prs if review.get("reviewers")
            for reviewer in review.get("reviewers", []) if reviewer["login"] == person
        ]
        amount_reviewed_by_person = len(reviewer_reviews)
        comments_by_person = [c for review in reviewer_reviews for c in review.get("comments", [])]
        amount_comments_by_person = len(comments_by_person)
        merged_prs_by_person = [pr for pr in merged_prs if pr["author"] == person]
        amount_merged_prs_by_person = len(merged_prs_by_person)
        # cycle_time_by_person =

        data.append(
            [person, loc, amount_prs, amount_reviewed_by_person, amount_comments_by_person, amount_merged_prs_by_person]
        )
    df = pd.DataFrame(data, columns=["Login", "LoC (added + deleted)", "PRs made", "Reviews made", "Comments made", "Merged PRs"])
    return df


