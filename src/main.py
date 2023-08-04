import flet as ft
from config import config

from pages._error import Error404
import importlib
import psutil
import gc
import os


def get_list_of_pages_from_directory() -> list:
    pages_list = set()

    def loop_over_sub_folders(path: str):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if item == "__pycache__":
                continue
            if os.path.isfile(item_path) and item_path.endswith(".py"):
                pages_list.add(item_path)
            elif os.path.isdir(item_path):
                loop_over_sub_folders(item_path)

    for root, folders, files in os.walk("pages"):
        for folder in folders:
            path = os.path.join(root, folder)
            loop_over_sub_folders(path)

        for file in files:
            item_path = os.path.join(root, file)
            if os.path.isfile(item_path) and item_path.endswith(".py"):
                pages_list.add(item_path)

    return pages_list


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
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

    docs: dict = config
    list_of_pages = get_list_of_pages_from_directory()

    def generate_view_as_instance(route):
        for file in list_of_pages:
            # filename = file.split("/")[-1].split(".")[0]
            filename = file.split("pages", 1)[1].split(".")[0]
            filepath = file
            # if "/" + filename == route:
            if filename == route:
                module_spec = importlib.util.spec_from_file_location(filename, filepath)
                module = importlib.util.module_from_spec(module_spec)
                module_spec.loader.exec_module(module)
                try:
                    return module.FxView(page, docs)

                except AttributeError:
                    return Error404(page, docs)

        return Error404(page, docs)

    def change_route(route):
        page.views.clear()
        gc.collect()
        view = generate_view_as_instance(page.route)
        page.views.append(view)

        page.update()

        # print(f"After: {process.memory_info().rss / 1024 / 1024} MB")

    def resize_applications(event):
        for view in page.views[:]:
            if view.route is not None:
                if page.width <= 850:
                    view.set_application_to_mobile()
                else:
                    view.set_application_to_desktop()

    index = generate_view_as_instance("/index")
    page.views.append(index)

    psutil.Process()
    # print(f"Initial Memory used: {process.memory_info().rss / 1024 / 1024} MB")

    page.on_route_change = change_route
    page.on_resize = resize_applications

    page.update()

    # print(f"Memory after initial update: {process.memory_info().rss / 1024 / 1024} MB")


ft.app(target=main)
