from packages.DatasetCHK import CHK
from packages.GenerateDataset import DatasetInfo

import flet as ft


class DataSelect(ft.Tab):
    def __init__(self, page:ft.Page, text: str | None = None, content: ft.Control | None = None, tab_content: ft.Control | None = None, icon: str | None = None, ref: ft.Ref | None = None, visible: bool | None = None, adaptive: bool | None = None):
        super().__init__(text, content, tab_content, icon, ref, visible, adaptive)
        self.page = page
        self.icon=ft.icons.DATA_USAGE

        self.get_directory_dialog = ft.FilePicker(on_result=self.get_directory_result)
        self.directory_path = ft.Text()
        page.overlay.extend([self.get_directory_dialog])
        self.learning_way = "categorical"
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
                            value = self.learning_way,
                            on_change=self.on_change_learning_way,
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

        self.success_failed_image = ft.Image(src="packages/image/failed.png",)

        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    self.folder_pickup,
                    ft.Divider(),
                    self.success_failed_image
                ]
            )
        )

    def get_directory_result(self, e: ft.FilePickerResultEvent):
        # # print(e)
        self.directory_path.value = e.path if e.path else None
        self.directory_path.update()


    def folder_submit(self,e):
        path = self.directory_path.value
        # print(self.page.client_storage.get("project_path"))
        if path:
            judge, data_path = CHK(path=path, data_type=self.data_type, learning_way=self.learning_way)
            # print(judge)
            if judge:
                test_dict = {'train':6, 'validation':4, 'test':0}
                dataset_info = DatasetInfo()
                dataset_info.send(test_dict, path, self.page.client_storage.get("project_path")+"/Data")
                self.page.client_storage.set("part_dict",test_dict)
                self.page.client_storage.set("dataset_path", path)
                self.page.client_storage.set("data_type",self.data_type)
                self.success_failed_image.src = "packages/image/success.png"
                with open(self.page.client_storage.get('project_path')+"/dataset_path.txt", 'w', encoding='utf-8') as file:
                    file.write(path+"\n"+self.data_type)
            else:
                self.success_failed_image.src = "packages/image/failed.png"
            self.page.update()

            print(judge)

    def on_change_data_type(self,e):
        self.data_type = e.control.value
        self.page.client_storage.set("data_type", self.data_type)

    def on_change_learning_way(self, e):
        self.learning_way =  e.control.value
 
