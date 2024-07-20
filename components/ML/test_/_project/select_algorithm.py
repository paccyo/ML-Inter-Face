from components.ML.test_._project.nn.nn_modelbuild import ModelBuild_NN
from components.ML.test_._project.ml.ml_modelbuild import ModelBuild_ML

from packages.util.Calldict import ML_display_dicts

import flet as ft 

class SelectAlgorithm(ft.Container):
    def __init__(self,page:ft.Page, navigation_rail_update):
        super().__init__()
        self.page = page
        self.navigation_rail_update = navigation_rail_update
        self.expand = True 
        self.ML_dicts = ML_display_dicts

        self.select_algorithm = ""
        self.check_now_index = None

        self.algorithm_list = [
            ModelBuild_NN(self.page),
            ModelBuild_ML(self.page,'DecisionTreeClassifier'),
            ModelBuild_ML(self.page,'DecisionTreeRegressor'),
            ModelBuild_ML(self.page,'LogisticRegression'),
            ModelBuild_ML(self.page,'RandomForestClassifier'),
            ModelBuild_ML(self.page,'RandomForestRegressor'),
            ModelBuild_ML(self.page,'SVC'),
            ModelBuild_ML(self.page,'SVR'),
        ]

        self.select_algorithm_button = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(),
                                ft.VerticalDivider(),
                                ft.Text(value=ML_name),
                            ]
                        ), 
                        on_click=self.on_click_algorithm, 
                        height=100, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                        data = ML_dict
                    ) for ML_name ,ML_dict in self.ML_dicts.items()
                ],
                scroll=ft.ScrollMode.HIDDEN,
            ),
            expand=True
        )


        self.content = ft.Column(
            controls=[
                ft.Container(content=ft.Text(value="アルゴリズムを選択",size=50), alignment=ft.alignment.center),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=self.select_algorithm_button, 
                            expand=True, 
                            bgcolor=ft.colors.RED, 
                            padding=ft.padding.only(top=70,bottom=70,left=50,right=50),
                        ),
                        ft.Container(
                            expand=True, 
                            bgcolor=ft.colors.BLUE
                        )
                    ],
                    expand=True
                )
            ]
        )


    def on_click_algorithm(self, e):
        
        if self.check_now_index == None:
            self.check_now_index = e.control.data["index"]
            self.page.client_storage.set("alg",self.select_algorithm_button.content.controls[self.check_now_index].data["alg"])
        elif self.check_now_index != e.control.data["index"]:
            self.page.client_storage.set("alg",self.select_algorithm_button.content.controls[self.check_now_index].data["alg"])
            self.select_algorithm_button.content.controls[self.check_now_index].content.controls[0].name = None
            self.select_algorithm_button.content.controls[self.check_now_index].update()
            self.check_now_index = e.control.data["index"]
        elif self.check_now_index == e.control.data["index"]:
            self.page.client_storage.set("alg",None) 
            self.check_now_index = None

        if e.control.content.controls[0].name == ft.icons.CHECK:
            e.control.content.controls[0].name = None
        else:
            e.control.content.controls[0].name = ft.icons.CHECK

        self.navigation_rail_update()
        e.control.update()