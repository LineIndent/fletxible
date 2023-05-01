# Flet module import
import flet as ft
from route import route


# main view
def pageView():
    return ft.View(
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=[
            ft.Row(
                alignment="center",
                controls=[
                    # start #
ft.Text(size=13, weight='bold', spans=[ft.TextSpan('index', on_click=lambda e: route(e, '/index'))]),
ft.Text(size=13, weight='bold', spans=[ft.TextSpan('about', on_click=lambda e: route(e, '/about'))]),# end #
                ],
            ),
            ft.Text("Hello World!", size=21),
        ],
    )
