from components._createproject.createprojectheader import AppHeader

import flet as ft
import datetime

class CreateProject(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_CreateProject"
        now_date = datetime.datetime.now()
        self.controls = [
            AppHeader(page),
            ft.TextField(
                value="new_project"+ now_date.strftime('%Y%m%d%H%M%S'),
                on_change=self.on_change_project_filename,
            )
        ]
        self.project_filename = ""

    def on_change_project_filename(self, e):
        self.project_filename = e.control.value
        print(self.project_filename)
        # e.con