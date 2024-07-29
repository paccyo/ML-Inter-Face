from packages.NNR import ReModel
from packages.NNR import Research

import flet as ft
import asyncio
import time
import glob

class ResearchModel(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page

        self.expand = True

        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)

        self.buttons = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(text="researchmodel",on_click=self.on_click_researchmodel),
                    ft.ElevatedButton(text="remodel",on_click=self.pick_files),
                ],
            ),
        width=200,
        )

        self.image_content = ft.Container(
            content=ft.Column(
                controls=[],
                expand=True,
                scroll=ft.ScrollMode.ALWAYS,
            ),
            expand=True
        )

        self.content = ft.Container(
            content=ft.Row(
                controls=[
                    self.buttons,
                    self.image_content,
                ],
                expand=True,
            ),
            expand=True
        )

    async def update_image(self):
        running = True
        t1 = None
        while running:
            await asyncio.sleep(0.2)
            self.image_content.content.controls = []
            result_files = glob.glob(self.project_path+"/Result/weights*.png")
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
                # self.image_content.content.scroll = ft.ScrollMode.ALWAYS
                self.image_content.update()
                
                if time.time()-t1 > 30:
                    self.image_content.content.scroll = ft.ScrollMode.ALWAYS
                    self.image_content.update()
                    running = False
                    

    def on_click_researchmodel(self,e):
        
        self.project_path = self.page.client_storage.get("project_file_path")
        
        Research(self.project_path+"/Result")
        
        self.remodel = ReModel(self.project_path+"/Result/trained_model.h5")

        self.page.run_task(self.update_image)


    def on_click_remodel(self,path):
        self.remodel.csv_to_model(csv_file_path=path, export_path=self.project_path+"/Result")

    # happens when example is added to the page (when user chooses the FilePicker control from the grid)
    def did_mount(self):
        self.page.overlay.append(self.pick_files_dialog)
        self.page.update()

    # happens when example is removed from the page (when user chooses different control group on the navigation rail)
    def will_unmount(self):
        self.page.overlay.remove(self.pick_files_dialog)
        self.page.update()

    async def pick_files(self,_):
        await self.pick_files_dialog.pick_files_async(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["csv"], allow_multiple=True)

    
    async def pick_files_result(self, e: ft.FilePickerResultEvent):
        print(e,e.files)
        file = e.files[0]
        self.on_click_remodel(file.path)
