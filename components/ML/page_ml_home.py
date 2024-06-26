from components._common.appheader import AppHeader
from components.ML._home.pastproject import PastProject

import flet as ft


class MLHome(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MLHome"
        self.controls = [
            AppHeader(page),
            ft.Container(
                content = ft.Stack(
                    controls=[
                        PastProject(self.page),
                        ft.ElevatedButton(text="create_new_project",on_click=self.go_create_project,top=50,right=20),
                    ],
                    width=self.page.width,
                    height=self.page.height
                )
            )
        ]



    def next(self, e):
        self.page.go("/Page_Project")

    def go_create_project(self, e):
        self.page.go("/Page_CreateProject")

