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
            # DO NOT REMOVE 'start' and 'end' markers!!
            # start #
            ft.Text(
                size=11,
                weight="bold",
                color="white",
                spans=[
                    ft.TextSpan(
                        "Index",
                        data="/index",
                        on_click=lambda __: self.page.go("/index"),
                    )
                ],
            ),
            ft.Text(
                size=11,
                weight="bold",
                color="white",
                spans=[
                    ft.TextSpan(
                        "About",
                        data="/about",
                        on_click=lambda __: self.page.go("/about"),
                    )
                ],
            ),  # end #
        ]
