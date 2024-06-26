from components._common.appheader import AppHeader

import flet as ft
import os
import datetime
import shutil
import glob

class MLCreateProject(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MLCreateProject"
        now_date = datetime.datetime.now()
        self.project_filename = "new_project"+ now_date.strftime('%Y%m%d%H%M%S')

        self.data_type = ft.Dropdown(
            options=[
                ft.dropdown.Option(text="image"),
                ft.dropdown.Option(text="csv"),
                ft.dropdown.Option(text="excel")
            ]
        )

        self.textfield_projectname = ft.Container(
            content=ft.TextField(
                value=self.project_filename,
                on_change=self.on_change_project_filename,
            ),
            alignment=ft.Alignment(-1,1),
            padding=ft.padding.only(left=100,right=100),
            height=50,
        )

        self.create_button = ft.Container(
            content=ft.ElevatedButton(
                text="create",
                on_click=self.on_click_create,
            ),
            alignment=ft.Alignment(0.5,-0.6)
        )

        self.controls = [
            AppHeader(page),
            ft.Column(
                controls=[
                    self.create_button,
                    self.textfield_projectname,
                ]
            )
        ]

    def on_change_project_filename(self, e):
        self.project_filename = e.control.value
        # print(self.project_filename)
        # e.con

    def on_click_create(self, e):
        if self.project_filename != "":
            path = os.path.abspath('projects/'+self.project_filename)
            # print(path)
            self.page.client_storage.set('project_path', path)
            os.makedirs(name=path,exist_ok=True)
            os.makedirs(name=path+"/Data",exist_ok=True)
            os.makedirs(name=path+"/Scripts",exist_ok=True)
            os.makedirs(name=path+"/Logs",exist_ok=True)
            os.makedirs(name=path+"/Result",exist_ok=True)
            shutil.copy("packages/image/metrics_0epoch.png", self.page.client_storage.get('project_path')+"/Result")
            shutil.copy("packages/image/loss_0epoch.png" ,self.page.client_storage.get('project_path')+"/Result")              
            self.page.go("/Page_Project")
        else:
            pass
            