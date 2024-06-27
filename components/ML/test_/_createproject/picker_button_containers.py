import flet as ft
    
    

class Pick_file_Container(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page

        self.get_directory_dialog = ft.FilePicker(on_result=self.get_directory_result)
        self.directory_path = ft.Text()
        self.page.overlay.extend([self.get_directory_dialog])

        self.button = ft.ElevatedButton(
            text = "Open file",
            icon=ft.icons.FOLDER_OPEN,
            on_click=lambda _: self.get_directory_dialog.pick_files(file_type=ft.FilePickerFileType.CUSTOM,allowed_extensions=["csv"]),
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
            width=300,
            height=50,
        )

        self.content = ft.Column(
            controls=[
                self.button,
                self.directory_path
            ]
        )

    def get_directory_result(self, e: ft.FilePickerResultEvent):
        self.directory_path.value = e.files[0].path if e.files[0].path else None
        self.directory_path.update()





class Pick_folder_Container(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page

        self.get_directory_dialog = ft.FilePicker(on_result=self.get_directory_result)
        self.directory_path = ft.Text()
        self.page.overlay.extend([self.get_directory_dialog])

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
                self.directory_path
            ]
        )
    
    def get_directory_result(self, e: ft.FilePickerResultEvent):
        self.directory_path.value = e.path if e.path else None
        self.directory_path.update()
