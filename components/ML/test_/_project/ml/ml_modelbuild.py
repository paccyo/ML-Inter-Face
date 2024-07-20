from packages.util.Calldict import ML_dicts, DETAIL,DROPDOWN,MAIN,TEXTFIELD
from packages.GenerateModelFile import ModelInfo

import flet as ft

class ModelBuild_ML(ft.Container):
    def __init__(self, page:ft.Page, algorythm = None):
        super().__init__()
        self.page = page
        self.algorythm = algorythm

        self.expand = True

        self.dicts = ML_dicts[self.algorythm]
        

        self.params_content = ft.Container(
            content=ft.Column(
                controls=[],
            ),
            expand=True,
            width=500,
            padding=ft.padding.all(50)
        )


        for key, value in self.dicts.items():
            rect = []
            def_value = value[0]
            option = value[2]
            input_type = value[1]
            detail = value[3]
            hint = value[4]
            if input_type == TEXTFIELD:
                rect = ft.Row(
                    controls=[
                        ft.Text(value=key),
                        ft.TextField(
                            value=def_value,
                            on_change=self.on_change_params,
                            data={"key":key}
                        )
                    ]
                )
            elif input_type == DROPDOWN:
                rect = ft.Row(
                    controls=[
                        ft.Text(value=key),
                        ft.Dropdown(
                            value=def_value,
                            options=[ft.dropdown.Option(x) for x in option],
                            on_change=self.on_change_params,
                            data={"key":key}
                        )
                    ]
                )
            if rect != []:
                self.params_content.content.controls.append(rect)


        self.build_button = ft.Container(
            content=ft.ElevatedButton(
              text="build",
              on_click=self.on_click_build_button,  
            ),
            alignment=ft.alignment.bottom_right,
            width=500,
            height=100,
        )

        self.image_content = ft.Container(
            expand=True,
        )


        self.content = ft.Row(
            controls=[
                
                ft.Column(
                    controls=[
                        self.params_content,
                        self.build_button,
                    ]
                ),
                ft.VerticalDivider(),
                self.image_content
            ],
            expand=True
        )


    def params_content_update(self,detail):

        for key, value in self.dicts.items():
            rect = []
            def_value = value[0]
            option = value[2]
            input_type = value[1]
            detail = value[3]
            hint = value[4]
            if input_type == TEXTFIELD:
                rect = ft.Row(
                    controls=[
                        ft.Text(value=key),
                        ft.TextField(value=def_value)
                    ]
                )
            elif input_type == DROPDOWN:
                rect = ft.Row(
                    controls=[
                        ft.Text(value=key),
                        ft.Dropdown(
                            value=def_value,
                            options=[ft.dropdown.Option(x) for x in option]
                        )
                    ]
                )
            if rect != []:
                self.params_content.content.controls.append(rect)
        
        self.params_content.content.update()


    def on_change_params(self,e):
        key = e.control.data
        self.dicts[key][0] = e.control.value

    def on_click_build_button(self,e):
        modelinfo = ModelInfo(mode="ML")
        send_dict = {}
        send_dict["alg"] = self.algorythm
        for key, value in self.dicts.items():
            v = value[0]
            if v == "None":
                v = None
            elif v == "True":
                v = True
            elif v == "False":
                v = False

            send_dict[key] = v
        
        modelinfo.send(
            model_dict=send_dict, 
            project_path=self.page.client_storage.get("project_file_path")+"/Scripts"
        )
