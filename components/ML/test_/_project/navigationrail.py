import flet as ft

class ProjectNavigationRail(ft.NavigationRail):
    def __init__(self, page:ft.Page, on_change=None, ref: ft.Ref | None = None):
        super().__init__()
        self.page = page
        self.on_change = on_change