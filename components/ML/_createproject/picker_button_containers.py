from packages import DatasetCHK

import flet as ft
    



class Pick_file_Container(ft.Container):
    def __init__(self, page:ft.Page, learning_way):
        super().__init__()
        self.page = page

        self.get_directory_dialog = ft.FilePicker(on_result=self.get_directory_result)
        self.data = None
        self.page.overlay.extend([self.get_directory_dialog])
        self.height = 250
        self.learning_way = learning_way
        self.expand = True
        self.button = ft.ElevatedButton(
            text = "Open file",
            icon=ft.icons.FOLDER_OPEN,
            on_click=lambda _: self.get_directory_dialog.pick_files(file_type=ft.FilePickerFileType.CUSTOM,allowed_extensions=["csv"],allow_multiple=True),
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
            width=500,
            height=50,
        )

        self.content = ft.Column(
            controls=[
                self.button,
            ],
            scroll=ft.ScrollMode.HIDDEN
        )


    def get_directory_result(self, e: ft.FilePickerResultEvent):
        self.content.controls = self.content.controls[:1]
        for file in e.files:
            self.content.controls.append(ft.Text(value=file.path if file.path else None))
            check = DatasetCHK.CHK(path=file.path, data_type='dataframe', learning_way=self.learning_way)
            print(file.path)
            print(check)
            if check[0]:
                self.bgcolor = None
            else:
                self.bgcolor = ft.colors.RED
        self.data = [file.path for file in e.files]
        self.update()






class Pick_folder_Container(ft.Container):
    def __init__(self, page:ft.Page, learning_way):
        super().__init__()
        self.page = page

        self.get_directory_dialog = ft.FilePicker(on_result=self.get_directory_result)
        self.data = None
        self.page.overlay.extend([self.get_directory_dialog])
        self.height = 250
        self.expand = True
        self.learning_way = learning_way
        self.button = ft.ElevatedButton(
            text = "Open directory",
            icon=ft.icons.FOLDER_OPEN,
            on_click=lambda _: self.get_directory_dialog.get_directory_path(),
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
            width=300,
            height=50,
        )


        self.content = ft.Column(
            controls=[
                self.button,
            ]
        )
    
    def get_directory_result(self, e: ft.FilePickerResultEvent):
        self.content.controls = self.content.controls[:1]
        self.content.controls.append(ft.Text(value=e.path if e.path else None))
        self.data = e.path
        check = DatasetCHK.CHK(path=self.data, data_type="image", learning_way=self.learning_way)
        print(check,e.path)
        if check[0]:
            self.bgcolor = None
        else:
            self.bgcolor = ft.colors.RED

        self.update()
