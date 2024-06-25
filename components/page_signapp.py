from components._signapp.signappheader import SignAppHeader
import flet as ft

class SignApp(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_SignApp"
        self.controls=[SignAppHeader(self.page)]