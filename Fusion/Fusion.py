from ui.menu import Menu
from download.downloader import Downloader
from Packages.packager import Packager
from update.updater import Update
# Create the main menu
main_menu = Menu([
    ["Downloader", lambda: Downloader(main_menu=main_menu)],
    ["Packages", lambda: Packager(main_menu=main_menu)],
    ["Update", lambda:Update()],
    ["Exit", "exit"]
])

# Start the main menu
main_menu.start()
