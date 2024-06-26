from components.ML.page_ml_home import MLHome
from components.ML.page_ml_project import MLProject
from components.ML.page_ml_createproject import MLCreateProject
# from components.DA.page_da_home import DAHome
# from components.DA.page_da_project import DAProject
# from components.DA.page_da_createproject import DACreateProject
from components.page_mainmenu import MainMenu
from components.page_userapp import UserApp
from components.page_signapp import SignApp

import flet as ft


def main(page: ft.Page):
    # Define the UI components
    page.title = "Neural Network Designer"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = "light"

    def route_change(handler):
        t_route = ft.TemplateRoute(handler.route)
        
        if t_route.match("/Page_UserApp"):
            page.views.clear()
            page.views.append(UserApp(page))
        elif t_route.match("/Page_SignApp"):
            page.views.append(SignApp(page))
        elif t_route.match("/Page_MainMenu"):
            page.views.clear()
            page.views.append(MainMenu(page))
        elif t_route.match("/Page_DAHome"):
            pass       
        elif t_route.match("/Page_MLHome"):
            page.views.clear()
            page.views.append(MLHome(page))
        elif t_route.match("/Page_MLProject"):
            page.views.clear()
            page.views.append(MLProject(page))
        elif t_route.match("/Page_MLCreateProject"):
            page.views.append(MLCreateProject(page))
        elif t_route.match("/Page_DAProject"):
            pass
        elif t_route.match("/Page_DACreateProject"):
            pass
            
        page.update()

    def view_pop(handler):
        page.views.pop()  # 1つ前に戻る
        page.go("/back")

    # 戻る時のロジック設定
    page.on_view_pop = view_pop

    # ルート変更時のロジック設定
    page.on_route_change = route_change

    page.go("/Page_UserApp")
    # page.go("/Page_Home")

# Start the app
ft.app(target=main, port=8550)
# ft.app(target=main, port=8550, view=ft.WEB_BROWSER)