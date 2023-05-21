import os


def route_string_method(route):
    string = f"\tif route == '/{route}':\n\t\te.page.views[index], e.page.views[current] = e.page.views[current], e.page.views[index]\n\t\te.page.update()\n"

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
            string = f"ft.Text(size=13, weight='bold', spans=[ft.TextSpan('{filename.capitalize()}', on_click=lambda e: route(e, '/{filename}'))]),"
            route_list.append(string)

    return route_list


def set_app_route_method():
    string = """from script import route_keys

def route(e, route):
    current = -1
    index: int

    for view in e.page.views[:]:
        if view.route == route:
            index = e.page.views.index(view)
            
%s
"""

    return string


def set_app_default_pages():
    string = """# Flet module import
import flet as ft
from route import route
from controls import *

class Header(ft.Container):
    def __init__(
        self,
        *args,
        bgcolor="#34373e",
        height=60,
        padding=ft.padding.only(left=60, right=60),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=4,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(2, 2),
        ),
        full_nav: ft.Row,
        mobile_nav: ft.IconButton,
        **kwargs,
    ):
        super().__init__(
            *args,
            bgcolor=bgcolor,
            height=height,
            padding=padding,
            shadow=shadow,
            **kwargs,
        )

        self.full_nav = full_nav
        self.mobile_nav = mobile_nav

        self.content = ft.Row(
            alignment="spaceBetween",
            controls=[
                ft.Row(
                    alignment="start",
                    # Change the title here ...
                    controls=[ft.Text("fletxible.", size=21, weight="w700")],
                ),
                self.full_nav,
                self.mobile_nav,
            ],
        )


class MobileNavigation(ft.IconButton):
    def __init__(
        self,
        icon=ft.icons.MENU_SHARP,
        visible=False,
        icon_size=14,
        icon_color="white",
        on_click=callable,
    ):
        super().__init__(
            icon=icon,
            visible=visible,
            icon_size=icon_size,
            icon_color=icon_color,
            on_click=on_click,
        )


class Navigation(ft.Row):
    def __init__(
        self,
        *args,
        alignment="center",
        **kwargs,
    ):
        super().__init__(
            *args,
            alignment=alignment,
            **kwargs,
        )

        self.controls = [
            # The markers start/end should not be deleted ... they are updated automatically ...
            # start #

            # end #
        ]


class Drawer(ft.Container):
    def __init__(
        self,
        *args,
        expand=True,
        width=0,
        bgcolor="#23262d",
        shadow=None,
        animate=ft.Animation(550, "ease"),
        content=ft.Column(
            expand=True,
            opacity=0,
            animate_opacity=ft.Animation(200, "easeIn"),
        ),
        **kwargs,
    ):
        super().__init__(
            *args,
            expand=expand,
            width=width,
            bgcolor=bgcolor,
            shadow=shadow,
            animate=animate,
            content=content,
            **kwargs,
        )

        self.content.controls = [
            ft.Container(
                bgcolor="#34373e",
                height=60,
                content=ft.Row(
                    alignment="center",
                    controls=[
                        ft.Text(
                            "fletxible.",
                            size=21,
                            weight="w700",
                        )
                    ],
                ),
            )
        ]


class LeftPanel(ft.Container):
    def __init__(
        self,
        *args,
        expand=1,
        padding=ft.padding.only(top=65),
        content=ft.Column(expand=True, alignment="start"),
        **kwargs,
    ):
        super().__init__(
            *args,
            expand=expand,
            padding=padding,
            content=content,
            **kwargs,
        )

        self.content.controls = []


class RightPanel(ft.Container):
    def __init__(
        self,
        *args,
        expand=1,
        padding=ft.padding.only(top=65),
        content=ft.Column(expand=True, alignment="start"),
        middle_panel: ft.Container,
        **kwargs,
    ):
        super().__init__(
            *args,
            expand=expand,
            padding=padding,
            content=content,
            **kwargs,
        )

        self.middle_panel = middle_panel

        self.content.controls = generate_right_rail(
            number=0,
            title=[],
            funcOne=[
                (
                    lambda i: lambda __: self.middle_panel.content.scroll_to(
                        key=str(i), duration=500
                    )
                )(i)
                # Change the range as needed ...
                for i in range(0, 0)
            ],
            # Change the range as needed ...
            funcTwo=[lambda e: self.rail_hover_color(e) for __ in range(0)],
        )

    def rail_hover_color(self, e):
        if e.data == "true":
            e.control.content.color = "white"

        else:
            e.control.content.color = ft.colors.with_opacity(0.55, "white10")

        e.control.content.update()


class MiddlePanel(ft.Container):
    def __init__(
        self,
        *args,
        expand=5,
        padding=ft.padding.only(top=65, right=15, left=15),
        alignment=ft.alignment.top_center,
        content=ft.Column(expand=True, alignment="start", scroll="hidden"),
        mobile_rail: any,
        **kwargs,
    ):
        super().__init__(
            *args,
            expand=expand,
            padding=padding,
            alignment=alignment,
            content=content,
            **kwargs,
        )

        self.mobile_rail = mobile_rail

        self.content.controls = [
            ft.Divider(height=10, color="transparent"),
            self.mobile_rail,
            ft.Divider(height=10, color="transparent"),
            # start writing your code here ...
            
            # end your code here ...
            ft.Divider(height=40, color="transparent"),
        ]


class MobileDropDownNavigation(Admonitions):
    def __init__(
        self,
        *args,
        type_="On this page",
        expanded_height=190,
        expanded=False,
        visible=False,
        icon_visible=False,
        controls_list=[
            ft.Container(
                padding=20,
                alignment=ft.alignment.top_left,
                content=ft.Column(
                    alignment="start",
                    horizontal_alignment="start",
                ),
            ),
        ],
        **kwargs,
    ):
        self.rail = []

        super().__init__(
            *args,
            type_=type_,
            expanded_height=expanded_height,
            expanded=expanded,
            visible=visible,
            icon_visible=icon_visible,
            controls_list=controls_list,
            **kwargs,
        )

    def get_on_page_navigation(self, middle_panel):
        self.rail = generate_right_rail(
            number=0,
            title=[],
            funcOne=[
                (
                    lambda i: lambda __: middle_panel.content.scroll_to(
                        key=str(i), duration=500
                    )
                )(i)
                # Change the range as needed ...
                for i in range(0, 0)
            ],
            # Change the range as needed ...
            funcTwo=[lambda e: self.rail_hover_color(e) for __ in range(0)],
        )

        self.controls_list[0].content.controls = self.rail

    def rail_hover_color(self, e):
        if e.data == "true":
            e.control.content.color = "white"

        else:
            e.control.content.color = ft.colors.with_opacity(0.55, "white10")

        e.control.content.update()


class ViewControls(ft.UserControl):
    def __init__(self):
        #
        self.stack = ft.Stack(expand=True)

        #
        self.row = ft.Row(expand=True, spacing=2)

        #
        self.drawer = Drawer()

        #
        self.left_panel = LeftPanel()

        #
        self.drop = MobileDropDownNavigation()

        #
        self.middle_panel = MiddlePanel(mobile_rail=self.drop)
        self.drop.get_on_page_navigation(middle_panel=self.middle_panel)
        self.drop.rail.pop(0)

        #
        self.right_panel = RightPanel(middle_panel=self.middle_panel)

        #
        self.nav = Navigation()

        #
        self.nav_mobile = MobileNavigation(on_click=lambda e: self.show_drawer(e))

        #
        self.header = Header(full_nav=self.nav, mobile_nav=self.nav_mobile)

        super().__init__()

    def show_drawer(self, e):
        if self.drawer.width != 220:
            self.drawer.width = 220
            self.drawer.shadow = ft.BoxShadow(
                blur_radius=15,
                spread_radius=8,
                color=ft.colors.with_opacity(0.25, "black"),
                offset=(4, 4),
            )
            self.drawer.update()

            self.drawer.content.opacity = 1
            self.drawer.update()

        else:
            self.drawer.content.opacity = 0
            self.drawer.update()

            self.drawer.width = 0
            self.drawer.shadow = None
            self.drawer.update()

    def hide_navigation(self):
        self.nav.visible = False
        self.nav.update()

        self.left_panel.visible = False
        self.left_panel.update()

        self.right_panel.visible = False
        self.right_panel.update()

        self.drop.visible = True
        self.drop.update()

        self.nav_mobile.visible = True
        self.nav_mobile.update()

    def show_navigation(self):
        self.drawer.width = 0
        self.drawer.shadow = None
        self.drawer.update()

        self.nav.visible = True
        self.nav.update()

        self.left_panel.visible = True
        self.left_panel.update()

        self.right_panel.visible = True
        self.right_panel.update()

        self.drop.visible = False
        self.drop.update()

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
        self.stack.controls = [
            self.row,
            self.header,
            self.drawer,
        ]

        #
        return self.stack


class View(ft.View):
    def __init__(
        self,
        *args,
        route="/index",
        bgcolor="#23262d",
        padding=0,
        controls=[
            ft.Container(expand=True, content=ViewControls()),
        ],
        **kwargs,
    ):
        super().__init__(
            *args,
            route=route,
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
