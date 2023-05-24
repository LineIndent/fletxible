import flet as ft


class RightPanel(ft.Container):
    def __init__(
        self,
        middle_panel: ft.Container,
        expand=1,
        padding=ft.padding.only(top=65),
        content=ft.Column(expand=True, alignment="start"),
    ):
        super().__init__(
            expand=expand,
            padding=padding,
            content=content,
        )

        self.middle_panel = middle_panel

        # self.content.controls = generate_right_rail(
        #     number=0,
        #     title=[],
        #     funcOne=[
        #         (
        #             lambda i: lambda __: self.middle_panel.content.scroll_to(
        #                 key=str(i), duration=500
        #             )
        #         )(i)
        #         # Change the range as needed ...
        #         for i in range(0, 0)
        #     ],
        #     # Change the range as needed ...
        #     funcTwo=[lambda e: self.rail_hover_color(e) for __ in range(0)],
        # )

    # def rail_hover_color(self, e):
    #     if e.data == "true":
    #         e.control.content.color = "white"

    #     else:
    #         e.control.content.color = ft.colors.with_opacity(0.55, "white10")

    #     e.control.content.update()
