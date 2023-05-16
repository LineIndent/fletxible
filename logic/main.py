import flet as ft
from script import script


def main(page: ft.Page):
    # Run main automation script ...
    script(page)
    page.update()

    # playground
    page.platform  # prints OS name: macos, ios, etc ...

    def resize_event(event):
        if page.width <= 700:
            for nav in page.views[-1].controls[:]:
                nav.hide_navigation()

        else:
            for nav in page.views[-1].controls[:]:
                nav.show_navigation()

    page.on_resize = resize_event


if __name__ == "__main__":
    ft.flet.app(target=main)
