import flet as ft
from script import script


def main(page: ft.Page):
    # Run main automation script ...
    script(page)
    page.update()

    # playground
    page.platform  # prints OS name: macos, ios, etc ...

    # page.on_resize = delta_event


if __name__ == "__main__":
    ft.flet.app(target=main)
