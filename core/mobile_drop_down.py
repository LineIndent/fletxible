import flet as ft


class MobileDropDownNavigation(ft.Container):
    def __init__(
        self,
        title: str,
        max_height: int,
        # drop_rail: list,
        #
        visible=False,
        height=45,
        bgcolor=ft.colors.with_opacity(0.95, "#20222c"),
        border=ft.border.all(0.85, "white24"),
        border_radius=6,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        animate=ft.Animation(300, "decelerate"),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=4,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(4, 4),
        ),
    ):
        self.title = title

        self.max_height = max_height
        if self.max_height != 0:
            self.max_height = max_height * 50

        # self.drop_rail = drop_rail

        super().__init__(
            visible=visible,
            height=height,
            bgcolor=bgcolor,
            border=border,
            border_radius=border_radius,
            shadow=shadow,
            clip_behavior=clip_behavior,
            animate=animate,
        )

        self.content = ft.Column(
            expand=True,
            alignment="start",
            horizontal_alignment="start",
            controls=[
                ft.Container(
                    bgcolor="#20222c",
                    padding=ft.padding.only(left=20),
                    content=ft.Row(
                        height=42,
                        alignment="spaceBetween",
                        controls=[
                            ft.Row(
                                vertical_alignment="center",
                                alignment="start",
                                spacing=10,
                                controls=[
                                    ft.Text(
                                        self.title.capitalize(),
                                        size=11,
                                        weight="w700",
                                    ),
                                ],
                            ),
                            ft.IconButton(
                                icon=ft.icons.ADD,
                                icon_size=15,
                                icon_color="white24",
                                rotate=ft.Rotate(0, ft.alignment.center),
                                animate_rotation=ft.Animation(400, "easeOutBack"),
                                on_click=lambda e: self.resize_admonition(e),
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    padding=15,
                    content=ft.Column(
                        alignment="start",
                        horizontal_alignment="start",
                        controls=[
                            ft.Text("Hello!"),
                            ft.Text("Hello!"),
                            ft.Text("Hello!"),
                            ft.Text("Hello!"),
                            ft.Text("Hello!"),
                            ft.Text("Hello!"),
                            ft.Text("Hello!"),
                            ft.Text("Hello!"),
                        ]
                        # controls=self.drop_rail,
                    ),
                ),
            ],
        )

    def resize_admonition(self, e):
        if self.height != self.max_height:
            self.height = self.max_height
            e.control.rotate = ft.Rotate(0.75, ft.alignment.center)
        else:
            self.height = 45
            e.control.rotate = ft.Rotate(0, ft.alignment.center)

        self.update()
