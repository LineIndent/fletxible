import flet as ft
from route import router


def page_view(nav_color: str = "red"):
    return ft.View(
        bgcolor="#2e2f3e",
        spacing=0,
        padding=0,
        vertical_alignment="start",
        controls=[
            ft.Column(
                expand=True,
                spacing=0,
                alignment="start",
                controls=[
                    ft.Row(
                        expand=2,
                        height=100,
                        spacing=0,
                        alignment="center",
                        controls=[
                            ft.Container(
                                expand=1,
                                height=80,
                                bgcolor=nav_color,
                                alignment=ft.alignment.center_right,
                                content=ft.Text(
                                    "Flet Web Material",
                                    size=22,
                                ),
                            ),
                            ft.Container(
                                expand=2,
                                height=80,
                                bgcolor=nav_color,
                                alignment=ft.alignment.center_right,
                                padding=ft.padding.only(right=35),
                                content=ft.Row(
                                    alignment="end",
                                    spacing=10,
                                    controls=[
                                        ft.Text(
                                            size=14,
                                            weight="bold",
                                            spans=[
                                                ft.TextSpan(
                                                    "index",
                                                    on_click=lambda e: router(
                                                        e, "/index"
                                                    ),
                                                )
                                            ],
                                        ),
                                        ft.Text(
                                            size=14,
                                            weight="bold",
                                            spans=[
                                                ft.TextSpan(
                                                    "about",
                                                    on_click=lambda e: router(
                                                        e, "/about"
                                                    ),
                                                )
                                            ],
                                        ),
                                        ft.Text(
                                            size=14,
                                            weight="bold",
                                            spans=[
                                                ft.TextSpan(
                                                    "contact",
                                                    on_click=lambda e: router(
                                                        e, "/contact"
                                                    ),
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(
                                expand=1,
                                height=80,
                                bgcolor=nav_color,
                                alignment=ft.alignment.center_left,
                                content=ft.Text("GitHub", size=15),
                            ),
                        ],
                    ),
                    ft.Row(expand=12, controls=[ft.Container(expand=True)]),
                    ft.Row(
                        expand=1, controls=[ft.Container(expand=True, bgcolor="black")]
                    ),
                ],
            )
        ],
    )
