import flet as ft
from script import run_template_script


#
def main(page: ft.Page):
    returned_modules: dict = run_template_script()

    print(returned_modules)
    page.padding = 10

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
