import flet as ft
from script import script


def main(page: ft.Page):
    script(page)
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
