from packages.NNR import ReModel
from packages.NNR import Research

import flet as ft

class ResearchModel(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page

        self.expand = True

        self.content = ft.Column(
            controls=[
                ft.ElevatedButton(text="researchmodel",on_click=self.on_click_researchmodel),
                ft.ElevatedButton(text="remodel",on_click=self.pick_files_result),
            ]
        )
    
    def on_click_researchmodel(self,e):
        
        self.project_path = self.page.client_storage.get("project_file_path")
        
        Research(self.project_path+"/Result")
        
        self.remodel = ReModel(self.project_path+"/Result/trained_model.h5")


    def on_click_remodel(self,path):
        self.remodel.csv_to_model(csv_file_path=path,export_path=self.project_path+"/Result")

    # happens when example is added to the page (when user chooses the FilePicker control from the grid)
    def did_mount(self):
        self.page.overlay.append(self.pick_files_dialog)
        self.page.update()

    # happens when example is removed from the page (when user chooses different control group on the navigation rail)
    def will_unmount(self):
        self.page.overlay.remove(self.pick_files_dialog)
        self.page.update()

    async def pick_files(self,_):
        await self.pick_files_dialog.pick_files_async(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["csv"], allow_multiple=False)

    
    async def pick_files_result(self, e: ft.FilePickerResultEvent):
        file = e.files[0]
        self.on_click_remodel(file.path)
