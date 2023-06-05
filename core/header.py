from core.repo_data import RepoData
import flet as ft


class Header(ft.Container):
    def __init__(
        self,
        docs: dict,
        full_nav: ft.Row,
        mobile_nav: ft.IconButton,
        height=90,
        padding=ft.padding.only(left=60, right=60),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=4,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(2, 2),
        ),
        animate=ft.Animation(500, "ease"),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    ):
        self.docs = docs
        self.repo_data = RepoData(self.docs)

        self.repo = self.docs["repo-url"]
        url = self.docs["repo-url"]

        self.name = self.docs["site-name"]
        self.background_color = self.docs["theme"][0]["bgcolor"]

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
                        ft.Text(
                            # start #
                            "fletxible.",  # end #
                            size=21,
                            weight="w700",
                        ),
                        self.repo,
                    ],
                ),
                #
                self.navigation,
            ],
        )
