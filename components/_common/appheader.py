import flet as ft


class AppHeader(ft.AppBar):
    def __init__(self, page:ft.Page, title="MLInterFace", bgcolor=ft.colors.CYAN, toolbar_height=75):
        super().__init__()
        self.page = page

        self.title=ft.Text(value=title, size=(toolbar_height//2), text_align="center")
        self.center_title=False
        self.toolbar_height=toolbar_height
        self.bgcolor=bgcolor

        self.toggle_dark_light_icon = ft.IconButton(
            icon="light_mode",
            selected_icon = "dark_mode",
            tooltip=f"switch light and dark mode",
            on_click=self.toggle_icon,
        )
        
        self.menubutton = ft.IconButton(
            icon=ft.icons.MENU
        )


        self.actions=[
            ft.Container(
                content=ft.Row(
                    [
                        self.toggle_dark_light_icon,
                        self.menubutton
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                margin=ft.margin.only(left=50, right=25)
            )
        ]

    def toggle_icon(self, e):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.toggle_dark_light_icon.selected = not self.toggle_dark_light_icon.selected
        self.page.update()