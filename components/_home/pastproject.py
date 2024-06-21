import flet as ft
import glob
import os

class PastProject(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page

        self.top=self.page.height//5
        self.left=self.page.width//7
        self.height=(self.page.height//5)*3
        self.width=(self.page.width//7)*5


        self.pastproject_list = glob.glob('projects/*')

        past_project = []
        for project in self.pastproject_list:
            rect = []

            
            rect = ft.ElevatedButton(
                content=ft.Column(
                    controls=[
                        ft.Text(value=project.split("\\")[-1], size=20),
                        ft.Text(value="path : "+project, size=10)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    # horizontal_alignment=ft.MainAxisAlignment.START,
                    spacing=5,
                ),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=0),
                ),
                on_click=self.on_click_past_project,
                width = self.width,
            )
            rect.data=project

            if rect != []:
                past_project.append(rect)
            
        
        # print(self.pastproject_list)
        self.past_project = ft.Container(
            content=ft.Column(
                controls=past_project,
                scroll=ft.ScrollMode.HIDDEN,
            ),
            height = self.height-50
        )
        
        
        self.content = ft.Column(
            controls=[
                ft.TextField(value="",hint_text="過去のプロジェクトを検索", on_change=self.filter_project),
                self.past_project
            ],
        )
    
    def on_click_past_project(self, e):
        path = os.path.abspath(e.control.data)
        # print(path)
        self.page.client_storage.set("project_path",path)
        # print(self.page.client_storage.get("project_path"))
        self.page.go("/Page_Project")
        pass


    def filter_project(self, e):
        pass

