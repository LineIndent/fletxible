# Flet module import
import flet as ft
from route import route
from controls import *


code1 = """
```python
$ pip install Fletxible
```
"""
code2 = """
```python
$ fletxible-init
```
"""
code3 = """```python
import flet as ft
from script import script

def main(page: ft.Page):
    # Run main automation script ...
    script(page)

    # Transition theme ...
    theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thickness=4,
            radius=10,
            main_axis_margin=5,
            cross_axis_margin=-10,
        )
    )
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme

    # Responsive navigation logic ...
    def resize_event(event):
        if page.width <= 700:
            for nav in page.views[-1].controls[:]:
                nav.content.hide_navigation()

        else:
            for nav in page.views[-1].controls[:]:
                nav.content.show_navigation()

    # Page events ...
    page.on_resize = resize_event
    page.update()

if __name__ == "__main__":
    ft.flet.app(target=main)
```
"""

intro = "Fletxible is a Python web boilerplate project designed to provide a solid foundation for building web applications with Python and Flet. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their applications, without the need to spend time setting up infrastructure or configuring tools."

algo = """


1. open_yaml_script(): Loads data from the "flet_config.yml" file.

2. check_pages_directory_script(): Checks if a "pages" directory exists and creates one if not.

3. update_pages_directory_script(docs: dict): Loops over the files in the "pages" directory and deletes any files that are not listed in the navigation information.

4. handle_navigation_routing_script(docs: dict): Loops over the navigation information and writes route strings to a temporary file.

5. set_application_routing_script(docs: dict): Reads the temporary file created in the previous step, creates a route.py file with the appropriate routes, and deletes the temporary file.

6. set_default_methods_script(docs: dict): Loops over the navigation information and creates default pages for each page listed, and creates a route.pickle file with information about the modules used in the application.

7. map_yaml(yaml_file_path, output_file_path): Reads a YAML file and writes its contents to a Python file with a specified filename.

8. script(page: ft.Page): Main function that calls the other functions to process the data and set up the application.

"""


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
            # start #
ft.Text(size=13, weight='bold', spans=[ft.TextSpan('Index', on_click=lambda e: route(e, '/index'))]),
ft.Text(size=13, weight='bold', spans=[ft.TextSpan('About', on_click=lambda e: route(e, '/about'))]),# end #
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
            number=4,
            title=["Installation", "Application Setup", "Algorithm", "License"],
            funcOne=[
                (
                    lambda i: lambda __: self.middle_panel.content.scroll_to(
                        key=str(i), duration=500
                    )
                )(i)
                for i in range(1, 5)
            ],
            funcTwo=[lambda e: self.rail_hover_color(e) for __ in range(4)],
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
            title("Getting Started"),
            text(intro),
            ft.Divider(height=10, color="transparent"),
            subtitle("1. Installation", key="1"),
            text("To use Fletxible, you need to have the following installed:"),
            text("- Latest version of Flet\n- Python 3.5+"),
            text(
                "If you don't have Flet installed, installing Fletxible automatically installs it for you. You can install Fletxible using the following command:"
            ),
            CodeBlock(code1),
            ft.Divider(height=10, color="transparent"),
            subtitle("2. Application Setup", key="2"),
            text(
                "After installing Fletxible, you can test if it's working properly by running the following command:"
            ),
            CodeBlock(code2),
            text(
                "If the package was installed correctly, a directory named logic along with a file called flet_config.yml will be generated inside the root directory."
            ),
            ft.Column(
                alignment="center",
                # spacing=20,
                controls=[
                    text("\t\t1. __init__.py"),
                    text("\t\t2. main.py"),
                    text("\t\t3. script.py"),
                    text("\t\t4. utilities.py"),
                ],
            ),
            ft.Text(
                size=12,
                weight="w400",
                spans=[
                    ft.TextSpan(
                        text="The ",
                    ),
                    ft.TextSpan(
                        text="main.py",
                        style=ft.TextStyle(weight="bold"),
                    ),
                    ft.TextSpan(
                        text=" should look like this:",
                    ),
                ],
            ),
            CodeBlock(code3),
            ft.Divider(height=10, color="transparent"),
            subtitle("3. Current Algorithm Functions", key="3"),
            text(
                "This algorithm is a script that loads and processes data from a YAML file flet_config.yml that contains navigation information for a web application. The script then updates and creates various files and directories necessary for the application to function."
            ),
            CodeBlock(algo),
            text(
                "Overall, the script is part of a larger application development process that involves reading and processing data from a YAML file, creating and updating various files and directories, and setting up routing information for a web application."
            ),
            ft.Divider(height=10, color="transparent"),
            subtitle("4. License", key="4"),
            ft.Text(
                size=12,
                weight="w400",
                spans=[
                    ft.TextSpan(
                        text="Fletxible is open-source and licensed under the ",
                    ),
                    ft.TextSpan(
                        text="MIT License ",
                        style=ft.TextStyle(weight="bold", color="cyan"),
                        url="https://github.com/LineIndent/fletxible/blob/main/LICENSE",
                    ),
                    ft.TextSpan(
                        text=".",
                    ),
                ],
            ),
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
            number=4,
            title=[
                "Installation",
                "Application Setup",
                "Algorithm",
                "License",
            ],
            funcOne=[
                (
                    lambda i: lambda __: middle_panel.content.scroll_to(
                        key=str(i), duration=500
                    )
                )(i)
                for i in range(1, 5)
            ],
            funcTwo=[lambda e: self.rail_hover_color(e) for __ in range(4)],
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
