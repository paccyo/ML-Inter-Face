import flet as ft
import flet.canvas as cv

class Option(ft.Tab):
    def __init__(self, page:ft.Page, text: str | None = None, content: ft.Control | None = None, tab_content: ft.Control | None = None, icon: str | None = None, ref: ft.Ref | None = None, visible: bool | None = None, adaptive: bool | None = None):
        super().__init__(text, content, tab_content, icon, ref, visible, adaptive)
        self.page = page
        self.text = "オプション"
        self.icon=ft.icons.SETTINGS
        self.content=ft.Text("This is Tab 3")