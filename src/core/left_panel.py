import flet as ft


class LeftPanel(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        routes: list[list],
        expand=1,
        padding=ft.padding.only(top=65),
        content=ft.Column(
            expand=True, alignment="start", horizontal_alignment="center"
        ),
    ):
        self.page = page
        self.routes = routes
        super().__init__(expand=expand, padding=padding, content=content)
        self.route_links = self.generate_sub_routes(self.routes)

        self.content.controls = self.route_links

    def generate_sub_routes(self, route_list: list[list]):
        route_links = [
            ft.Divider(height=35, color="transparent"),
            ft.Divider(height=25, color="transparent"),
        ]
        if route_list is not None:
            for route in route_list:
                route_links.append(self.route(title=route[0], route_to=route[1]))

            return route_links

    def route(self, title: str, route_to: str) -> ft.Control:
        return ft.Text(
            size=11,
            weight="bold",
            spans=[ft.TextSpan(title, on_click=lambda __: self.page.go(route_to))],
        )
