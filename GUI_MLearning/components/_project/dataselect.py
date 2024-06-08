from packages.DatasetCHK import CHK

import flet as ft


class DataSelect(ft.Tab):
    def __init__(self, page:ft.Page, text: str | None = None, content: ft.Control | None = None, tab_content: ft.Control | None = None, icon: str | None = None, ref: ft.Ref | None = None, visible: bool | None = None, adaptive: bool | None = None):
        super().__init__(text, content, tab_content, icon, ref, visible, adaptive)
        self.page = page
        self.icon=ft.icons.DATA_USAGE

        self.get_directory_dialog = ft.FilePicker(on_result=self.get_directory_result)
        self.directory_path = ft.Text()
        page.overlay.extend([self.get_directory_dialog])
        self.learningway = "categorical"
        self.data_type = "image"
        self.folder_pickup=ft.Container(
            content=ft.Row(
                controls=[
                    ft.Dropdown(
                            width=100,
                            height=50,
                            text_size=10,
                            scale=1,
                            value = self.data_type,
                            on_change=self.on_change_data_type,
                            options=[ft.dropdown.Option("image")]
                        ),
                    ft.Dropdown(
                            width=100,
                            height=50,
                            text_size=10,
                            scale=1,
                            value = self.learningway,
                            on_change=self.on_chenge_leraning_way,
                            options=[ft.dropdown.Option("categorical")],
                        ),
                    ft.ElevatedButton(
                        "Open directory",
                        icon=ft.icons.FOLDER_OPEN,
                        on_click=lambda _: self.get_directory_dialog.get_directory_path(),
                        disabled=page.web,
                    ),
                    self.directory_path,
                    ft.ElevatedButton(
                        "submit",
                        icon=ft.icons.FOLDER_OPEN,
                        on_click=self.folder_submit,
                        disabled=page.web
                    )
                ],
            ),
            alignment=ft.alignment.top_left
        )
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    self.folder_pickup,
                    ft.Divider()
                ]
            )
        )

    def get_directory_result(self, e: ft.FilePickerResultEvent):
        # print(e)
        self.directory_path.value = e.path if e.path else None
        self.directory_path.update()


    def folder_submit(self,e):
        path = self.directory_path.value
        if path:
            judge = CHK(path=path, data_type=self.data_type, learning_way=self.learningway)
            print(judge)

    def on_change_data_type(self,e):
        self.data_type = e.control.value

    def on_chenge_leraning_way(self, e):
        self.learningway =  e.control.value
 
