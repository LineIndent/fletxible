import flet as ft
from core.drawer import Drawer
from core.left_panel import LeftPanel
from core.right_panel import RightPanel
from core.mobile_drop_down import MobileDropDownNavigation
from core.middle_panel import MiddlePanel
from core.navigation import Navigation
from core.mobile_navigation import MobileNavigation
from core.header import Header


class ViewControls(ft.UserControl):
    def __init__(self):
        #
        self.stack = ft.Stack(expand=True)

        #
        self.row = ft.Row(expand=True, spacing=2)

        #
        self.drawer = Drawer()

        #
        self.left_panel = LeftPanel()

        #
        self.drop = MobileDropDownNavigation()

        #
        # page_controls = self.PageControls()
        self.middle_panel = MiddlePanel(controls=[self.drop])
        # self.drop.get_on_page_navigation(middle_panel=self.middle_panel)
        # self.drop.rail.pop(0)

        #
        self.right_panel = RightPanel(middle_panel=self.middle_panel)

        #
        self.nav = Navigation()

        #
        self.nav_mobile = MobileNavigation(on_click=lambda e: self.show_drawer(e))

        #
        self.header = Header(full_nav=self.nav, mobile_nav=self.nav_mobile)

        super().__init__()

    def show_drawer(self, e):
        if self.drawer.width != 220:
            self.drawer.width = 220
            self.drawer.shadow = ft.BoxShadow(
                blur_radius=15,
                spread_radius=8,
                color=ft.colors.with_opacity(0.25, "black"),
                offset=(4, 4),
            )
            self.drawer.update()

            self.drawer.content.opacity = 1
            self.drawer.update()

        else:
            self.drawer.content.opacity = 0
            self.drawer.update()

            self.drawer.width = 0
            self.drawer.shadow = None
            self.drawer.update()

    def hide_navigation(self):
        self.nav.visible = False
        self.nav.update()

        self.left_panel.visible = False
        self.left_panel.update()

        self.right_panel.visible = False
        self.right_panel.update()

        self.drop.visible = True
        self.drop.update()

        self.nav_mobile.visible = True
        self.nav_mobile.update()

    def show_navigation(self):
        self.drawer.width = 0
        self.drawer.shadow = None
        self.drawer.update()

        self.nav.visible = True
        self.nav.update()

        self.left_panel.visible = True
        self.left_panel.update()

        self.right_panel.visible = True
        self.right_panel.update()

        self.drop.visible = False
        self.drop.update()

        self.nav_mobile.visible = False
        self.nav_mobile.update()

    def build(self):
        #
        self.row.controls = [
            self.left_panel,
            self.middle_panel,
            self.right_panel,
        ]

        #
        self.stack.controls = [
            self.row,
            self.header,
            self.drawer,
        ]

        #
        return self.stack


class View(ft.View):
    def __init__(
        self,
        bgcolor="#23262d",
        padding=0,
        controls=[
            ft.Container(expand=True, content=ViewControls()),
        ],
    ):
        super().__init__(
            bgcolor=bgcolor,
            padding=padding,
            controls=controls,
        )
