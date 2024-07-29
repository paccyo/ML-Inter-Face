from packages.util.Calldict import ML_display_dicts

import flet as ft 

class SelectAlgorithm(ft.Container):
    def __init__(self,page:ft.Page, navigation_rail_update):
        super().__init__()
        self.page = page
        self.navigation_rail_update = navigation_rail_update
        self.expand = True 
        self.ML_dicts = ML_display_dicts
        self.learning_type = self.page.client_storage.get("project_info")["learning_type"]
        self.check_now_content = None

        self.select_algorithm_button = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(),
                                ft.VerticalDivider(),
                                ft.Text(value=ML_name),
                            ]
                        ), 
                        on_click=self.on_click_algorithm, 
                        height=100, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                        data = ML_dict
                    ) for ML_name, ML_dict in self.ML_dicts.items() if ML_dict[self.learning_type] == 'True'
                ],
                scroll=ft.ScrollMode.HIDDEN,
            ),
            expand=True
        )

        self.image_content = ft.Image(src="packages\image\logo.png",fit=ft.ImageFit.CONTAIN)


        self.content = ft.Column(
            controls=[
                ft.Container(content=ft.Text(value="アルゴリズムを選択",size=50), alignment=ft.alignment.center),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=self.select_algorithm_button, 
                            expand=True, 
                            bgcolor=ft.colors.BLUE_100, 
                            padding=ft.padding.only(top=70,bottom=70,left=50,right=50),
                        ),
                        ft.Container(
                            content=self.image_content,
                            expand=True,
                            # bgcolor=ft.colors.BLUE
                        )
                    ],
                    expand=True
                )
            ]
        )


    def on_click_algorithm(self, e):
        
        if self.check_now_content == None:
            self.check_now_content = e.control
            self.page.client_storage.set("alg",e.control.data["alg"])
        elif self.check_now_content != e.control:
            self.page.client_storage.set("alg",e.control.data["alg"])
            self.check_now_content.content.controls[0].name = None
            self.check_now_content.update()
            self.check_now_content = e.control
        elif self.check_now_content == e.control:
            self.page.client_storage.set("alg",None) 
            self.check_now_content = None

        if e.control.content.controls[0].name == ft.icons.CHECK:
            e.control.content.controls[0].name = None
        else:
            e.control.content.controls[0].name = ft.icons.CHECK

        # if self.page.client_storage.get("alg"):
        #     if self.page.client_storage.get("alg") == "NN"
        if self.check_now_content:
            self.image_content_update(self.check_now_content.data['path'])
        self.navigation_rail_update()
        e.control.update()

    def image_content_update(self, image):
        if image:
            self.image_content.src = image
        else:
            self.image_content.src = None
        self.image_content.update()
