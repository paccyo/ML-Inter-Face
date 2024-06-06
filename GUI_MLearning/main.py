# from components.page_home import Home
from components.page_project import Project

import flet as ft


def main(page: ft.Page):
    # Define the UI components
    page.title = "Neural Network Designer"
    page.vertical_alignment = ft.MainAxisAlignment.START


    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)
        if troute.match("/ProjectPage"):
            page.views.append(Project(page))
        # elif troute.match("/HomePage"):
        #     page.views.clear()
        #     page.views.append(Home(page))
        page.update()

    # ルート変更時のロジック設定
    page.on_route_change = route_change


    page.go("/ProjectPage")
    # page.go("/HomePage")

# Start the app
ft.app(target=main)
# ft.app(target=main, port=8550, view=ft.WEB_BROWSER)