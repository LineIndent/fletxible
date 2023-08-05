import flet as ft
from core.base import FxBaseView
import fx_material as fx  # noqa: F401


class FxView(FxBaseView):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        route="",  # place route here ...
    ):
        self.components = self.fx_controls()
        self.nav_rail = self.fx_rail()

        super().__init__(
            page=page,
            docs=docs,
            components=self.components,
            nav_rail=self.nav_rail,
            route=route,
        )

    def fx_rail(self) -> list[list]:
        return []  # page navigation here ...

    def fx_controls(self) -> list:
        return [
            ft.Divider(height=35, color="transparent"),
            ft.Divider(height=25, color="transparent"),
            # Start your layout below #
            # End your layout above #
            ft.Divider(height=15, color="transparent"),
        ]
