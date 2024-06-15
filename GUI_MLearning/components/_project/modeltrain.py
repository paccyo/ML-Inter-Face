# from packages import RunTrain
from packages import copy_trainpy
from packages import GenerateBatfile

import flet as ft
import flet.canvas as cv
import glob

class ModelTrain(ft.Tab):
    def __init__(self, page:ft.Page, text: str | None = None, content: ft.Control | None = None, tab_content: ft.Control | None = None, icon: str | None = None, ref: ft.Ref | None = None, visible: bool | None = None, adaptive: bool | None = None):
        super().__init__(text, content, tab_content, icon, ref, visible, adaptive)
        self.page = page
        self.text = "学習"
        self.icon=ft.icons.ADJUST
        self.info_files = glob.glob(self.page.client_storage.get("project_path")+"/Scripts/*")
        print(self.info_files)
        self.batch_size = 2
        self.epoch = 1000
        batch = ft.Container(
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
        epoch = ft.Container(
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

        self.content = ft.Stack(
            [
                ft.Container(
                    content=ft.Column(
                        controls=[batch,
                                  epoch]
                    ),
                    top=0,
                    left=0
                ),
                ft.ElevatedButton(text="train",on_click=self.on_click_train, right=0, bottom=0),
            ],
            expand=True,
        )


    def on_change_batch_size(self, e):
        self.batch_size = int(e.control.value)
        print("batch_size",self.batch_size,type(self.batch_size))

    def on_change_epoch(self, e):
        self.epoch = int(e.control.value)
        print("epoch",self.epoch,type(self.epoch))

    def on_click_train(self, e):
        # RunTrain.run(part_dict=self.page.client_storage.get("part_dict"),
        #              data_type=self.page.client_storage.get("data_type"),
        #              epochs=self.epoch,
        #              batchs=self.batch_size,
        #              project_path=self.page.client_storage.get("project_path")+"/Result")
        copy_trainpy.CopyTrain(self.page.client_storage.get("project_path")+"/Scripts")
        GenerateBatfile.generate(target_path=self.page.client_storage.get("project_path")+"/Scripts",
                                 run_path=r"C:\Users\Yuuki\Documents\GUI_MLearning\Scripts\activate.bat",
                                 part_dict=self.page.client_storage.get("part_dict"),
                                 data_type=self.page.client_storage.get("data_type"),
                                 epochs=self.epoch,
                                 batchs=self.batch_size,
                                 project_path=self.page.client_storage.get("project_path")+"/Result")
        GenerateBatfile.Runbat(self.page.client_storage.get("project_path")+"/Scripts"+"/run.bat")
        e.control.disabled = True
        self.page.update()
        pass