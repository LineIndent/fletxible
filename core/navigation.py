import flet as ft


class Navigation(ft.Row):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        function: callable,
        alignment="center",
    ):
        self.page = page
        self.docs = docs

        self.function = function

        self.index: int
        self.current = -1

        super().__init__(
            alignment=alignment,
        )

        self.controls = [
            # DO NOT REMOVE 'start' and 'end' markers!!
            # start #
            ft.Text(
                size=11,
                weight="bold",
                spans=[
                    ft.TextSpan(
                        "Installation",
                        on_click=lambda e: self.page.go("/installation"),
                    )
                ],
            ),
            ft.Text(
                size=11,
                weight="bold",
                spans=[
                    ft.TextSpan(
                        "About",
                        on_click=lambda e: self.page.go("/about"),
                    )
                ],
            ),  # end #
        ]

