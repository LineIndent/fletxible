import importlib.util
import flet as ft
import os
import yaml


# Open the fx config YAML file and create a python dict object ...
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

    # Set application routing system ...
    router = {}
    for file in os.listdir("web"):
        if os.path.isfile(f"web/{file}"):
            filename = os.path.splitext(file)[0]
            filepath = os.path.join("web", file)
            router["/" + filename] = importlib.util.spec_from_file_location(
                filename, filepath
            )

    def route_change(route):
        page.views.clear()
        page.views.append(router[page.route].loader.load_module().FxView(page, docs))
        page.update()

    page.data = router


    # Set page responsive layout based on page width ...
    for view in page.views[1:]:
        view.fx_dynamics(event=None)

    page.on_route_change = route_change
    page.views.append(router["/installation"].loader.load_module().FxView(page, docs))
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
