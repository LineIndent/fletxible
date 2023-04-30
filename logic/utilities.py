def route_string_method(route):
    string = f"\tif route == '/{route}':\n\t\te.page.views.append(returned_modules[route].loader.load_module().page_view())\n\t\te.page.go('/{route}')\n"

    string = string.expandtabs(4)
    return string


def set_app_route_method():
    string = """
def route(e, route):
    e.page.views.clear()
%s
"""

    return string


def set_app_default_pages():
    string = """# Flet module import
import flet as ft

# main view
def pageView():
    return ft.View(
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=[
            ft.Text("Hello World!", size=21)
        ]
    )
"""

    return string
