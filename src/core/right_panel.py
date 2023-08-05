import flet as ft


class RightPanel(ft.Container):
    def __init__(
        self,
        docs: dict,
        middle_panel: ft.Container,
        fx_rail: list,
        expand=1,
        padding=ft.padding.only(top=65, left=10),
    ):
        self.docs = docs
        self.highlight = self.docs.get("theme", "").get("bgcolor", "")

        self.middle_panel = middle_panel

        self.fx_rail = fx_rail
        self.adjusted_nav_rail = self.generate_right_rail_logic(self.fx_rail)

        self.rail_controls = ft.Column(
            expand=True, alignment="start", controls=self.adjusted_nav_rail
        )

        super().__init__(expand=expand, padding=padding)
        self.content = self.rail_controls

    def generate_right_rail_logic(self, fx_rail_list):
        nav_rail = [
            ft.Divider(height=35, color="transparent"),
            ft.Divider(height=25, color="transparent"),
        ]

        if len(fx_rail_list) != 0:
            for item in fx_rail_list:
                key = item[0]
                nav_rail.append(
                    ft.Container(
                        content=ft.Text(
                            item[1],
                            size=12,
                            weight="w500",
                        ),
                        on_hover=lambda e,: self.rail_hover_color(e),
                        on_click=lambda _, key=key: self.scroll_to_key(key),
                    )
                )

        return nav_rail

    def scroll_to_key(self, key):
        self.middle_panel.main_column.scroll_to(key=str(key), duration=500)

    def rail_hover_color(self, e):
        if e.data == "true":
            e.control.content.color = self.highlight

        else:
            e.control.content.color = ""

        e.control.content.update()
