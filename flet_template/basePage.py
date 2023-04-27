"""
This is a base page template that setups a new page to be used in the web application.

The page is generated automatically when a user adds to the navigation list in the fletDocs.yml file.

"""


base_page = """import flet as ft
import flet_material as fm


def page_view():
    return ft.View(
        route="%s",
        controls=[]
        
    )

"""
