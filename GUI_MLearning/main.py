from components.page_home import Home
from components.page_project import Project
from components.page_createproject import CreateProject

import flet as ft


def main(page: ft.Page):
    # Define the UI components
    page.title = "Neural Network Designer"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = "dark"

    def route_change(handler):
        t_route = ft.TemplateRoute(handler.route)
        
        if t_route.match("/Page_Home"):
            page.views.clear()
            page.views.append(Home(page))
        elif t_route.match("/Page_Project"):
            page.views.clear()
            page.views.append(Project(page))
        elif t_route.match("/Page_CreateProject"):
            page.views.append(CreateProject(page))
        page.update()

    def view_pop(handler):
        page.views.pop()  # 1つ前に戻る
        page.go("/back")
        # page.update()
        # update() だと route が変更されない。
        # そうなると1つ戻ってまた進むことができなくなるので go("/back") で回避。不具合？

    # 戻る時のロジック設定
    page.on_view_pop = view_pop

    # ルート変更時のロジック設定
    page.on_route_change = route_change

    # page.go("/Page_Project")
    page.go("/Page_Home")

# Start the app
ft.app(target=main)
# ft.app(target=main, port=8550, view=ft.WEB_BROWSER)