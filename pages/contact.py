import flet as ft
from flet_template.route import router


def page_view():
    return ft.View(
        vertical_alignment="center",
        horizontal_alignment="center",
        bgcolor="pink",
        controls=[
            ft.ElevatedButton(
                "index", width=120, height=45, on_click=lambda e: router(e, "/index")
            ),
            ft.ElevatedButton(
                "about", width=120, height=45, on_click=lambda e: router(e, "/about")
            ),
            ft.ElevatedButton(
                "contact",
                width=120,
                height=45,
                on_click=lambda e: router(e, "/contact"),
            ),
        ],
    )
