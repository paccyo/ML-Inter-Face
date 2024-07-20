# from packages import RunTrain
from packages import copy_to_userproject,GenerateBatfile
from packages import read_activate_path

import flet as ft
import flet.canvas as cv
import glob
import asyncio
import shutil
import os

class ModelTrain_NN(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page

        self.project_path = self.page.client_storage.get("project_file_path")
        self.info_files = glob.glob(self.project_path+"/Scripts/*")
        print(self.info_files)
        self.metrics = None
        self.loss = None
        re = glob.glob(self.project_path+"/Result/*.png")
        for r in re:
            if "metrics" in re:
                self.metrics = re
            elif "loss" in re:
                self.loss = re
        if self.metrics == None:
            self.metrics = self.project_path+"/Result/metrics_0epoch.png"
        if self.loss == None:
            self.loss = self.project_path+"/Result/loss_0epoch.png"
        self.batch_size = 2
        self.epoch = 1000
        self.batch_input = ft.Container(
            content=ft.Row(
                controls=[
                    # ft.Tooltip(
                    #     content=ft.Text(value="batch")
                    # ),
                    ft.Text(value="batch"),
                    ft.TextField(value=self.batch_size,on_change=self.on_change_batch_size)
                ]
            ),
            alignment=ft.alignment.top_center
        )
        self.epoch_input = ft.Container(
            content=ft.Row(
                controls=[
                    # ft.Tooltip(
                    #     content=ft.Text(value="epoch"),
                    # ),
                    ft.Text(value="epoch"),
                    ft.TextField(value=self.epoch,on_change=self.on_change_epoch)
                ]
            ),
            alignment=ft.alignment.top_center
        )

        self.graph_image = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=self.metrics,
                        width=int(self.page.width*(50/126)),
                        height=int(self.page.height*(30/68)),
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Image(
                        src=self.loss,
                        width=int(self.page.width*(50/126)),
                        height=int(self.page.height*(30/68)),
                        fit=ft.ImageFit.CONTAIN
                    ),
                ]
            ),
            top=0,
            left=500,
            expand=True
        )
        print(self.page.width,self.page.height)
        self.pb_text = ft.Text(value="epoch:  "+"0"+"/"+str(self.epoch),top=480,left=50)
        self.pb = ft.ProgressBar(width=400,top=500,left=0,value=0)
        
        self.content = ft.Stack(
            [
                ft.Container(
                    content=ft.Column(
                        controls=[self.batch_input,
                                  self.epoch_input]
                    ),
                    top=0,
                    left=0
                ),
                self.graph_image,
                self.pb_text,
                self.pb,
                ft.ElevatedButton(text="train",on_click=self.on_click_train, right=0, bottom=0),
            ],
            expand=True,
        )
        self.task = None



    def on_change_batch_size(self, e):
        self.batch_size = int(e.control.value)
        print("batch_size",self.batch_size,type(self.batch_size))

    def on_change_epoch(self, e):
        self.epoch = int(e.control.value)
        self.pb_text.value = "epoch:  "+"0"+"/"+str(self.epoch)
        self.page.update()
        print("epoch",self.epoch,type(self.epoch))

    def on_click_train(self, e):
        shutil.rmtree(self.project_path+"/Result/")
        os.makedirs(name=self.project_path+"/Result",exist_ok=True)
        shutil.copy("packages/image/metrics_0epoch.png", self.project_path+"/Result")
        shutil.copy("packages/image/loss_0epoch.png" ,self.project_path+"/Result")

        copy_to_userproject.CopyTrain(self.project_path+"/Scripts")
        GenerateBatfile.generate(target_path=self.project_path+"/Scripts",
                                 run_path=read_activate_path.read_activ_path(),
                                 part_dict=self.page.client_storage.get("part_dict"),
                                 data_type=self.page.client_storage.get("data_type"),
                                 epochs=self.epoch,
                                 batchs=self.batch_size,
                                 project_path=self.project_path+"/Result")
        GenerateBatfile.Runbat(self.project_path+"/Scripts"+"/run.bat")
        e.control.disabled = True
        self.page.update()
        self.task = asyncio.run(self.async_get_picture())
        pass

    async def async_get_picture(self):
        while True:
            result_file=glob.glob(self.project_path+"/Result/*.*")
            re_loss = None
            re_metrics = None
            for file in result_file:
                if "loss" in file:
                    re_loss = file
                elif "metrics" in file:
                    re_metrics = file
            if re_loss != None and re_metrics != None:
                if self.metrics != re_metrics or self.loss != re_loss:
                    epoch = int(re_metrics.split("_")[-1].replace("epoch.png",""))
                    self.metrics = re_metrics
                    self.loss = re_loss
                    self.graph_image.content.controls[0].src=self.metrics
                    self.graph_image.content.controls[1].src=self.loss
                    self.graph_image.content.controls[0].width=int(self.page.width*(50/126))
                    self.graph_image.content.controls[0].height=int(self.page.height*(30/68))
                    self.graph_image.content.controls[1].width=int(self.page.width*(50/126))
                    self.graph_image.content.controls[1].height=int(self.page.height*(30/68))

                    self.pb_text.value = "epoch:  "+str(epoch)+"/"+str(self.epoch)
                    self.pb.value = epoch/self.epoch
                    self.page.update()

            await asyncio.sleep(0.5)
