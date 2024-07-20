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

        self.create_dataset_content = CreateDatasetImage(page=self.page) if self.info["data_type"] == "image" else CreateDatasetDataFrame(page=self.page)
        self.select_algorithm_content = SelectAlgorithm(page=self.page, navigation_rail_update=self.navigation_rail_update)
        
        self.project_tasks = [
            self.create_dataset_content,
            self.select_algorithm_content,

        ]

        self.navigation_rail = ProjectNavigationRail(self.page,on_change=self.on_change_navigation_rail)

        self.page_content = ft.Row(
            controls=[
                self.navigation_rail,
                ft.VerticalDivider(width=1),
                self.project_tasks[0],
            ],
            expand=True,
            alignment=ft.alignment.top_left
        )
        

        self.controls = [
            AppHeader(self.page, toolbar_height=40),
            self.page_content,
        ]

    
    def navigation_rail_update(self):
        select_index = self.select_algorithm_content.check_now_index
        if select_index != None:
            self.project_tasks = self.project_tasks[:2]
            self.project_tasks.append(self.select_algorithm_content.algorithm_list[select_index])
            self.navigation_rail.destinations[2].disabled = False
        else:
            self.project_tasks = self.project_tasks[:2]
            self.navigation_rail.destinations[2].disabled = True
        self.navigation_rail.update()


    
    def on_change_navigation_rail(self,e):

        self.page_content.controls[2] = self.project_tasks[e.control.selected_index]
        
        self.page_content.update()