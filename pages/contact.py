import flet as ft
from route import router



def page_view():
    return ft.View(
        vertical_alignment="start",
        horizontal_alignment="center",
        controls=[
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
                        expand=3,
                        height=80,
                        spacing=5,
                        alignment="center",
                        controls=[
                            ft.Container(
                                expand=1,
                                height=80,
                                bgcolor=None,
                                alignment=ft.alignment.center_right,
                                content=ft.Text(
                                    "Placeholder",
                                    size=22,
                                ),
                            ),
                            ft.Container(
                                expand=2,
                                height=80,
                                bgcolor=None,
                                alignment=ft.alignment.center_right,
                                padding=ft.padding.only(right=35),
                                content=ft.Row(
                                    alignment="end", 
                                    spacing=10, 
                                    controls=[
                                        ft.Text(size=14, weight='bold', spans=[ft.TextSpan('index', on_click=lambda e: router(e, '/index'))]),
ft.Text(size=14, weight='bold', spans=[ft.TextSpan('about', on_click=lambda e: router(e, '/about'))]),
ft.Text(size=14, weight='bold', spans=[ft.TextSpan('contact', on_click=lambda e: router(e, '/contact'))]),

                                    ],
                                ),
                            ),
                            ft.Container(
                                expand=1,
                                height=80,
                                bgcolor=None,
                                alignment=ft.alignment.center_left,
                                content=ft.Text("GitHub", size=15),
                            ),
                        ],
                    ),
                    ft.Row(
                        expand=2,
                        controls=[
                            ft.Container(
                                expand=True,
                                bgcolor="blue",
                                content=ft.Row(expand=True),
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
        ]
        
        )

