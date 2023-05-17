import os


def route_string_method(route):
    string = f"\tif route == '/{route}':\n\t\te.page.views.append(route_keys[route].loader.load_module().View())\n\t\te.page.go('/{route}')\n"

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

class ViewControls(ft.UserControl):
    def __init__(self):
        #
        self.stack = ft.Stack(expand=True)

        #
        self.row = ft.Row(expand=True, spacing=2)

        #
        self.left_panel = ft.Container(
            expand=1,
            padding=ft.padding.only(top=65),
            content=ft.Column(
                expand=True,
                alignment="start",
                controls=[],
            ),
        )

        #
        self.middle_panel = ft.Container(
            expand=5,
            padding=ft.padding.only(top=65, right=15, left=15),
            alignment=ft.alignment.top_center,
            content=ft.Column(
                expand=True,
                scroll="hidden",
                alignment="start",
                controls=[],
            ),
        )

        #
        self.right_panel = ft.Container(
            expand=1,
            padding=ft.padding.only(top=65),
            content=ft.Column(
                expand=True,
                alignment="start",
                controls=[],
            ),
        )

        self.nav = ft.Row(
            alignment="center",
            controls=[
                # start #
                
                # end #
            ],
        )

        #
        self.nav_mobile = ft.IconButton(
            icon=ft.icons.MENU_SHARP, visible=False, icon_size=14, icon_color="white"
        )

        #
        self.header = ft.Container(
            bgcolor="#34373e",
            height=60,
            padding=ft.padding.only(left=20, right=20),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=4,
                color=ft.colors.with_opacity(0.25, "black"),
                offset=ft.Offset(2, 2),
            ),
            content=ft.Row(
                alignment="spaceBetween",
                controls=[
                    ft.Row(
                        alignment="start",
                        controls=[ft.Text("fletxible.", size=21, weight="w700")],
                    ),
                    self.nav,
                    self.nav_mobile,
                ],
            ),
        )
        super().__init__()

    def hide_navigation(self):
        self.nav.visible = False
        self.nav.update()

        self.nav_mobile.visible = True
        self.nav_mobile.update()

    def show_navigation(self):
        self.nav.visible = True
        self.nav.update()

        self.nav_mobile.visible = False
        self.nav_mobile.update()

    def build(self):
        #
        self.row.controls = [
            self.left_panel,
            self.middle_panel,
            self.right_panel,
        ]

        #
        self.stack.controls = [self.row, self.header]

        #
        return self.stack


class View(ft.View):
    def __init__(
        self,
        *args,
        bgcolor="#23262d",
        padding=0,
        controls=[ft.Container(expand=True, content=ViewControls())],
        **kwargs,
    ):
        super().__init__(
            *args,
            bgcolor=bgcolor,
            padding=padding,
            controls=controls,
            **kwargs,
        )

"""

    return string


def set_up_yaml_file():
    string = """
site-name: ""
repo-url: ""

theme:
  - bgcolor: "#2e2f3e"
  - primary: "teal"
  - accent: "blue300"

nav:
  - Home: "index.py"
  - About: "about.py"

"""
    return string


def set_up_main_method():
    string = """# Modules for Flet and Fletxible
import flet as ft
from script import script


def main(page: ft.Page):
    # Run main script ... 
    script(page)
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)  
"""

    return string
