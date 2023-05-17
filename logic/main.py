import flet as ft
from script import script


def main(page: ft.Page):
    # Run main automation script ...
    script(page)

    # Transition theme ...
    theme = ft.Theme()
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
