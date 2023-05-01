import os


def route_string_method(route):
    string = f"\tif route == '/{route}':\n\t\te.page.views.append(route_keys[route].loader.load_module().pageView())\n\t\te.page.go('/{route}')\n"

    string = string.expandtabs(4)
    return string


def navigation_example_method():
    route_list: list = []
    for file in os.listdir("pages"):
        # Set the path of the file to loop over folders and only include files
        path = os.path.join("pages", file)

        # If the path is NOT a folder, continue ...
        if not os.path.isdir(path):
            filename = os.path.splitext(file)[0]
            string = f"ft.Text(size=13, weight='bold', spans=[ft.TextSpan('{filename}', on_click=lambda e: route(e, '/{filename}'))]),"
            route_list.append(string)

    return route_list


def set_app_route_method():
    string = """from script import route_keys
def route(e, route):
    e.page.views.clear()
%s
"""

    return string


def set_app_default_pages():
    string = """# Flet module import
import flet as ft
from route import route

# main view
def pageView():
    return ft.View(
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=[
            ft.Row(
                alignment="center",
                controls=
                    [
                    # start #
                    
                    # end #       
                ],
            ),
            ft.Text("Hello World!", size=21)
        ]
    )
"""

    return string


############################################
######### Create config file YAML ##########
############################################


def set_up_yaml_file():
    string = """
site-name: ""
repo-url: ""

theme:
  - bgcolor: "#2e2f3e"
  - primary: "red"
  - accent: "blue300"

nav:
  - Home: "index.py"
  - About: "about.py"

"""
    return string
