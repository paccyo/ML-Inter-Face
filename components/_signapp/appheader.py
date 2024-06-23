import flet as ft

class SignAppHeader(ft.AppBar):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        # self.leading=ft.Icon(ft.icons.TRIP_ORIGIN_ROUNDED)
        # self.leading_width=100
        self.title=ft.Text(value="MLInterFace", size=32, text_align="left")
        self.center_title=False
        self.toolbar_height=50
        # self.bgcolor=ft.colors.SURFACE_VARIANT,
        self.bgcolor=ft.colors.CYAN
        self.toggle_dark_light_icon = ft.IconButton(
            icon="light_mode",
            selected_icon = "dark_mode",
            tooltip=f"switch light and dark mode",
            on_click=self.toggle_icon,
        )
        self.actions=[
            ft.Container(
                content=ft.Row(
                    [
                        self.toggle_dark_light_icon,
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

