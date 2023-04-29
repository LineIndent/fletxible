"""
This is a base page template that setups a new page to be used in the web application.
The page is generated automatically when a user adds to the navigation list in the fletDocs.yml file.

"""


base_page = """import flet as ft
from route import router



def page_view(nav_color: str="%s"):
    return ft.View(
        bgcolor="%s",
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
                                    "%s",
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
                                        %s
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
                                    ft.Row(
                        expand=12, controls=[ft.Container(expand=True)]
                    ),
                    ft.Row(
                        expand=1, controls=[ft.Container(expand=True, bgcolor="black")]
                    ),

        ],
    )
        ]
        
        )

"""
