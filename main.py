from components.ML.page_ml_home import MLHome
from components.ML.page_ml_createproject import MLCreateProject
# from components.ML.page_ml_project import MLProject


from components.ML.test_.page_ml_project import MLProject


from components.DS.page_ds_home import DSHome
# from components.DS.page_ds_project import DSProject
# from components.DS.page_ds_createproject import DSNewFile

from components.page_mainmenu import MainMenu
from components.page_signin import SignIn
from components.page_signup import SignUp

import flet as ft


def main(page: ft.Page):
    # Define the UI components
    page.title = "Neural Network Designer"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = "light"

    def route_change(handler):
        t_route = ft.TemplateRoute(handler.route)
        print(t_route.route)
        if t_route.match("/Page_SignIn"):
            page.views.clear()
            page.views.append(SignIn(page))
        elif t_route.match("/Page_SignUp"):
            page.views.append(SignUp(page))
        elif t_route.match("/Page_MainMenu"):
            page.views.clear()
            page.views.append(MainMenu(page))
        elif t_route.match("/Page_DSHome"):
            page.views.append(DSHome(page))
        elif t_route.match("/Page_MLHome"):
            page.views.append(MLHome(page))
        elif t_route.match("/Page_MLProject"):
            page.views.clear()
            page.views.append(MLProject(page))
        elif t_route.match("/Page_MLCreateProject"):
            page.views.append(MLCreateProject(page))
        elif t_route.match("/Page_DSProject"):
            pass
        elif t_route.match("/Page_DSNewFile"):
            pass
            
        page.update()

    def view_pop(handler):
        page.views.pop()  # 1つ前に戻る
        page.go("/back")

    # 戻る時のロジック設定
    page.on_view_pop = view_pop

    # ルート変更時のロジック設定
    page.on_route_change = route_change

    page.go("/Page_SignIn")
    # page.go("/Page_DSHome")
    # page.go("/Page_MainMenu")
    # page.go("/Page_MLHome")
    # page.go("/Page_MLProject")

# Start the app
ft.app(target=main, port=8550)
# ft.app(target=main, port=8550, view=ft.WEB_BROWSER)