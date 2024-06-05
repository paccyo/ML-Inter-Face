from components.project.projectdata import ProjectData
from components.project.dataselect import DataSelect
from components.project.preprocessing import Preprocessing
from components.project.modelbuild import ModelBuild
from components.project.modelcompile import ModelCompile
from components.project.option import Option

import flet as ft


class Project(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/ProjectPage"
        self.controls = [
            ft.Tabs(
                selected_index=1,
                animation_duration=300,
                tabs=[],
                expand=1,
            )
        ]

        self.controls[0].tabs = [
            ProjectData(self.controls[0]),
            DataSelect(self.controls[0]),
            Preprocessing(self.controls[0]),
            ModelBuild(self.controls[0]),
            ModelCompile(self.controls[0]),
            Option(self.controls[0])
        ]