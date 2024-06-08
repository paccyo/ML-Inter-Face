import flet as ft
import glob


class PastProject(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        
        self.pastproject_list = glob.glob('projects/*')

        print(self.pastproject_list)
        self.pastproject = ft.Container(
            content=ft.Column(
                controls=[],
            ),
            expand=True,
            bgcolor=ft.colors.AMBER
        )
        for project in self.pastproject_list:
            self.pastproject.content.controls.append(
                ft.ElevatedButton(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(value=project.split("\\")[-1], size=20),
                                ft.Text(value="path : "+project, size=10)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5,
                        )
                    ),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    width=500,
                    height=80
                )
            )        
        self.content = ft.Column(
            controls=[
                ft.TextField(value="test", on_change=self.filter_project),
                self.pastproject
            ],
            scroll=ft.ScrollMode.HIDDEN
        )



    def filter_project(self, e):
        pass

