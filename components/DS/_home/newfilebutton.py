import flet as ft

class NewFileButtons(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page=page

        self.file_button = ft.IconButton(
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
            icon=ft.icons.FILE_OPEN_OUTLINED,
            icon_size=100,
            width=100,
            height=100,
            on_click=self.on_click_new_file,
        )


        self.content=ft.Row(
            controls=[

            ]
        )
        self.alignment=ft.alignment.bottom_left
        self.padding=ft.padding.only(left=50,right=50)

ft.IconButton(
                            
                            )