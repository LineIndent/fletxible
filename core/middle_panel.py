import flet as ft


class MiddlePanel(ft.Container):
    def __init__(
        self,
        controls: list,
        function: list[callable],
        page: ft.Page,
        expand=5,
        padding=ft.padding.only(top=65, right=15, left=15),
        alignment=ft.alignment.top_center,
        content=ft.Column(
            expand=True,
            alignment="start",
            scroll="hidden",
            spacing=0,
        ),
    ):
        super().__init__(
            expand=expand, padding=padding, alignment=alignment, content=content
        )
        self.page = page
        self.function = function
        self.controls = controls
        self.content.on_scroll = lambda e: self.get_scroll(e)
        self.content.controls = self.controls

    def get_scroll(self, e: ft.OnScrollEvent) -> None:
        if e.pixels >= float(2.0):
            self.function[0](60)
            self.function[1](0, False)

        if e.pixels <= float(1.9):
            if self.page.width >= 850:
                self.function[1](1, True)
                self.function[0](90)
