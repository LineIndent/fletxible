import os, importlib.util
import yaml
from base import base_page
import flet as ft
import pickle5 as pickle


class RouteButton(ft.ElevatedButton):
    def __str__(self, route):
        return f"ft.ElevatedButton('{route}', width=120, height=45, on_click=lambda e: e.page.go('/{route}'))"


def run_template_script():
    # Load the YAML file
    with open("fletDocs.yml", "r") as file:
        fletDocs = yaml.safe_load(file)

    # Check if "pages" directory exists
    pages_dir = None
    for root, dirs, files in os.walk("."):
        if "pages" in dirs:
            pages_dir = os.path.join(root, "pages")
            break

    if not pages_dir:
        # Create "pages" directory in the root folder
        pages_dir = os.path.join(os.getcwd(), "pages")
        os.mkdir(pages_dir)

    # Load the dictionary data from the JSON file, or create an empty dictionary if the file is empty
    try:
        with open("routes.pickle", "rb") as f:
            _modules = pickle.load(f)
    except FileNotFoundError as e:
        _modules = {}

    nav_list: list = []
    # Loop over name navigation
    with open("class.txt", "w") as f:
        for page in fletDocs["nav"]:
            for key in page:
                obj = RouteButton()
                value = os.path.splitext(page[key])[0]
                f.write(f"{obj.__str__(value)}," + "\n")

    # Loop over the nav list and create/update files
    for page in fletDocs["nav"]:
        for key in page:
            filename = f"{page[key]}"
            filepath = os.path.join("pages", filename)

            if not os.path.exists(filepath):
                with open("class.txt", "r") as z, open(filepath, "w") as f:
                    content = z.read()
                    filename = os.path.splitext(filename)[0]
                    f.write(f"{base_page % content}")

            filename = os.path.splitext(filename)[0]
            _modules["/" + filename] = importlib.util.spec_from_file_location(
                filename, filepath
            )

    # Write the updated dictionary data back to the JSON file
    with open("routes.pickle", "wb") as f:
        pickle.dump(_modules, f)

    # Loop over files in the pages directory and delete any files that are not listed in the nav
    for file in os.listdir("pages"):
        if file.endswith(".py"):
            found = False
            for page in fletDocs["nav"]:
                if page.get(next(iter(page))) == file:
                    found = True
                    break
            if not found:
                os.remove(os.path.join("pages", file))

    return _modules
