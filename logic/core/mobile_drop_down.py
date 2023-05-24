import flet as ft
from components.drop_down import DropDown


class MobileDropDownNavigation(DropDown):
    def __init__(
        self,
        type_="On this page",
        expanded_height=190,
        expanded=False,
        visible=False,  # make visible false ...
        icon_visible=False,
        controls_list=[
            ft.Container(
                padding=20,
                alignment=ft.alignment.top_left,
                content=ft.Column(
                    alignment="start",
                    horizontal_alignment="start",
                ),
            ),
        ],
    ):
        self.rail = []

        super().__init__(
            type_=type_,
            expanded_height=expanded_height,
            expanded=expanded,
            visible=visible,
            icon_visible=icon_visible,
            controls_list=controls_list,
        )

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
