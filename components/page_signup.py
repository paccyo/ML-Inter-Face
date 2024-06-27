from components._common.appheader import AppHeader

import flet as ft
import glob

class SignUp(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_SignUp"

        self.username = ""
        self.password = ""
        self.re_password = ""

        self.accounts = [s.split("\\")[-1][:-7] for s in glob.glob('accounts/*.paccyo')]        

        self.input_username = ft.TextField(label="user name", border=ft.InputBorder.UNDERLINE, hint_text="enter username" ,width=300, on_change=self.on_change_username)
        self.input_password = ft.TextField(label="password", border=ft.InputBorder.UNDERLINE, hint_text="enter password" ,width=300, on_change=self.on_change_password)
        self.re_input_password = ft.TextField(label="Re-enter password", border=ft.InputBorder.UNDERLINE, hint_text="Re-enter password" ,width=300, on_change=self.on_change_repassword)
        self.error_username = ft.Text(value="",size=10,color=ft.colors.RED)
        self.error_password = ft.Text(value="",size=10,color=ft.colors.RED)
        self.error_re_password = ft.Text(value="",size=10,color=ft.colors.RED)

        self.user_app = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(value="Sign App",size=20),
                    height=50,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER
                ),
                ft.Container(
                    content=self.input_username,
                    height=70,
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=self.error_username,
                    height=15,
                    alignment=ft.alignment.top_right,
                    padding=ft.padding.only(right=30)
                ),
                ft.Container(
                    content=self.input_password,
                    height=50,
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=self.error_password,
                    height=15,
                    alignment=ft.alignment.top_right,
                    padding=ft.padding.only(right=30)
                ),
                ft.Container(
                    content=self.re_input_password,
                    height=50,
                    alignment=ft.alignment.top_center,
                ),
                ft.Container(
                    content=self.error_re_password,
                    height=15,
                    alignment=ft.alignment.top_right,
                    padding=ft.padding.only(right=30)
                ),
                ft.Container(
                    content=ft.CupertinoFilledButton(
                        content=ft.Text("Sign in"),
                        opacity_on_click=0.3,
                        on_click=self.on_click_sign_up,
                    ),
                    alignment=ft.alignment.bottom_center,
                ),
            ],
        )

        self.controls = [
            AppHeader(self.page),
            ft.Container(
                content=ft.Container(
                    content=self.user_app,
                    border=ft.border.all(1, ft.colors.BLACK),
                    alignment=ft.Alignment(0,-1),
                    width=350,
                    height=475
                ),
                alignment=ft.Alignment(0,0),
                expand=True
            )
        ]

    def on_change_username(self, e):
        self.username = e.control.value
        if self.username in self.accounts:
            self.error_username.value = "既に使用されているアカウント名です"
            self.error_username.update()
        else:
            self.error_username.value = ""
            self.error_username.update()
            pass

    def on_change_password(self, e):
        if len(self.password) < len(e.control.value):
            self.password = self.password+e.control.value[-1]
        elif len(e.control.value) < len(self.password):
            self.password = self.password[:-1]
        e.control.value = "*"*len(self.password)
        e.control.update()


    def on_change_repassword(self, e):
        if len(self.re_password) < len(e.control.value):
            self.re_password = self.re_password+e.control.value[-1]
        elif len(e.control.value) < len(self.re_password):
            self.re_password = self.re_password[:-1]
        e.control.value = "*"*len(self.re_password)
        e.control.update()

        if self.re_password == self.password:
            self.error_password.value = ""
            self.error_password.update()
            self.error_re_password.value = ""
            self.error_re_password.update()
        elif self.password == "":
            self.error_password.value = "パスワードが入力されていません"
            self.error_password.update()
        else:            
            self.error_password.value = ""
            self.error_password.update()
            self.error_re_password.value = "入力したパスワードと違います"
            self.error_re_password.update()


    def on_click_sign_up(self, e):
        print(self.accounts)
        if self.username not in self.accounts:
            with open("accounts/"+self.username+".paccyo","w",encoding="utf-8") as f:
                f.write(self.password)
            self.page.go("/Page_SignIn")
        else:
            self.error_username.value = "既に登録されているアカウントです"
            self.error_password.value = ""
            self.error_username.update()
            self.error_password.update()