import flet as ft
from functools import partial


class Navigation(ft.Row):
    def __init__(
        self,
        page: ft.Page,
        function: callable,
        alignment="center",
    ):
        self.page = page

        # self.page.on_route_change = self.set_app_router
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
                size=13,
                weight="bold",
                spans=[
                    ft.TextSpan(
                        "Index",
                        data="/index",
                        on_click=lambda e: self.set_app_router(e),
                    )
                ],
            ),
            ft.Text(
                size=13,
                weight="bold",
                spans=[
                    ft.TextSpan(
                        "About",
                        data="/about",
                        on_click=lambda e: self.set_app_router(e),
                    )
                ],
            ),  # end #
        ]

    def set_app_router(self, route):
        self.page.views.clear()
        # begin #
        if route.control.data == "/index":
            self.page.views.append(
                self.page.data[route.control.data]
                .loader.load_module()
                .FxView(self.page)
            )
            self.page.go(route.control.data)

        if route.control.data == "/about":
            self.page.views.append(
                self.page.data[route.control.data]
                .loader.load_module()
                .FxView(self.page)
            )
            self.page.go(route.control.data)

        # finish #
        self.page.update()
