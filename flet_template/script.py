import os, importlib.util
import yaml
from base import base_page
from route_base import route_page
import flet as ft
import pickle5 as pickle


class RouteButton(ft.ElevatedButton):
    def __str__(self, route):
        return f"ft.Text(size=14, weight='bold', spans=[ft.TextSpan('{route}', on_click=lambda e: router(e, '/{route}'))])"


class RouteEvent:
    def __str__(self, route):
        st = f"\tif route == '/{route}':\n\t\te.page.views.append(returned_modules[route].loader.load_module().page_view())\n\t\te.page.go('/{route}')\n"

        st = st.expandtabs(4)
        return st


theme_template: dict = {}
_modules: dict = {}


def run_template_script():
    # Load the YAML file
    with open("fletDocs.yml", "r") as file:
        fletDocs = yaml.safe_load(file)

    theme_template["site-name"] = fletDocs["site-name"]
    theme_template["bgcolor"] = fletDocs["theme"][0]["bgcolor"]
    theme_template["primary"] = fletDocs["theme"][1]["primary"]
    theme_template["accent"] = fletDocs["theme"][2]["accent"]

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

    # Loop over name navigation
    # If the base.txt file is not found, it will create one in the ./flet_template directory
    with open("./flet_template/base.txt", "w") as f, open(
        "./flet_template/router.txt", "w"
    ) as k:
        for page in fletDocs["nav"]:
            for key in page:
                obj = RouteButton()
                event = RouteEvent()
                value = os.path.splitext(page[key])[0]
                f.write(f"{obj.__str__(value)}," + "\n")
                k.write(f"{event.__str__(value)}")

    with open("./flet_template/router.txt", "r") as z, open(
        "./flet_template/route.py", "w"
    ) as f:
        content = z.read()
        f.write(route_page % content)

    # Loop over the nav list and create/update files
    for page in fletDocs["nav"]:
        for key in page:
            filename = f"{page[key]}"
            filepath = os.path.join("pages", filename)

            if not os.path.exists(filepath):
                with open("./flet_template/base.txt", "r") as z, open(
                    filepath, "w"
                ) as f:
                    content = z.read()
                    primary = theme_template["primary"]
                    site_name = theme_template["site-name"]
                    bgcolor = theme_template["bgcolor"]
                    filename = os.path.splitext(filename)[0]
                    f.write(f"{base_page % (primary, bgcolor, site_name, content)}")

            filename = os.path.splitext(filename)[0]
            _modules["/" + filename] = importlib.util.spec_from_file_location(
                filename, filepath
            )

    # Write the updated dictionary data back to the JSON file
    with open("./flet_template/routes.pickle", "wb") as f:
        pickle.dump(_modules, f)

    return _modules, theme_template
