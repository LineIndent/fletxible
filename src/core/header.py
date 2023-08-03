from core.repo_data import RepoData
import flet as ft
import time


class Header(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        full_nav: ft.Row,
        mobile_nav: ft.IconButton,
        height=90,
        padding=ft.padding.only(left=60, right=60),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=4,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(3, 3),
        ),
        animate=ft.Animation(500, "ease"),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    ):
        self.page = page
        self.docs = docs
        self.repo_data = RepoData(self.docs)

        url = self.docs.get("repo-url", "")

        self.name = self.docs.get("site-name", "")
        self.background_color = self.docs.get("theme", "").get("bgcolor", "")

        self.full_nav = full_nav
        self.mobile_nav = mobile_nav

        self.navigation = ft.Row(
            alignment="start",
            opacity=1,
            animate_opacity=ft.Animation(500, "ease"),
            vertical_alignment="start",
            controls=[
                self.full_nav,
            ],
        )
        self.repo = ft.Row(
            alignment="end",
            controls=[
                self.mobile_nav,
                ft.Column(
                    opacity=1,
                    animate_opacity=ft.Animation(500, "ease"),
                    alignment="center",
                    horizontal_alignment="start",
                    spacing=5,
                    controls=[
                        ft.Container(
                            on_click=lambda __: self.page.launch_url(url=url),
                            content=ft.Tooltip(
                                padding=10,
                                vertical_offset=25,
                                message="Go to repository",
                                bgcolor=ft.colors.with_opacity(0.85, "#20222c"),
                                text_style=ft.TextStyle(color="white", size=9),
                                content=self.repo_data,
                            ),
                        ),
                    ],
                ),
            ],
        )

        self.title = ft.Text(
            # start #
            "fletxible.",  # end #
            size=21,
            color="white",
            weight="w700",
            opacity=1,
            offset=ft.transform.Offset(0, 0),
            animate_opacity=ft.Animation(100, "ease"),
            animate_offset=ft.Animation(100, "ease"),
        )

        super().__init__(
            height=height,
            padding=padding,
            shadow=shadow,
            animate=animate,
            clip_behavior=clip_behavior,
        )

        self.bgcolor = self.background_color

        self.content = ft.Column(
            alignment="center",
            spacing=20,
            controls=[
                #
                ft.Row(
                    alignment="spaceBetween",
                    vertical_alignment="center",
                    controls=[
                        self.title,
                        ft.Row(
                            spacing=1,
                            alignment="end",
                            vertical_alignment="center",
                            controls=[
                                ft.IconButton(
                                    icon_size=14,
                                    icon=ft.icons.DARK_MODE_ROUNDED,
                                    icon_color="white",
                                    on_click=lambda e: self.toggle_theme(e),
                                ),
                                self.repo,
                            ],
                        ),
                    ],
                ),
                self.navigation,
            ],
        )

    def set_header_name(self, name: str):
        if name != self.title.value:
            self.title.opacity = 0
            self.title.offset = ft.transform.Offset(-0.25, 0)
            self.title.update()
            time.sleep(0.1)
            self.title.value = name
            self.title.offset = ft.transform.Offset(0, 0)
            self.title.opacity = 1
            self.title.update()

    def toggle_theme(self, e):
        if e.control.icon == ft.icons.LIGHT_MODE_ROUNDED:
            self.page.theme_mode = ft.ThemeMode.DARK
            e.control.icon = ft.icons.DARK_MODE_ROUNDED

        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            e.control.icon = ft.icons.LIGHT_MODE_ROUNDED

        self.page.update()
