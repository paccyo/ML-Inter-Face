from components._common.appheader import AppHeader
import flet as ft

class MainMenu(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MainMenu"
        self.controls = [
            AppHeader(self.page,title="ML/DS InterFace",bgcolor=ft.colors.LIME),
            ft.ElevatedButton(text="ML",on_click=self.on_click_ML),
            ft.ElevatedButton(text="DS",on_click=self.on_click_DS)
        ]
    
    def on_click_ML(self,e):
        self.page.go("/Page_MLHome")
    
    def on_click_DS(self,e):
        self.page.go("/Page_DSHome")