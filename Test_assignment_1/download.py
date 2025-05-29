import click
import csv
import requests
import time


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-i', '--file_name', help='Input csv file name.')
def download(file_name):
    """Command line tool to check URL status and response time."""

    with open(file_name, 'r') as file:
        csv_file = csv.reader(file, delimiter='|')
        next(csv_file)
        for row in csv_file:
            try:
                start_time = time.time()
                response = requests.get(row[1], timeout=3)
                end_time = time.time() - start_time
                click.echo(
                    f'“{row[0]}”, HTTP {response.status_code}, time {end_time:.2f} seconds'
                )
            except requests.RequestException:
                click.echo(f'Skipping {row[1]}')


if __name__ == '__main__':
    download()
