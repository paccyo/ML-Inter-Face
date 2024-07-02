import flet as ft 

class SelectAlgorithm(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        # self.bgcolor = ft.colors.BLUE
        self.select_algorithm = ""
        self.check_now_index = None

        self.select_algorithm_button = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(),
                                ft.VerticalDivider(),
                                ft.Text(value="TEST")
                            ]
                        ), 
                        on_click=self.on_click_algorithm, 
                        height=100, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                        data = {"check":False, "index":0}
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(),
                                ft.VerticalDivider(),
                                ft.Text(value="TESTGGGG")
                            ]
                        ), 
                        on_click=self.on_click_algorithm, 
                        height=100, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                        data = {"check":False, "index":1}
                    ),
                ]
            ),
            expand=True
        )


        self.content = ft.Column(
            controls=[
                ft.Container(content=ft.Text(value="アルゴリズムを選択",size=50), alignment=ft.alignment.center),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.Container(content=self.select_algorithm_button, expand=True, bgcolor=ft.colors.RED, padding=ft.padding.only(top=100,bottom=100,left=50,right=50),),
                        ft.Container(expand=True, bgcolor=ft.colors.BLUE)
                    ],
                    expand=True
                )
            ]
        )


    def on_click_algorithm(self, e):
        if self.check_now_index == None:
            self.check_now_index = e.control.data["index"]
        elif self.check_now_index != e.control.data["index"]:
            self.select_algorithm_button.content.controls[self.check_now_index].content.controls[0].name = None
            self.select_algorithm_button.content.controls[self.check_now_index].update()
            self.check_now_index = e.control.data["index"]
        elif self.check_now_index == e.control.data["index"]:
            self.check_now_index = None

        if e.control.content.controls[0].name == ft.icons.CHECK:
            e.control.content.controls[0].name = None
        else:
            e.control.content.controls[0].name = ft.icons.CHECK
        e.control.update()