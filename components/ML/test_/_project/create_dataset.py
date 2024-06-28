import flet as ft

class CreateDatasetImage(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.content = ft.Tabs(
            tabs=[
                ft.Tab(text="データプレビュー",content=ft.Container(expand=True, bgcolor=ft.colors.AMBER)),
                ft.Tab(text="前処理",content=ft.Container(expand=True, bgcolor=ft.colors.AMBER_300)),
            ]
        )

class CreateDatasetDataFrame(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.content = ft.Tabs(
            tabs=[
                ft.Tab(text="データプレビュー",content=ft.Container(expand=True, bgcolor=ft.colors.AMBER)),
                ft.Tab(text="前処理",content=ft.Container(expand=True, bgcolor=ft.colors.AMBER_300)),
            ]
        )