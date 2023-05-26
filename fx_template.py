import flet as ft
from base import FxControls
from components import typography as fxType
from components import block as fxCode

installation = """```python
$ pip3 install Fletxible
```
"""
update = """```python
$ Fletxible --version
```
"""


class FxView(ft.View):
    def __init__(
        self,
        page: ft.Page,
        route="",  # set your routes here ...
        bgcolor="#23262d",
        padding=0,
    ) -> None:
        self.page = page
        self.page.on_resize = self.fx_dynamics
        self.fx_view = FxControls(self.page, self.fx_controls(), self.fx_rail())

        super().__init__(route=route, bgcolor=bgcolor, padding=padding)

        self.controls = [ft.Container(expand=True, content=self.fx_view)]

    def fx_dynamics(self, event) -> None:
        if self.page.width <= 850:
            self.fx_view.set_application_to_mobile()
        else:
            self.fx_view.set_application_to_desktop()

    # Method: Create your side rails(fx_right panel) here by passing in strings...
    def fx_rail(self):
        return []

    # Method: Create your layout here. Create your UI inside this list ...
    def fx_controls(self, fx_drop_down_placeholder=ft.Container()) -> list:
        return [
            ft.Divider(height=15, color="transparent"),
            # start your layout design here ...
            fx_drop_down_placeholder,  # DO NOT remove this placeholder ...
            fxType.heading(f"Hi! Welcome to Fletxible!!"),
            fxType.subtitle("Start building your website with fletxible!!"),
            ft.Divider(height=5, color="transparent"),
            fxType.paragraph(
                "You can install Fletxible using with the following command: "
            ),
            fxCode.CodeBlock(installation),
            fxType.paragraph(
                "Make sure you've installed the latest version of fletxible: "
            ),
            fxCode.CodeBlock(update),
            # end your layout design here ...
            ft.Divider(height=15, color="transparent"),
        ]
