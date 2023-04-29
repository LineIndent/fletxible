import click
import os


main_thread = """import flet as ft
from script import run_template_script


def main(page: ft.Page):
    returned_modules, theme_template = run_template_script()
    page.padding = 10
    page.bgcolor = theme_template["bgcolor"]

    for keys, __ in returned_modules.items():
        page.views.append(returned_modules[keys].loader.load_module().page_view())

    page.go("/index")
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)

"""

base_thread = """
'''This is a base page template that setups a new page to be used in the web application.
The page is generated automatically when a user adds to the navigation list in the fletDocs.yml file.'''




base_page = '''import flet as ft
from route import router


def page_view(nav_color: str="%s"):
    return ft.View(
        bgcolor="%s",
        spacing=0,
        padding=0,
        vertical_alignment="start",
        controls=[
            ft.Column(
        expand=True,
        spacing=0,
        alignment="start",
        controls=[
                    ft.Row(
                        expand=2,
                        height=100,
                        spacing=0,
                        alignment="center",
                        controls=[
                            ft.Container(
                                expand=1,
                                height=80,
                                bgcolor=nav_color,
                                alignment=ft.alignment.center_right,
                                content=ft.Text(
                                    "%s",
                                    size=22,
                                ),
                            ),
                            ft.Container(
                                expand=2,
                                height=80,
                                bgcolor=nav_color,
                                alignment=ft.alignment.center_right,
                                padding=ft.padding.only(right=35),
                                content=ft.Row(
                                    alignment="end", 
                                    spacing=10, 
                                    controls=[
                                        %s
                                    ],
                                ),
                            ),
                            ft.Container(
                                expand=1,
                                height=80,
                                bgcolor=nav_color,
                                alignment=ft.alignment.center_left,
                                content=ft.Text("GitHub", size=15),
                            ),
                        ],
                    ),
                                    ft.Row(
                        expand=12, controls=[ft.Container(expand=True)]
                    ),
                    ft.Row(
                        expand=1, controls=[ft.Container(expand=True, bgcolor="black")]
                    ),

        ],)])'''
"""

route_base_thread = """route_page = '''from script import run_template_script

returned_modules, __ = run_template_script()


def router(e, route):
    e.page.views.clear()
%s '''
    
"""

script_thread = """import os, importlib.util
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
        st = f'''\tif route == '/{route}':
        \t\te.page.views.append(returned_modules[route].loader.load_module().page_view())
        \t\te.page.go('/{route}')\n'''

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
                f.write(f"{obj.__str__(value)}," + '''\n''')
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
"""


@click.command()
def init():
    # Create YAML file
    with open("fletDocs.yml", "w") as f:
        f.write(
            """# Insert your web app details
    site-name: "Flet Web Material"
    repo-url: ""

    # Choose application theme
    theme:
    - bgcolor: "#2e2f3e"
    - primary: ""
    - accent: ""

    # nav tree
    nav:
    - Home: "index.py"
    - Page: "page.py"
    """
        )

    # Create templates directory if it doesn't exist
    if not os.path.exists("flet_template"):
        os.makedirs("flet_template")

    # Define the list of files to be generated
    file_list = ["__init__.py", "main.py", "base.py", "route_base.py", "script.py"]

    # Generate each file in the templates directory
    for file_name in file_list:
        file_path = os.path.join("flet_template", file_name)
        open(file_path, "a").close()

        # If it's the __init__.py file, write the import statements
        if file_name == "__init__.py":
            with open(file_path, "w") as f:
                f.write("from flet_template.base import base_page\n")
                f.write("from flet_template.main import main\n")
                f.write("from flet_template.script import run_template_script\n")
                f.write("from flet_template.route_base import route_page\n")

        # If it's the main.py file, write the main statements
        if file_name == "main.py":
            with open(file_path, "w") as f:
                f.write(main_thread)

        # If it's the base.py file, write the main statements
        if file_name == "base.py":
            with open(file_path, "w") as f:
                f.write(base_thread)

        # If it's the route_base.py file, write the main statements
        if file_name == "route_base.py":
            with open(file_path, "w") as f:
                f.write(route_base_thread)

        # If it's the scrip.py file, write the main statements
        if file_name == "script.py":
            with open(file_path, "w") as f:
                f.write(script_thread)

    click.echo(f"Generated {len(file_list)} files in the 'templates' directory.")
    click.echo(f"Get started by changing the fletDocs.yml file!")


@click.group()
def flet_template():
    pass


flet_template.add_command(init)

if __name__ == "__main__":
    flet_template()
