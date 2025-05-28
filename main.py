from helpers.installer import install_software

def update_packages():
    for package in packages:
        install_software(package)

try:
    import logging
    from rich.logging import RichHandler
    from rich.console import Console
    from helpers.data_manement import write_data, download, updater, show_all_stored_data
    import questionary
except:
    packages = ["spotdl", "rich", "questionary"]
    update_packages()

debug = True
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)


console = Console()
log = logging.getLogger("rich")


def new_entry():
    link = console.input("Add [blue]Link[/blue] to your Spotify Watcher: ")
    if link.startswith("https://open.spotify.com/"):
        name = console.input("Please enter the [green]Name[/green] for your Playlist/Album: ")
        location = path = questionary.path("Please enter the Location where you want to store your files: ").ask()
        write_data(name, link, location)
    else:
        console.print("Your [red]Link[/red] have to be from Spotify!")
        return

choices=["1 downlaod a single Song", 
        "2 Add a new Album/Playlist to the Watchlist", 
        "3 Manuelly update your Album/Playlists",
        "4 Display all stored data"]

def menu():
    while True:
        num = (
        questionary.select(
            "What do you want to do?",
            choices=choices,
        ).ask()
        or "do nothing"
    )
        if num == choices[0]:
            link = console.input("Enter the [blue]Link[/blue]: ")
            download(link)
        elif num == choices[1]:
            new_entry()
        elif num == choices[2]:
            updater()
        elif num == choices[3]:
            show_all_stored_data()
        else:
            console.print("Please select an [red]availible[/red] Option!")

if __name__ == "__main__":
    menu()
