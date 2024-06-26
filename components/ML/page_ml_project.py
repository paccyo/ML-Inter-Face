from components.ML._project.projectdata import ProjectData
from components.ML._project.dataselect import DataSelect
from components.ML._project.preprocessing import Preprocessing
from components.ML._project.modelbuild import ModelBuild
from components.ML._project.modelcompile import ModelCompile
from components.ML._project.modeltrain import ModelTrain
from components.ML._project.option import Option


import flet as ft


class MLProject(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MLProject"
        self.controls = [
            ft.Tabs(
                selected_index=1,
                animation_duration=300,
                tabs=[],
                expand=1,
            )
        ]

        self.controls[0].tabs = [
            ProjectData(page),
            DataSelect(page),
            Preprocessing(page),
            ModelBuild(page),
            ModelCompile(page),
            ModelTrain(page),
            Option(page)
        ]

