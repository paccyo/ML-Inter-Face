import flet as ft

class Header(ft.AppBar):
    def __init__():
        super().__init__()
        pass
    # def __init__(self, page:ft.Page):
    #     super().__init__()
    #     self.page = page


# class AppHeader(ft.AppBar):
#     def __init__(self, page: ft.Page, page_title: str="Example"):
#         super().__init__()
#         self.page = page
#         self.page_title = page_title
#         self.toggle_dark_light_icon = ft.IconButton(
#             icon="light_mode",
#             selected_icon = "dark_mode",
#             tooltip=f"switch light and dark mode",
#             on_click=self.toggle_icon,
#         )
#         self.appbar_items = [
#             ft.PopupMenuItem(text="Login"),
#             ft.PopupMenuItem(),
#             ft.PopupMenuItem(text="SignUp"),
#             ft.PopupMenuItem(),
#             ft.PopupMenuItem(text="Settings"),
#         ]
#         # Appのpage.appbarフィールドの設定
#         self.page.appbar = ft.AppBar(
#             leading=ft.Icon(ft.icons.TRIP_ORIGIN_ROUNDED),
#             leading_width=100,
#             title=ft.Text(value=self.page_title, size=32, text_align="center"),
#             center_title=False,
#             toolbar_height=75,
#             bgcolor=ft.colors.SURFACE_VARIANT,
#             actions=[
#                 ft.Container(
#                     content=ft.Row(
#                         [
#                             self.toggle_dark_light_icon,
#                             ft.ElevatedButton(text="SOMETHING"),
#                             ft.PopupMenuButton(
#                                 items=self.appbar_items
#                             ),
#                         ],
#                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                     ),
#                     margin=ft.margin.only(left=50, right=25)
#                 )
#             ],
#         )

#     def toggle_icon(self, e):
#         self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
#         self.toggle_dark_light_icon.selected = not self.toggle_dark_light_icon.selected
#         self.page.update()


class AppHeader(ft.AppBar):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.leading=ft.Icon(ft.icons.TRIP_ORIGIN_ROUNDED)
        self.leading_width=100
        self.title=ft.Text(value="プロジェクト", size=32, text_align="center")
        self.center_title=False
        self.toolbar_height=75
        self.bgcolor=ft.colors.SURFACE_VARIANT,
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