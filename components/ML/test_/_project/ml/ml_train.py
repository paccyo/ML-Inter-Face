from packages import copy_to_userproject
from packages import GenerateBatfile

from packages import read_activate_path

import flet as ft
import glob
import shutil
import os
import time
import asyncio

class ModelTrain_ML(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page

        self.project_path = self.page.client_storage.get("project_file_path")
        self.alg = self.page.client_storage.get("alg")
        self.run = read_activate_path.read_activ_path()
        
        self.train_button_content = ft.Container(
            content=ft.ElevatedButton(text="train", on_click=self.on_click_pre_train),
            width=300,
        )

        self.image_content = ft.Container(
            content=ft.Column(
                controls=[],
                scroll=ft.ScrollMode.ALWAYS,
                expand=True,
            ),
            bgcolor=ft.colors.GREY_100,
            expand=True
        )

        self.content = ft.Container(
            content=ft.Row(
                controls=[
                    self.train_button_content,
                    self.image_content,
                ],
                expand=True
            ),
            expand=True,
            padding=ft.padding.all(20)
        )


    async def update_image(self):
        running = True
        t1 = None
        while running:

            await asyncio.sleep(0.2)
            self.image_content.content.controls = []
            result_files = glob.glob(self.project_path+"/Result/ML_result/*.png")
            print(result_files)
            if result_files != []:
                if t1 == None:
                    t1 = time.time()
                for result in result_files:
                    rect = ft.Container(
                        content=ft.Image(src=result,fit=ft.ImageFit.CONTAIN),
                        width=self.page.height-50,
                        height=self.page.height-50,
                    )
                    self.image_content.content.controls.append(rect)
                if time.time()-t1 > 1:
                    self.image_content.content.scroll = ft.ScrollMode.ALWAYS
                    self.image_content.update()
                    running = False


    def on_click_pre_train(self,e):
        self.project_path = self.page.client_storage.get("project_file_path")
        shutil.rmtree(self.project_path+"/Result/")
        os.makedirs(name=self.project_path+"/Result",exist_ok=True)
        shutil.copy("packages/image/metrics_0epoch.png", self.project_path+"/Result")
        shutil.copy("packages/image/loss_0epoch.png" ,self.project_path+"/Result")
        self.part_dict = self.page.client_storage.get("part_dict")

        self.page.run_task(self.update_image)

        self.on_click_train()


    def on_click_train(self):
        copy_to_userproject.CopyMLTrain(self.project_path+"/Scripts")
        GenerateBatfile.generateML(
            target_path=self.project_path+"/Scripts", 
            run_path=self.run, 
            part_dict=self.part_dict, 
            dataset_path=self.project_path+"/Data/dataset" , 
            export_path=self.project_path+"/Result", 
            alg=self.alg, 
            train_mode="categorical"
        )
        GenerateBatfile.Runbat(self.project_path+"/Scripts/run.bat")
