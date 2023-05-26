import flet as ft


class Header(ft.Container):
    def __init__(
        self,
        full_nav: ft.Row,
        mobile_nav: ft.IconButton,
        bgcolor="#34373e",
        height=60,
        padding=ft.padding.only(left=60, right=60),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=4,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(2, 2),
        ),
    ):
        super().__init__(
            bgcolor=bgcolor,
            height=height,
            padding=padding,
            shadow=shadow,
        )

        self.full_nav = full_nav
        self.mobile_nav = mobile_nav

        self.content = ft.Row(
            alignment="spaceBetween",
            controls=[
                ft.Row(
                    alignment="start",
                    controls=[ft.Text("fletxible.", size=21, weight="w700")],
                ),
                self.full_nav,
                self.mobile_nav,
            ],
        )
