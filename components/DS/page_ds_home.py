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

                    ]
                ),
                padding=ft.padding.only(top=50,left=100,right=100,bottom=50)
            )

        ]

    def on_click_new_file(self, e):
        
        pass