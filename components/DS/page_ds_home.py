from components._common.appheader import AppHeader
import flet as ft


class DSHome(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_DSHome"

        self.controls = [
            AppHeader(page=self.page, title="DS InterFace", bgcolor=ft.colors.AMBER),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.ElevatedButton(text="new_file", on_click=self.on_click_new_file, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)), height=40, width=300),
                            alignment=ft.Alignment(1,-1),
                        ),
                        
                    ]
                ),
                padding=ft.padding.only(top=10,left=10,right=10,bottom=50)
            )

        ]

    def on_click_new_file(self, e):
        # self.page.go("/Page_DSNewFile")
        pass