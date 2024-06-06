from typing import List
import flet as ft

class Header(ft.AppBar):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page


class AppHeader(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.toggle_dark_light_icon = ft.IconButton(
            icon="light_mode",
            selected_icon = "dark_mode",
            tooltip=f"switch light and dark mode",
            on_click=self.toggle_icon,
        )
        
        something_btn = ft.ElevatedButton(text="Button")
        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(), # divider
            ft.PopupMenuItem(text="Settings"),
        ]
        # Appのpage.appbarフィールドの設定
        self.page.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.TRIP_ORIGIN_ROUNDED),
            leading_width=100,
            title=ft.Text(value="Example", size=32, text_align="center"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.Container(
                    content=ft.Row(
                        [
                            self.toggle_dark_light_icon,
                            something_btn,
                            ft.PopupMenuButton(
                                items=self.appbar_items
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )

    def toggle_icon(self, e):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.update()
        self.toggle_dark_light_icon.selected = not self.toggle_dark_light_icon.selected
        self.page.update()