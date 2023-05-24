import flet as ft
from router import route


class Navigation(ft.Row):
    def __init__(
        self,
        alignment="center",
    ):
        super().__init__(
            alignment=alignment,
        )

        self.controls = [
            # DO NOT REMOVE 'start' and 'end' markers!
            # start #
            ft.Text(
                size=13,
                weight="bold",
                spans=[ft.TextSpan("Index", on_click=lambda e: route(e, "/index"))],
            ),
            ft.Text(
                size=13,
                weight="bold",
                spans=[ft.TextSpan("About", on_click=lambda e: route(e, "/about"))],
            ),  # end #
        ]
