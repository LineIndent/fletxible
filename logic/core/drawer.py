import flet as ft


class Drawer(ft.Container):
    def __init__(
        self,
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
                bgcolor="#34373e",
                height=60,
                content=ft.Row(
                    alignment="center",
                    controls=[
                        ft.Text(
                            "fletxible.",
                            size=21,
                            weight="w700",
                        )
                    ],
                ),
            )
        ]
