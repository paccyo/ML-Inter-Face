from components._userapp.userappheader import UserAppHeader

import os
import flet as ft
# from flet.auth.providers import GitHubOAuthProvider

# GITHUB_CLIENT_ID = os.getenv("Ov23liJzDjKYmusd0wGC")
# assert GITHUB_CLIENT_ID, "set GITHUB_CLIENT_ID environment variable"
# GITHUB_CLIENT_SECRET = os.getenv("f1b102d0777b6d58e2b95c2126b5947a019f610a")
# assert GITHUB_CLIENT_SECRET, "set GITHUB_CLIENT_SECRET environment variable"

class UserApp(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_UserApp"
        
        # self.provider = GitHubOAuthProvider(
        #     client_id=GITHUB_CLIENT_ID,
        #     client_secret=GITHUB_CLIENT_SECRET,
        #     redirect_url="http://localhost:8550/oauth_callback",
        # )


        self.userapp = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(value="User Login",size=20),
                    height=50,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER
                ),
                ft.Container(
                    content=ft.TextField(label="user name", border=ft.InputBorder.UNDERLINE, hint_text="enter username" ,width=300),
                    height=70,
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=ft.TextField(label="password", border=ft.InputBorder.UNDERLINE, hint_text="enter password" ,width=300),
                    height=70,
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=ft.TextButton(text="sign app"),
                    height=90,
                    alignment=ft.Alignment(0.8, 1)
                ),
                ft.Container(
                    content=ft.CupertinoFilledButton(
                        content=ft.Text("CupertinoFilled"),
                        opacity_on_click=0.3,
                        on_click=lambda e: print("CupertinoFilledButton clicked!"),
                    ),
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=ft.Container(
                        content=ft.Row(
                            controls=[
                            ft.Text(value="Google"),
                            ft.Container(content=ft.Image(src="packages\image\google_image.png",fit=ft.ImageFit.CONTAIN),width=30,height=30)
                            ],
                        ),
                        width=100,
                        height=50,
                        border=ft.border.all(1, ft.colors.BLACK),
                        on_click=lambda e: print("Google Aouth clicked!"),
                        # on_click=self.login_click
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

    # def login_click(self, e):
    #     self.page.login(self.provider)

    # def on_login(self, e):
    #     print("Login error:", e.error)
    #     print("Access token:", self.page.auth.token.access_token)
    #     print("User ID:", self.page.auth.user.id)
