import os
import csv
from contextlib import chdir


from rich.console import Console

console = Console()


def show_all_stored_data():
    with open('links.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            console.print(f"[yellow]{row[0]}[/yellow], [magenta]{row[1]}[/magenta], [blue]{row[2]}[/blue]")
        csv_file.close()


def update():
    with open('links.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            try:
                with chdir(row[2]):
                    download(row[1])
            except Exception:
                os.mkdir(row[2])
                with chdir(row[2]):
                    download(row[1])
        csv_file.close()


def write_data(playlist_name: str, link_value: str, path: str):
    with open('links.csv', mode='a') as link_file:
        link_writer = csv.writer(link_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        link_writer.writerow([playlist_name, link_value, path])
        link_file.close()


def download(link: str):
    os.system(f"python3 -m spotdl {link}")
