import numpy as np

from github.constants import (
    IDEAL_MERGE_RATE,
    IDEAL_OPEN_TO_MERGE,
    IDEAL_PR_SIZE,
    IDEAL_TIME_TO_REVIEW,
    IDEAL_TIME_TO_OPEN,
    IDEAL_TIME_TO_MERGE,
)
from github.aggregation import (
    merge_rate_dataframe,
    open_to_merge_dataframe,
    pr_size_metrics_dataframe,
    open_to_merge_for_last_week_dataframe,
    prs_table_dataframe,
    team_stats_dataframe,
    time_to_review_dataframe,
    time_to_open_dataframe,
    time_to_merge_dataframe,
)
from plots import (
    plot_line_chart,
    plot_line_chart_with_bar,
    plot_pie_chart,
    plot_table_chart,
)


def export(content):
    merge_rate_df = merge_rate_dataframe(content)
    ideal_merge_rate = np.repeat(IDEAL_MERGE_RATE, len(merge_rate_df))
    fig_merge_rate = plot_line_chart(
        merge_rate_df, "Merge Rate", "Week", ["Merge Rate"], ideal_merge_rate
    )

    open_to_merge_df = open_to_merge_dataframe(content)
    ideal_open_to_merge = np.repeat(IDEAL_OPEN_TO_MERGE, len(open_to_merge_df))
    fig_open_to_merge = plot_line_chart(
        open_to_merge_df,
        "Open to Merge Time",
        "Week",
        ["Mean", "Median", "Percentile 95"],
        ideal_open_to_merge,
    )

    pr_size_metrics_df = pr_size_metrics_dataframe(content)
    ideal_pr_size = np.repeat(IDEAL_PR_SIZE, len(pr_size_metrics_df))
    fig_pr_size = plot_line_chart_with_bar(
        pr_size_metrics_df,
        "PR Size",
        "Week",
        ["Mean", "Median", "Percentile 95"],
        "Max Additions",
        ideal_pr_size,
    )

    open_to_merge_by_author = open_to_merge_for_last_week_dataframe(content)
    fig_open_to_merge_by_author = plot_pie_chart(
        open_to_merge_by_author,
        "Last Week Open to Merge Time by Author",
        "Author",
        "Duration in hours",
    )

    time_to_review_df = time_to_review_dataframe(content)
    ideal_time_to_review = np.repeat(IDEAL_TIME_TO_REVIEW, len(time_to_review_df))
    fig_time_to_review = plot_line_chart(
        time_to_review_df,
        "Time to Review",
        "Week",
        ["Mean", "Median", "Percentile 95"],
        ideal_time_to_review,
    )

    time_to_open_df = time_to_open_dataframe(content)
    ideal_time_to_open = np.repeat(IDEAL_TIME_TO_OPEN, len(time_to_open_df))
    fig_time_to_open = plot_line_chart(
        time_to_open_df,
        "Time to Open",
        "Week",
        ["Mean", "Median", "Percentile 95"],
        ideal_time_to_open,
    )

    time_to_merge_df = time_to_merge_dataframe(content)
    ideal_time_to_merge = np.repeat(IDEAL_TIME_TO_MERGE, len(time_to_merge_df))
    fig_time_to_merge = plot_line_chart(
        time_to_merge_df,
        "Time to Merge",
        "Week",
        ["Mean", "Median", "Percentile 95"],
        ideal_time_to_merge,
    )

    prs_list_df = prs_table_dataframe(content)
    fig_prs_list = plot_table_chart(prs_list_df)

    team_stats_df = team_stats_dataframe(content)
    fig_team_stats = plot_table_chart(team_stats_df)

    with open("github/exports/ui/export.html", "w") as f:
        f.write(fig_team_stats.to_html(full_html=False, include_plotlyjs="cdn"))
        f.write(fig_prs_list.to_html(full_html=False, include_plotlyjs="cdn"))
        f.write(fig_merge_rate.to_html(full_html=False, include_plotlyjs="cdn"))
        f.write(fig_open_to_merge.to_html(full_html=False, include_plotlyjs="cdn"))
        f.write(fig_pr_size.to_html(full_html=False, include_plotlyjs="cdn"))
        f.write(
            fig_open_to_merge_by_author.to_html(full_html=False, include_plotlyjs="cdn")
        )
        f.write(fig_time_to_review.to_html(full_html=False, include_plotlyjs="cdn"))
        f.write(fig_time_to_open.to_html(full_html=False, include_plotlyjs="cdn"))
        f.write(fig_time_to_merge.to_html(full_html=False, include_plotlyjs="cdn"))
