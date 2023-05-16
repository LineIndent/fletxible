import flet as ft
from script import script


def main(page: ft.Page):
    # Run main automation script ...
    script(page)

    # Transition theme ...
    theme = ft.Theme()
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme

    # Responsive naivgation logic => set navigation for mobile/desktop
    def get_mobile():
        if page.platform == "ios":
            for nav in page.views[-1].controls[:]:
                nav.hide_navigation()

            for nav in page.views[-1].controls[:]:
                nav.show_navigation()

    # Responsive navigation logic ...
    def resize_event(event):
        if page.width <= 700:
            for nav in page.views[-1].controls[:]:
                nav.hide_navigation()

        else:
            for nav in page.views[-1].controls[:]:
                nav.show_navigation()

    page.on_resize = resize_event

    get_mobile()

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main, view="web_browser")
