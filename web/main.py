import importlib.util
import flet as ft
import os


def testRun(Page):
    router: dict = {}
    for page in os.listdir("web"):
        if os.path.isfile(f"web/{page}") and page not in (
            "main.py",
            "styles.py",
            "controls.py",
            "route.py",
        ):
            filename = os.path.splitext(page)[0]
            filepath = os.path.join("web", page)

            router["/" + filename] = importlib.util.spec_from_file_location(
                filename, filepath
            )

    for keys, __ in router.items():
        Page.views.append(router[keys].loader.load_module().View())


def main(page: ft.Page):
    testRun(page)

    # Web theme ...
    theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thickness=4,
            radius=10,
            main_axis_margin=5,
            cross_axis_margin=-10,
        )
    )
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme

    # Responsive navigation logic ...
    def resize_event(event):
        if page.width <= 900:
            for nav in page.views[-1].controls[:]:
                nav.content.hide_navigation()

        else:
            for nav in page.views[-1].controls[:]:
                nav.content.show_navigation()

    # Set's the index.py page as the first page.
    index = -1
    current = 1
    page.views[index], page.views[current] = page.views[current], page.views[index]
    page.update()

    # Page events ...
    page.on_resize = resize_event
    page.update()
    resize_event(None)
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
