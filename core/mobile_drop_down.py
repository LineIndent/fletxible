import flet as ft


class MobileDropDownNavigation(ft.Container):
    def __init__(
        self,
        max_height: int,
        controls_list: list,
        title="On this page ...",
        #
        border=ft.border.all(0.95, "white24"),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        animate=ft.Animation(250, "ease"),
        expand=True,
        border_radius=6,
        padding=0,
        height=48,
        content=ft.Column(alignment="start", spacing=0),
    ):
        self.title = title
        self.max_height = max_height
        self.controls_list = controls_list

        self.column = ft.Column(controls=[ft.Text("asdasd")])

        self.container = ft.Container(
            height=45,
            bgcolor=ft.colors.with_opacity(0.95, "#20222c"),
            border_radius=6,
            padding=10,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
                        # on_click=lambda e: self.resize_admonition(e),
                    ),
                ],
            ),
        )

        super().__init__(
            border=border,
            clip_behavior=clip_behavior,
            animate=animate,
            expand=expand,
            border_radius=border_radius,
            padding=padding,
            height=height,
            content=content,
        )

        self.content.controls = [self.container, self.column]

        # method: expand and retract admonition control + animation set

    # def resize_admonition(self, e):
    #     if self.height != self.expanded_height:
    #         self.height = self.expanded_height
    #         self.container.border_radius = ft.border_radius.only(
    #             top_left=6, top_right=6
    #         )
    #         e.control.rotate = ft.Rotate(0.75, ft.alignment.center)
    #     else:
    #         self.height = 48
    #         e.control.rotate = ft.Rotate(0, ft.alignment.center)
    #         self.container.border_radius = 6

    #     self.update()


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
