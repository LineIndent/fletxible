import flet as ft


class MiddlePanel(ft.Container):
    def __init__(
        self,
        components: list,
        function: list[callable],
        page: ft.Page,
        header_name: str,
        expand=5,
        padding=ft.padding.only(top=65, right=15, left=15),
        alignment=ft.alignment.top_center,
    ):
        self.page = page
        self.components = components
        self.header_name = header_name
        self.function = function

        self.main_column = ft.Column(
            expand=True, alignment="start", scroll="hidden", spacing=0
        )
        self.main_column.controls = self.components
        self.main_column.on_scroll = lambda e: self.get_scroll(e)
        super().__init__(expand=expand, padding=padding, alignment=alignment)
        self.content = self.main_column

    def get_scroll(self, e: ft.OnScrollEvent) -> None:
        if e.pixels >= float(2.0):
            self.function[0](60)
            self.function[1](0, False)
            self.function[2](self.page.route.replace("/", "").capitalize())

        if e.pixels <= float(1.9):
            self.function[2](self.header_name.name)
            if self.page.width >= 850:
                self.function[1](1, True)
                self.function[0](90)
