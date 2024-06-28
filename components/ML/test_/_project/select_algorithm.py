import flet as ft 

class SelectAlgorithm(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.bgcolor = ft.colors.BLUE