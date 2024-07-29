from components.ML._createproject.picker_button_containers import Pick_file_Container,Pick_folder_Container
from components._common.appheader import AppHeader

from packages import DatasetCHK

import flet as ft
import os
import datetime
import shutil
import glob
import json

class MLCreateProject(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MLCreateProject"
        now_date = datetime.datetime.now()
        self.project_filename = "new_project"+ now_date.strftime('%Y%m%d%H%M%S')

        self.textfield_projectname = ft.Container(
            content=ft.TextField(
                value=self.project_filename,
                label="任意のプロジェクト名",
                on_change=self.on_change_project_filename,
            ),
            height=50,
        )
        self.segment_button_data_type = ft.CupertinoSegmentedButton(
            selected_index=0,
            controls=[ft.Text(".csv/.excel",size=30), ft.Text("画像",size=30)],
            on_change=self.on_change_segment_button_data_type,
            width=500,
        )

        self.segment_button_learning = ft.CupertinoSegmentedButton(
            selected_index=0,
            controls=[ft.Text("分類",size=30),ft.Text("回帰",size=30)],
            width=500,
            on_change=self.on_change_learning_way,
        )
        

        self.file_contener = Pick_file_Container(self.page, learning_way="categorical")
        self.folder_container = Pick_folder_Container(self.page, learning_way="categorical")

        self.get_pick_container = ft.Container(content=self.file_contener)

        self.controls = [
            AppHeader(page),
            ft.Container(
                content=ft.Column(
                    controls=[
                        self.textfield_projectname,
                        ft.Container(content=ft.Text(value="データタイプを選択"),alignment=ft.alignment.bottom_left),
                        self.segment_button_data_type,
                        ft.Container(content=ft.Text(value="回帰/分類を選択"),alignment=ft.alignment.bottom_left),
                        self.segment_button_learning,
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Container(content=ft.Text(value="データのインポート"),alignment=ft.alignment.bottom_left),
                                            self.get_pick_container,
                                        ]
                                    ),
                                    border=ft.border.all(color=ft.colors.BLACK),
                                    width=500,
                                ),
                                ft.Container(
                                    content=ft.ElevatedButton(
                                        text="create",
                                        on_click=self.on_click_create,
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                        height=50,
                                        width=100,
                                    ),
                                    alignment=ft.alignment.bottom_right,
                                    expand=True
                                )
                            ],
                        ),
                        
                    ]
                ),
                padding=ft.padding.only(top=70,left=60,right=60,bottom=20)
            )
        ]

    def on_change_learning_way(self, e):
        if e.control.controls[int(e.data)].value == "分類":
            self.file_contener.learning_way = "categorical"
            self.older_container.learning_way = "categorical"
        elif e.control.controls[int(e.data)].value == "回帰":
            self.file_contener.learning_way = "regression"
            self.older_container.learning_way = "regression"

        self.file_contener.update()
        self.older_container.update()

    def on_change_segment_button_data_type(self,e):
        if e.control.controls[int(e.data)].value == "画像":
            self.segment_button_learning.selected_index = 0
            self.segment_button_learning.disabled = True
            self.get_pick_container.content = self.folder_container
        else:
            self.segment_button_learning.disabled = False
            self.get_pick_container.content = self.file_contener
        self.get_pick_container.update()
        self.segment_button_learning.update()


    def on_change_project_filename(self, e):
        self.project_filename = e.control.value


    def on_click_create(self, e):
        with open("packages/util/project_info.json",encoding="utf-8") as f:
            info = json.load(f)
        if self.project_filename != "":
            info["project_name"] = self.project_filename 
            info["data_type"] = "image" if self.segment_button_data_type.selected_index == 1 else "dataframe"
            info["learning_type"] = "categorical" if self.segment_button_learning.controls[self.segment_button_learning.selected_index].value == "分類" else "regression"
            if self.get_pick_container.content.data:
                if info["data_type"] == "image":
                    info["data_info"][info["data_type"]]["data_path"] = self.get_pick_container.content.data
                    
                elif info["data_type"] == "dataframe":
                    info["data_info"][info["data_type"]] = "projects/"+info["project_name"]+"/Data/original_data.csv"
                

                path = os.path.abspath('projects/'+self.project_filename)
                # print(path)
                self.page.client_storage.set("project_file_path", path)
                
                os.makedirs(name=path,exist_ok=True)
                os.makedirs(name=path+"/Data",exist_ok=True)
                os.makedirs(name=path+"/Scripts",exist_ok=True)
                os.makedirs(name=path+"/Logs",exist_ok=True)
                os.makedirs(name=path+"/Result",exist_ok=True)
                shutil.copy("packages/image/metrics_0epoch.png", self.page.client_storage.get('project_file_path')+"/Result")
                shutil.copy("packages/image/loss_0epoch.png" ,self.page.client_storage.get('project_file_path')+"/Result") 

                check = DatasetCHK.CHK(
                    path=self.get_pick_container.content.data, 
                    data_type=info["data_type"], 
                    learning_way=self.file_contener.learning_way,
                    export_path="projects/"+info["project_name"]+"/Data"
                )
                if check[0]:
                    if info["data_type"] == "image":
                        info["data_info"][info["data_type"]]["sample_paths"] = check[1]
                    pass
                else:
                    return
                
                with open(path+"/project_info.json","w") as f:
                    json.dump(info, f, indent=2)
                self.page.client_storage.set("project_info",info)
                self.page.go("/Page_MLProject")
        else:
            pass
            