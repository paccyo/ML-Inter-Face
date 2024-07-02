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
                        ft.IconButton(
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            icon=ft.icons.FILE_OPEN_OUTLINED,
                            icon_size=100,
                            width=100,
                            height=100,
                            on_click=self.on_click_new_file,
                            ),
                        
                    ]
                ),
                padding=ft.padding.only(top=50,left=100,right=100,bottom=50)
            )

        ]

    def on_click_new_file(self, e):
        
        pass