from components._userapp.userappheader import UserAppHeader

import flet as ft


class UserApp(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_UserApp"
        
        self.username = ""
        self.password = ""

        self.userapp = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(value="User Login",size=20),
                    height=50,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER
                ),
                ft.Container(
                    content=ft.TextField(label="user name", border=ft.InputBorder.UNDERLINE, hint_text="enter username" ,width=300, on_change=self.on_change_usename),
                    height=70,
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=ft.TextField(label="password", border=ft.InputBorder.UNDERLINE, hint_text="enter password" ,width=300, on_change=self.on_change_password),
                    height=70,
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=ft.TextButton(text="sign app",
                                          on_click=self.on_click_sign_app),
                    height=90,
                    alignment=ft.Alignment(0.8, 1),
                ),
                ft.Container(
                    content=ft.CupertinoFilledButton(
                        content=ft.Text("Sign in"),
                        opacity_on_click=0.3,
                        # on_click=lambda e: print("CupertinoFilledButton clicked!"),
                        on_click=self.on_click_sign_in,
                    ),
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=ft.Container(
                        content=ft.Row(
                            controls=[
                            ft.Text(value="  Google",color=ft.colors.BLACK),
                            ft.Container(content=ft.Image(src="packages\image\google_image.png",fit=ft.ImageFit.CONTAIN),width=30,height=30,border_radius=30)
                            ],
                        ),
                        width=100,
                        height=50,
                        bgcolor=ft.colors.WHITE,
                        border=ft.border.all(1, ft.colors.BLACK),
                        on_click=lambda e: print("Google Aouth clicked!"),
                    ),
                    height=90,
                    alignment=ft.alignment.center,
                )
            ]
        )

        self.controls = [
            UserAppHeader(self.page),
            ft.Container(
                content=ft.Container(
                    content=self.userapp,
                    border=ft.border.all(1, ft.colors.BLACK),
                    alignment=ft.Alignment(0,-1),
                    width=350,
                    height=475
                ),
                alignment=ft.Alignment(0,0),
                expand=True
            )
        ]

    def on_change_usename(self, e):
        self.username = e.control.value

    def on_change_password(self, e):
        self.password = e.control.value
        e.control.value = "*"*len(self.password)
        e.control.update()

    def on_click_sign_in(self, e):
        self.page.go("/Page_Home")

    def on_click_sign_app(self, e):
        self.page.go("/Page_SignApp")

