from components._common.appheader import AppHeader
import flet as ft

class MainMenu(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MainMenu"
        self.controls = [
            AppHeader(self.page, title="ML/DS InterFace", bgcolor=ft.colors.LIME),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="ML",
                            on_click=self.on_click_ML,
                            width=200,
                            height=100,
                            bgcolor=ft.colors.BLUE,
                            style=ft.ButtonStyle(
                                color=ft.colors.WHITE,
                            )
                        ),
                        ft.ElevatedButton(
                            text="DS",
                            on_click=self.on_click_DS,
                            width=200,
                            height=100,
                            bgcolor=ft.colors.ORANGE,
                            style=ft.ButtonStyle(
                                color=ft.colors.WHITE,
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]

    def on_click_ML(self, e):
        self.page.go("/Page_MLHome")

    def on_click_DS(self, e):
        self.page.go("/Page_DSHome")