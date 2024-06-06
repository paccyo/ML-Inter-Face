from components.home.homeheader import AppHeader

import flet as ft

class Home(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Home"
        self.controls = [
            AppHeader(page),
            ft.ElevatedButton(text="go_next",on_click=self.next)
        ]

    def next(self, e):
        self.page.go("/ProjectPage")

