import flet as ft
import flet_material as fm


def page_view():
    return ft.View(
        vertical_alignment="center",
        horizontal_alignment="center",
        controls=['ft.ElevatedButton(width=120, height=45, on_click=lambda e: e.page.go())', 'ft.ElevatedButton(width=120, height=45, on_click=lambda e: e.page.go())', 'ft.ElevatedButton(width=120, height=45, on_click=lambda e: e.page.go())']
        
        )

