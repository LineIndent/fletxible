import flet as ft


class MobileDropDownNavigation(ft.Container):
    def __init__(
        self,
        title: str,
        max_height: int,
        drop_rail: list[list],
        middle_panel: ft.Container,
        visible=False,
        height=45,
        bgcolor=ft.colors.with_opacity(0.95, "#20222c"),
        border=ft.border.all(0.85, "white24"),
        border_radius=6,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        animate=ft.Animation(300, "decelerate"),
        alignment=ft.alignment.top_left,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=4,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(4, 4),
        ),
    ):
        self.title = title
        self.middle_panel = middle_panel
        self.drop_rail = drop_rail

        self.max_height = max_height
        if self.max_height != 0:
            self.max_height = (max_height * 30) + 60

        self.drop_rail = self.generate_right_rail_logic(self.drop_rail)

        super().__init__(
            visible=visible,
            height=height,
            bgcolor=bgcolor,
            border=border,
            border_radius=border_radius,
            shadow=shadow,
            clip_behavior=clip_behavior,
            animate=animate,
            alignment=alignment,
        )

        self.content = ft.Column(
            expand=True,
            alignment="start",
            spacing=0,
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
                                        color="white",
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
                    padding=ft.padding.only(left=20, right=20, bottom=10, top=15),
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        alignment="spaceEven",
                        horizontal_alignment="start",
                        controls=self.drop_rail,
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

    def rail_hover_color(self, e):
        if e.data == "true":
            e.control.content.color = "white"

        else:
            e.control.content.color = ft.colors.with_opacity(0.55, "white10")

        e.control.content.update()

    def generate_right_rail_logic(self, fx_rail_list):
        nav_rail = []
        if len(fx_rail_list) != 0:
            for item in fx_rail_list:
                key = item[0]
                nav_rail.append(
                    ft.Container(
                        content=ft.Text(
                            item[1],
                            size=12,
                            color=ft.colors.with_opacity(0.55, "white10"),
                        ),
                        on_hover=lambda e,: self.rail_hover_color(e),
                        on_click=lambda _, key=key: self.scroll_to_key(key),
                    )
                )

        return nav_rail

    def scroll_to_key(self, key):
        self.middle_panel.main_column.scroll_to(key=str(key), duration=500)
