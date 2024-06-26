import flet as ft

class MainMenu(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MainMenu"
        self.controls = [
            ft.ElevatedButton(text="ML",on_click=self.on_click_ML),
            ft.ElevatedButton(text="DA",on_click=self.on_click_DA)
        ]

    def on_click_ML(self,e):
        self.page.go("/Page_MLHome")
    
    def on_click_DA(self,e):
        self.page.go("/Page_DAHome")