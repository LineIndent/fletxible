import flet as ft
from bs4 import BeautifulSoup
import httpx
import asyncio
from math import pi


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

        self.repo = self.docs["repo-url"]
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
        self.repo_data = asyncio.run(self.get_repo_data())

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
                        ft.Text("LineIndent/fletxible", size=11, weight="bold"),
                        ft.Row(
                            alignment="center",
                            vertical_alignment="center",
                            controls=self.repo_data,
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
'fletxible.',# end #
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

    # Method: gets the repo details based on the input repo URL ...
    async def get_repo_data(self):
        # await asyncio.sleep(5)
        controls_list: list = []

        icon_elements = ["LABEL_OUTLINED", "STAR_BORDER_SHARP", "CALL_SPLIT_SHARP"]

        span_elements: list = [
            "css-truncate css-truncate-target text-bold mr-2",
            "Counter js-social-count",
            "Counter",
        ]

        async with httpx.AsyncClient() as client:
            response = await client.get(self.repo)
            data = response.content

        soup = BeautifulSoup(data, "html.parser")

        for i, span in enumerate(span_elements):
            span_element = soup.find("span", span)
            if span_element is not None:
                text_content = span_element.text.strip()

                if i == 0:
                    icon = ft.Icon(
                        name=icon_elements[i], size=10, rotate=ft.Rotate(pi / 4)
                    )
                else:
                    icon = ft.Icon(name=icon_elements[i], size=10)

                controls_list.append(
                    ft.Row(
                        alignment="center",
                        spacing=0,
                        controls=[
                            icon,
                            ft.Text(
                                text_content,
                                size=10,
                                weight="w200",
                            ),
                        ],
                    )
                )

            else:
                pass

        return controls_list
