import flet as ft
from script import run_template_script


#
def main(page: ft.Page):
    run_template_script()
    page.padding = 0

    spec1 = ft.colors.with_opacity(0.1, "white")
    spec2 = ft.colors.with_opacity(0.05, "white")

    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            alignment="space_between",
            controls=[
                ft.Column(
                    expand=2,
                    alignment="start",
                    spacing=0,
                    controls=[
                        ft.Row(
                            expand=2,
                            height=80,
                            controls=[
                                ft.Container(expand=True, bgcolor="white10"),
                            ],
                        ),
                        ft.Row(
                            expand=1,
                            controls=[
                                ft.Container(expand=True, bgcolor="blue"),
                            ],
                        ),
                    ],
                ),
                ft.Row(expand=12, controls=[ft.Container(expand=True, bgcolor=spec2)]),
                ft.Row(expand=1, controls=[ft.Container(expand=True, bgcolor=spec1)]),
            ],
        )
    )

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
