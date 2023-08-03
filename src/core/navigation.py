import flet as ft


class Navigation(ft.Row):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        function: callable,
        alignment="center",
    ):
        self.docs = docs

        self.function = function

        self.index: int
        self.current = -1

        super().__init__(
            alignment=alignment,
        )

        self.page = page
        self.controls = [
            # start #
            self.router("Home", "/index"),
            self.router("About", "/about"),
            # end #
        ]

    def router(self, title: str, route_to: str):
        return ft.Text(
            size=11,
            weight="bold",
            color="white",
            spans=[ft.TextSpan(title, on_click=lambda __: self.page.go(route_to))],
        )
