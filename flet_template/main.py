import flet as ft
from script import run_template_script
import os, sys

ft.View()


#
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
