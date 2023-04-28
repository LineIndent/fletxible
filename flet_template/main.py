import flet as ft
from script import run_template_script
import os, sys

#
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


#
def main(page: ft.Page):
    page.padding = 10
    returned_modules: dict = run_template_script()

    for keys, __ in returned_modules.items():
        print(keys)
        page.views.append(returned_modules[keys].loader.load_module().page_view())

    page.go("/index")
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
