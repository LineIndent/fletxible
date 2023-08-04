import flet as ft


class Navigation(ft.Row):
    def __init__(
        self,
        page: ft.Page,
        alignment="center",
    ):
        self.page = page

        super().__init__(alignment=alignment)
        self.controls = [
            self.route("Home", "/index"),
            self.route("About", "/about"),
            self.route("Contact", "/contact/index"),
        ]

    def route(self, title: str, route_to: str) -> ft.Control:
        return ft.Text(
            size=11,
            weight="bold",
            color="white",
            spans=[ft.TextSpan(title, on_click=lambda __: self.page.go(route_to))],
        )
