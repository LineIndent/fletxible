import flet as ft


class Drawer(ft.Container):
    def __init__(
        self,
        docs: dict,
        expand=True,
        width=0,
        bgcolor="#23262d",
        shadow=None,
        animate=ft.Animation(550, "ease"),
        content=ft.Column(
            expand=True,
            opacity=0,
            animate_opacity=ft.Animation(200, "easeIn"),
        ),
    ):
        self.docs = docs
        background_color = self.docs["theme"][0]["bgcolor"]

        super().__init__(
            expand=expand,
            width=width,
            bgcolor=bgcolor,
            shadow=shadow,
            animate=animate,
            content=content,
        )

        self.content.controls = [
            ft.Container(
                bgcolor=background_color,
                height=60,
                content=ft.Row(
                    alignment="center",
                    controls=[
                        ft.Text(
                            # start #
'fletxible.',# end #
                            size=21,
                            weight="w700",
                        )
                    ],
                ),
            )
        ]
