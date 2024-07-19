import flet as ft
from components._common.appheader import AppHeader

class MainMenu(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_MainMenu"
        self.controls = [
            AppHeader(self.page, title="ML/DS InterFace", bgcolor=ft.colors.LIME),
            ft.Container(
                content=ft.Row(
                    controls=[
                        self.create_image_button("ML", "packages\image\ML_image.png", self.on_click_ML, ft.colors.LIGHT_BLUE),
                        self.create_image_button("DS", "packages\image\DS_image.png", self.on_click_DS, ft.colors.ORANGE),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]

    def create_image_button(self, text, img_src, on_click, text_color):
        container = ft.Container(
            content=ft.Stack(
                [
                    ft.Image(src=img_src, width=400, height=200),
                    ft.Container(
                        bgcolor=ft.colors.BLACK,
                        opacity=0.1,
                        width=400,
                        height=200,
                        border_radius=15,
                    ),
                    ft.Text(text, size=50, color=text_color, weight=ft.FontWeight.BOLD)
                ],
                alignment=ft.alignment.center,
            ),
            width=400,
            height=200,
            border_radius=20,
            on_click=on_click,
            data=text,  # ボタン名を 'data' に保存
            border=ft.border.all(width=2, color=ft.colors.TRANSPARENT)  # 初期状態では透明な枠線
        )

        container.on_hover = self.create_hover_event(container)
        return container

    def create_hover_event(self, container):
        def on_hover(e):
            if e.data == "true":
                container.border = ft.border.all(width=2, color=ft.colors.BLACK)  # ホバー時に枠線を表示
            else:
                container.border = ft.border.all(width=2, color=ft.colors.TRANSPARENT)  # ホバー解除時に枠線を非表示
            container.update()
        return on_hover

    def on_click_ML(self, e):
        self.page.go("/Page_MLHome")

    def on_click_DS(self, e):
        self.page.go("/Page_DSHome")

def main(page: ft.Page):
    page.title = "Image Button Example"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    main_menu = MainMenu(page)
    page.views.append(main_menu)

ft.app(target=main)