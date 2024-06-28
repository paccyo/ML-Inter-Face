from components._common.appheader import AppHeader
from components.ML.test_._project.navigationrail import ProjectNavigationRail


import flet as ft


class MLProject(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MLProject"
        self.controls = [
            AppHeader(self.page, toolbar_height=30),
            ft.Row(
                controls=[
                    ProjectNavigationRail(self.page),
                    ft.VerticalDivider(width=1)
                ],
                expand=True,
                alignment=ft.alignment.top_left
            )
        ]
