import flet as ft


class MiddlePanel(ft.Container):
    def __init__(
        self,
        controls: list,
        expand=5,
        padding=ft.padding.only(top=65, right=15, left=15),
        alignment=ft.alignment.top_center,
        content=ft.Column(
            expand=True,
            alignment="start",
            scroll="hidden",
        ),
    ):
        super().__init__(
            expand=expand, padding=padding, alignment=alignment, content=content
        )

        self.controls = controls
        self.content.controls = self.controls
