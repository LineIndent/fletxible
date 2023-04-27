import os
import yaml
from base import base_page
import flet as ft


class ContainerTitle(ft.Container):
    def __str__(self):
        return "ft.Container(width=100, height=100, bgcolor='pink')"


def run_template_script():
    # Load the YAML file
    with open("fletDocs.yml", "r") as file:
        fletDocs = yaml.safe_load(file)

    # Get user .yml file details
    bgcolor = fletDocs["theme"][0]["bgcolor"]
    site_name = fletDocs["site-name"]
    repo_url = fletDocs["repo-url"]

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

    # Loop over the nav list and create/update files
    for page in fletDocs["nav"]:
        for key in page:
            filename = f"{page[key]}"
            filepath = os.path.join("pages", filename)

            if not os.path.exists(filepath):
                with open(filepath, "w") as f:
                    filename = os.path.splitext(filename)[0]
                    f.write(f"{base_page % (bgcolor, filename, site_name, repo_url)}")

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
