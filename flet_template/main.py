import flet as ft
from script import run_template_script


#


#
def main(page: ft.Page):
    page.padding = 10
    returned_modules: dict = run_template_script()
    page.views.append(returned_modules["/index"].loader.load_module().page_view())
    page.go("/index")
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
