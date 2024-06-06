from components.home.homeheader import AppHeader

import flet as ft

class Home(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Home"
        self.controls = [
            AppHeader(page),
        ]