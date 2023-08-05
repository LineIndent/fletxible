import flet as ft
from core.base import FxBaseView
import fx_material as fx  # noqa: F401
from pages.router import contact_navigation


class FxSubView(FxBaseView):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        route="/contact/index",  # place route here ...
    ):
        self.components = self.fx_controls()
        self.nav_rail = self.fx_rail()
        self.sub_nav = self.fx_sub_navigation()

        super().__init__(
            page=page,
            docs=docs,
            components=self.components,
            nav_rail=self.nav_rail,
            sub_nav=self.sub_nav,
            route=route,
        )

    def fx_sub_navigation(self) -> list[list]:
        return contact_navigation()

    def fx_rail(self) -> list[list]:
        return [
            ["1", "testing"],
        ]  # page navigation here ...

    def fx_controls(self) -> list:
        return [
            ft.Divider(height=35, color="transparent"),
            ft.Divider(height=25, color="transparent"),
            # Start your layout below #
            fx.heading("Inner CONTACT/INDEX Page"),
            # End your layout above #
            ft.Divider(height=15, color="transparent"),
        ]
