from components._common.appheader import AppHeader

from packages.DS import DS
from packages.open_html import view_DS

import flet as ft
import os
import pandas as pd

class DSHome(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_DSHome"

        self.ds = None

        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        # self.page.overlay.extend([self.pick_files_dialog])

        self.controls = [
            AppHeader(page=self.page, title="DS InterFace", bgcolor=ft.colors.AMBER),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text(value="ファイルをアップロード",size=50),
                            height=200,
                            alignment=ft.alignment.center
                        ),
                        ft.Container(
                            content=ft.IconButton(icon=ft.icons.FILE_OPEN, icon_size=200, on_click=self.pick_files, height=300, width=300),
                            alignment=ft.alignment.center,
                        ),
                    ]
                ),
                padding=ft.padding.only(top=10,left=10,right=10,bottom=50)
            )
        ]

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
        path = file.path
        print(path)
        df = pd.read_csv(path)
        export_path = "projet_ds/"+path.split("\\")[-1][:-4]+"/Result"
        os.makedirs(name="projet_ds/"+path.split("\\")[-1][:-4], exist_ok=True)
        os.makedirs(name=export_path, exist_ok=True)
        self.ds = DS()
        self.ds.send(df, export_dir_result=export_path)
        view_DS(export_path+"/DS_result/AutoViz/")


    def on_click_new_file(self, e):
        # self.page.go("/Page_DSNewFile")
        pass