import flet as ft


class MobileDropDownNavigation(ft.Container):
    def __init__(
        self,
        title: str,
        max_height: int,
        #
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

        super().__init__(
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
                    bgcolor="blue100",
                    content=ft.Row(),
                ),
            ],
        )
        # self.content.controls = [self.container, self.column]

        # method: expand and retract admonition control + animation set

    def resize_admonition(self, e):
        if self.height != self.max_height:
            self.height = self.max_height
            # self.container.border_radius = ft.border_radius.only(
            #     top_left=6, top_right=6
            # )
            e.control.rotate = ft.Rotate(0.75, ft.alignment.center)
        else:
            self.height = 45
            e.control.rotate = ft.Rotate(0, ft.alignment.center)
            # self.container.border_radius = 6

        self.update()


# import flet as ft
# from components.drop_down import DropDown


# class MobileDropDownNavigation(DropDown):
#     def __init__(
#         self,
#         type_="On this page",
#         expanded_height=190,
#         expanded=False,
#         visible=False,
#         icon_visible=False,
#         controls_list=[
#             ft.Container(
#                 padding=20,
#                 alignment=ft.alignment.top_left,
#                 content=ft.Column(
#                     alignment="start",
#                     horizontal_alignment="start",
#                 ),
#             ),
#         ],
#     ):
#         self.rail = []

#         super().__init__(
#             type_=type_,
#             expanded_height=expanded_height,
#             expanded=expanded,
#             visible=visible,
#             icon_visible=icon_visible,
#             controls_list=controls_list,
#         )

# def get_on_page_navigation(self, middle_panel):
#     self.rail = generate_right_rail(
#         number=0,
#         title=[],
#         funcOne=[
#             (
#                 lambda i: lambda __: middle_panel.content.scroll_to(
#                     key=str(i), duration=500
#                 )
#             )(i)
#             # Change the range as needed ...
#             for i in range(0, 0)
#         ],
#         # Change the range as needed ...
#         funcTwo=[lambda e: self.rail_hover_color(e) for __ in range(0)],
#     )

#     self.controls_list[0].content.controls = self.rail

# def rail_hover_color(self, e):
#     if e.data == "true":
#         e.control.content.color = "white"

#     else:
#         e.control.content.color = ft.colors.with_opacity(0.55, "white10")

#     e.control.content.update()
