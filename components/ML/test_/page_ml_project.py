from components._common.appheader import AppHeader
from components.ML.test_._project.navigationrail import ProjectNavigationRail
from components.ML.test_._project.create_dataset import CreateDatasetDataFrame, CreateDatasetImage

from components.ML.test_._project.select_algorithm import SelectAlgorithm

from components.ML.test_._project.nn.nn_modelbuild import ModelBuild_NN
from components.ML.test_._project.ml.ml_modelbuild import ModelBuild_ML

from components.ML.test_._project.nn.modelcompile import ModelCompile
from components.ML.test_._project.nn.modeltrain import ModelTrain_NN

from components.ML.test_._project.ml.ml_train import ModelTrain_ML

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
        model_build = ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER_OUTLINED, color=ft.colors.RED),
            selected_icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER, color=ft.colors.RED),
            label="モデル構築",
        )

        model_compile = ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER_OUTLINED, color=ft.colors.RED),
            selected_icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER, color=ft.colors.RED),
            label="コンパイル",
        )

        model_train = ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.WORK_OUTLINED, color=ft.colors.RED),
            selected_icon_content=ft.Icon(ft.icons.WORK, color=ft.colors.RED),
            label="モデルの学習",
        )


        select_alg = self.select_algorithm_content.check_now_content

        if select_alg != None:
            self.project_tasks = self.project_tasks[:2]
            self.navigation_rail.destinations = self.navigation_rail.destinations[:2]
            self.navigation_rail.destinations.append(model_build)
            self.project_tasks.append(ModelBuild_NN(self.page) if select_alg.data["alg"] == "NN" else ModelBuild_ML(self.page,select_alg.data["alg"]))
            if select_alg.data["alg"] == "NN":
                self.navigation_rail.destinations.append(model_compile)
                self.project_tasks.append(ModelCompile(self.page))
                self.navigation_rail.destinations.append(model_train)
                self.project_tasks.append(ModelTrain_NN(self.page))
            else:    
                self.navigation_rail.destinations.append(model_train)
                self.project_tasks.append(ModelTrain_ML(self.page))
            
        else:
            self.project_tasks = self.project_tasks[:2]
            self.navigation_rail.destinations = self.navigation_rail.destinations[:2]

        self.navigation_rail.update()


    
    def on_change_navigation_rail(self,e):
        print(self.project_tasks,e.control.selected_index)
        self.page_content.controls[2] = self.project_tasks[e.control.selected_index]
        self.page_content.update()