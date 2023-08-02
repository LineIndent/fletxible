import flet as ft
from config import config

import importlib
import os
import psutil
import gc


def main(page: ft.Page):
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

    docs: dict = config  # noqa: F841

    def generate_view_as_instance(route):
        for file in os.listdir("pages"):
            if os.path.isfile(f"pages/{file}"):
                filename = os.path.splitext(file)[0]
                if "/" + filename == route:
                    filepath = os.path.join("pages", file)
                    module_spec = importlib.util.spec_from_file_location(
                        filename, filepath
                    )
                    module = importlib.util.module_from_spec(module_spec)
                    module_spec.loader.exec_module(module)
                    return module.FxView(page, docs)

    def change_route(route):
        page.views.clear()
        gc.collect()
        view = generate_view_as_instance(page.route)
        page.views.append(view)

        page.update()
        print(f"After: {process.memory_info().rss / 1024 / 1024} MB")

    def resize_applications(event):
        for view in page.views[:]:
            if view.route is not None:
                if page.width <= 850:
                    view.set_application_to_mobile()
                else:
                    view.set_application_to_desktop()

    index = generate_view_as_instance("/index")
    page.views.append(index)

    process = psutil.Process()
    print(f"Initial Memory used: {process.memory_info().rss / 1024 / 1024} MB")

    page.on_route_change = change_route
    page.on_resize = resize_applications

    page.update()

    print(f"Memory after initial update: {process.memory_info().rss / 1024 / 1024} MB")


ft.app(target=main)
