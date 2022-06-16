import click
import arrow

from datetime import datetime, timedelta
import github

@click.command()
@click.option(
    "--start-date", 
    "start_date", 
    help="Start date."
) 
def github_metrics(start_date):
    if not start_date:
        start_date = arrow.now()
        end_date = (start_date + timedelta(days=14))
    else: 
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = (start_date + timedelta(days=14))
    
    click.echo(
        click.style(
            f"Scraping data from {start_date.date()} - {end_date.date()} ",
            bold=True,
        )
    )

    assert end_date.date() > start_date.date(), "Wrong date"
    assert end_date.date() < arrow.now().date(), f"End date in the future {end_date.date()} > {arrow.now().date()}"

    end_date = end_date.date()
    start_date = start_date.date()

    data = github.fetch_all(start_date, end_date)
    github.to_json(data)
    github.to_html()

if __name__ == '__main__':
    github_metrics()