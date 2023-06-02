import importlib.util
import flet as ft
import os
import yaml


with open("fx_config.yml", "r") as file:
    docs: dict = yaml.safe_load(file)


def main(page: ft.Page):
    # Web theme ...
    theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thickness=4,
            radius=10,
            main_axis_margin=5,
            cross_axis_margin=-10,
        ),
    )
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    page.theme = theme

    router = {}
    for file in os.listdir("web"):
        if os.path.isfile(f"web/{file}"):
            filename = os.path.splitext(file)[0]
            filepath = os.path.join("web", file)
            router["/" + filename] = importlib.util.spec_from_file_location(
                filename, filepath
            )

    for key, __ in router.items():
        page.views.append(router[key].loader.load_module().FxView(page, docs))

    page.data = router
    page.update()

    for view in page.views[1:]:
        view.fx_dynamics(event=None)

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
