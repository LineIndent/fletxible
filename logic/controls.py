import flet as ft
import asyncio
from logic.styles import admonitions_color_scheme


def title(title):
    return ft.Text(value=title, size=21, weight="bold")


def subtitle(title, key=None):
    return ft.Text(value=title, size=17, weight="w700", key=key)


def text(title):
    return ft.Text(value=title, size=12, weight="w400")


def generate_right_rail(number: int, title: list, funcOne: list, funcTwo: list):
    rail_list: list = [
        ft.Divider(height=10, color="transparent"),
    ]

    if number != 0:
        for index in range(number):
            rail_list.append(
                ft.Container(
                    content=ft.Text(
                        title[index],
                        size=12,
                        color=ft.colors.with_opacity(0.55, "white10"),
                    ),
                    on_click=funcOne[index],
                    on_hover=funcTwo[index],
                )
            )

        return rail_list

    else:
        pass


class CodeBlock(ft.UserControl):
    def __init__(self, title):
        #
        self.title = title

        #
        self._hovered: bool | None = None

        self.copy_box = ft.Container(
            width=28,
            height=28,
            border=ft.border.all(1, "transparent"),
            right=1,
            top=1,
            border_radius=7,
            scale=ft.Scale(1),
            animate=ft.Animation(400, "ease"),
            alignment=ft.alignment.center,
            content=ft.Icon(
                name=ft.icons.COPY,
                size=14,
                color="white12",
                opacity=0,
                animate_opacity=ft.Animation(420, "ease"),
            ),
            on_click=lambda e: asyncio.run(self.get_copy_box_content(e)),
        )

        super().__init__()

    async def get_copy_box_content(self, e):
        self.title = self.title.replace("`", "")
        self.title = self.title.replace("python", "")
        e.page.set_clipboard(self.title)

        while self._hovered:
            self.copy_box.disabled = True
            self.copy_box.update()

            self.copy_box.content.opacity = 0
            self.copy_box.content.name = ft.icons.CHECK
            self.copy_box.update()

            await asyncio.sleep(0.25)

            self.copy_box.content.opacity = 1
            self.copy_box.content.color = "teal"
            self.copy_box.update()

            await asyncio.sleep(1)

            self.copy_box.content.opacity = 0
            self.copy_box.content.name = ft.icons.COPY
            self.copy_box.content.color = "white12"
            self.copy_box.update()

            self.copy_box.disabled = False
            self.copy_box.update()

            break

        if self._hovered == True:
            self.copy_box.content.opacity = 1

        else:
            self.copy_box.content.opacity = 0

        self.copy_box.content.update()

    def show_copy_box(self, e):
        if e.data == "true":
            self.copy_box.border = ft.border.all(0.95, "white10")
            self.copy_box.content.opacity = 1
            self._hovered = True

        else:
            self.copy_box.content.opacity = 0
            self.copy_box.border = ft.border.all(0.95, "transparent")
            self._hovered = False

        self.copy_box.update()

    def build(self):
        return ft.Row(
            alignment="start",
            vertical_alignment="center",
            controls=[
                ft.Container(
                    expand=True,
                    padding=5,
                    border_radius=7,
                    bgcolor="#282b33",
                    on_hover=lambda e: self.show_copy_box(e),
                    content=ft.Stack(
                        controls=[
                            ft.Markdown(
                                value=self.title,
                                selectable=True,
                                extension_set="gitHubWeb",
                                code_theme="atom-one-dark-reasonable",
                                code_style=ft.TextStyle(size=12),
                            ),
                            self.copy_box,
                        ],
                    ),
                )
            ],
        )


class Admonitions(ft.Container):
    def __init__(
        self,
        type_: str,
        expanded_height: int,
        expanded: bool,
        icon_visible: bool,
        controls_list: list,
        *args,
        **kwargs,
    ):
        #
        self.type_ = type_
        self.expanded_height = expanded_height
        self.expanded = expanded
        self.controls_list = controls_list

        # define: control
        self.column = ft.Column(
            controls=self.controls_list,
        )

        # define admonition title properties
        bgcolor = admonitions_color_scheme.get(self.type_, {}).get("bgcolor", "#20222c")
        border_color = admonitions_color_scheme.get(self.type_, {}).get(
            "border_color", "white24"
        )
        icon = admonitions_color_scheme.get(self.type_, {}).get("icon", "white24")

        self.container = ft.Container(
            height=45,
            bgcolor=ft.colors.with_opacity(0.95, bgcolor),
            border_radius=6,
            padding=10,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        vertical_alignment="center",
                        alignment="start",
                        spacing=10,
                        controls=[
                            ft.Icon(
                                name=icon,
                                color=border_color,
                                size=18,
                                visible=icon_visible,
                            ),
                            ft.Text(
                                self.type_.capitalize(),
                                size=11,
                                weight="w700",
                            ),
                        ],
                    ),
                    ft.IconButton(
                        icon=ft.icons.ADD,
                        icon_size=15,
                        icon_color=border_color,
                        rotate=ft.Rotate(0, ft.alignment.center),
                        animate_rotation=ft.Animation(400, "easeOutBack"),
                        on_click=lambda e: self.resize_admonition(e),
                    ),
                ],
            ),
        )

        kwargs.setdefault("border", ft.border.all(0.95, border_color))
        kwargs.setdefault("clip_behavior", ft.ClipBehavior.HARD_EDGE)
        kwargs.setdefault("animate", ft.Animation(250, "ease"))
        kwargs.setdefault("expand", self.expanded)
        kwargs.setdefault("border_radius", 6)
        kwargs.setdefault("height", 48)
        kwargs.setdefault("padding", 0)
        kwargs.setdefault(
            "content",
            ft.Column(
                alignment="start",
                spacing=0,
                controls=[
                    self.container,
                    self.column,
                ],
            ),
        )

        super().__init__(*args, **kwargs)

    # method: expand and retract admonition control + animation set
    def resize_admonition(self, e):
        if self.height != self.expanded_height:
            self.height = self.expanded_height
            self.container.border_radius = ft.border_radius.only(
                top_left=6, top_right=6
            )
            e.control.rotate = ft.Rotate(0.75, ft.alignment.center)
        else:
            self.height = 48
            e.control.rotate = ft.Rotate(0, ft.alignment.center)
            self.container.border_radius = 6

        self.update()
