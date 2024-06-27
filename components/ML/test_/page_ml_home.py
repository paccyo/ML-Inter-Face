from components._common.appheader import AppHeader
from components.ML.test_._home.pastproject import PastProject

import flet as ft


class MLHome(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MLHome"
        self.controls = [
            AppHeader(page),
            ft.Container(
                content = ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.ElevatedButton(text="create_new_project", on_click=self.go_create_project, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)), height=40, width=300),
                            alignment=ft.Alignment(1,-1),
                        ),
                        PastProject(self.page,alignment=ft.Alignment(0,0)),
                    ],
                ),
                padding=ft.padding.only(top=10,left=50,right=50,bottom=30)
            )
        ]



    def next(self, e):
        self.page.go("/Page_MLProject")

    def go_create_project(self, e):
        self.page.go("/Page_MLCreateProject")

