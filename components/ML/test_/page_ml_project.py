from components._common.appheader import AppHeader
from components.ML.test_._project.navigationrail import ProjectNavigationRail
from components.ML.test_._project.create_dataset import CreateDatasetDataFrame, CreateDatasetImage
from components.ML.test_._project.select_algorithm import SelectAlgorithm

import flet as ft
import json

class MLProject(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MLProject"
        self.project_file_path = self.page.client_storage.get("project_file_path")
        self.info = {}
        with open(self.project_file_path+"/project_info.json") as f:
            self.info = json.load(f)

        self.create_dataset_content = CreateDatasetImage(self.page) if self.info["data_type"] == "image" else CreateDatasetDataFrame(self.page)
        self.select_algorithm_content = SelectAlgorithm(self.page)

        self.page_content = ft.Row(
            controls=[
                ProjectNavigationRail(self.page,on_change=self.on_change_navigation_rail),
                ft.VerticalDivider(width=1),
                self.create_dataset_content,
            ],
            expand=True,
            alignment=ft.alignment.top_left
        )
        

        self.controls = [
            AppHeader(self.page, toolbar_height=40),
            self.page_content,
        ]


    
    def on_change_navigation_rail(self,e):
        if e.control.selected_index == 0:
            self.page_content.controls[2] = self.create_dataset_content
        elif e.control.selected_index == 1:
            self.page_content.controls[2] = self.select_algorithm_content
        self.page_content.update()