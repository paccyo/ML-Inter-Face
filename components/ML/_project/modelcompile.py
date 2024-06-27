from packages.util.Calldict import (compile_dicts,MAIN,DETAIL,DROPDOWN,TEXTFIELD)
from packages.nn.GenerateCompileFile import CompileInfo

import flet as ft
import flet.canvas as cv

class ModelCompile(ft.Tab):
    def __init__(self, page: ft.Page, text: str | None = None, content: ft.Control | None = None, tab_content: ft.Control | None = None, icon: str | None = None, ref: ft.Ref | None = None, visible: bool | None = None, adaptive: bool | None = None):
        super().__init__(text, content, tab_content, icon, ref, visible, adaptive)
        self.page = page
        self.text="モデルコンパイル"
        self.icon=ft.icons.ADJUST
        self.compile_dicts = compile_dicts
        # print(self.compile_dicts)
        self.optimizer_set = []
        self.other_option = []

        self.optimizer_set.append(
            ft.Row(
                controls=[
                    ft.Tooltip(
                        message = self.compile_dicts["select_optimizer"][4],
                        content=ft.Text(value="optimizer"+':')),
                    ft.Dropdown(
                        width=100,
                        height=50,
                        text_size=10,
                        scale=1,
                        on_change=self.select_optimizer,
                        value=self.compile_dicts["select_optimizer"][0],
                        options=[ft.dropdown.Option(str(x)) for x in self.compile_dicts["select_optimizer"][2]]
                    )
                ]
            )
        )

        self.other_option.append(
            ft.Row(
                controls=[
                    ft.Tooltip(
                        message = self.compile_dicts["loss"][4],
                        content=ft.Text(value="loss"+':')),
                    ft.Dropdown(
                        width=100,
                        height=50,
                        text_size=10,
                        scale=1,
                        on_change=self.on_change_loss,
                        value=self.compile_dicts["loss"][0],
                        options=[ft.dropdown.Option(str(x)) for x in self.compile_dicts["loss"][2]]
                    )
                ]
            )
        )
        self.other_option.append(
            ft.Row(
                controls=[
                    ft.Tooltip(
                        message = self.compile_dicts["metrics"][4],
                        content=ft.Text(value="metrics"+':')),
                    ft.Dropdown(
                        width=100,
                        height=50,
                        text_size=10,
                        scale=1,
                        value=self.compile_dicts["metrics"][0],
                        on_change=self.on_change_metrics,
                        options=[ft.dropdown.Option(str(x)) for x in self.compile_dicts["metrics"][2]]
                    )
                ]
            )
        )
        

        self.content=ft.Stack(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Container(content=ft.Column(controls=self.optimizer_set)),
                                    ft.Divider(),
                                    ft.Container(content=ft.Column(controls=[])),
                                ]
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=self.other_option
                            )
                        ),
                    ]
                ),
                ft.ElevatedButton(text="compile", on_click=self.on_click_compile, bottom=0,right=0)
            ]
        )
    def on_change_metrics(self, e):
        self.compile_dicts["metrics"][0] = e.control.value

    def on_change_loss(self, e):
        self.compile_dicts["loss"][0] = e.control.value

    def select_optimizer(self, e):
        optimizer = e.control.value
        self.compile_dicts["select_optimizer"][0] = optimizer
        detail_view = True if self.compile_dicts["optimizer"][optimizer]["detail_view"] == "True" else False

        def on_change_params(e_control):
            self.compile_dicts["optimizer"][optimizer][e_control.control.data["param"]][0] = e_control.control.value
            # print(e_control.control.value)

        def on_change_detail_checkbox(e_control):
            if e_control.control.value == True:
                self.compile_dicts["optimizer"][optimizer]["detail_view"] = "True"
                optimizer_params_view(optimizer, True)
            else:
                self.compile_dicts["optimizer"][optimizer]["detail_view"] = "False"
                optimizer_params_view(optimizer, False)


        def optimizer_params_view(optimizer_name, detail):
            if optimizer_name == "None":
                self.content.controls[0].controls[0].content.controls[2].content.controls = []
                self.content.controls[0].controls[0].content.controls[2].content.update()
                return
            
            optimizer_params = []
            optimizer_params.append(ft.Checkbox(label="detail option", value=detail, on_change = on_change_detail_checkbox))

            for param, value in compile_dicts["optimizer"][optimizer_name].items():
                if param in ["color", 'detail_view']:
                    continue
                rect = []
                param_value = value[0]
                control_type = value[1]
                main_detail = value[3]
                tips = value[4]
                if main_detail == MAIN or detail:
                    if control_type == TEXTFIELD:
                        rect = ft.Row(
                            controls=[
                                ft.Tooltip(
                                    message = tips,
                                    content=ft.Text(value=param+':')),
                                ft.TextField(
                                    value=param_value,
                                    border="underline",
                                    text_size=20,
                                    on_change=on_change_params
                                )
                            ],
                            width=200,
                        )
                        rect.controls[1].data = {"param":param}
                    elif control_type == DROPDOWN:
                        rect = ft.Row(
                            controls=[
                                ft.Tooltip(
                                    message = tips,
                                    content=ft.Text(value=param+':')),
                                ft.Dropdown(
                                    width=100,
                                    height=50,
                                    text_size=10,
                                    scale=1,
                                    value=param_value,
                                    on_change=on_change_params,
                                    options=[ft.dropdown.Option(str(x)) for x in value[2]]
                                )
                            ],
                            width=200,
                        )
                        rect.controls[1].data = {"param":param}
                if rect != []:
                    optimizer_params.append(rect)
            self.content.controls[0].controls[0].content.controls[2].content.controls = optimizer_params
            self.content.controls[0].controls[0].content.controls[2].content.update()


        optimizer_params_view(optimizer, detail_view)


    def on_click_compile(self, e):
        compile_info = CompileInfo()
        compile_state = {}
        optimizer = self.compile_dicts["select_optimizer"][0]
        compile_state["optimizer"] = {optimizer:self.compile_dicts["optimizer"][optimizer]}
        compile_state["loss"] = self.compile_dicts["loss"][0]
        compile_state["metrics"] = self.compile_dicts["metrics"][0]

        for key, value in compile_state.items():
            if key == "detail_view":
                continue
            if type(value) == str:
                if value == "True":
                    compile_state[key] = True
                elif value == "False":
                    compile_state[key] = False
                elif value == "None":
                    compile_state[key] = None
                else:
                    compile_state[key] = value
            else:
                compile_state[key] = value
        detail = True if compile_state["optimizer"][optimizer]["detail_view"] == "True" else False
        compile_state["optimizer"][optimizer] = {key:value[0] for key,value in compile_state["optimizer"][optimizer].items() if value[3] == MAIN or detail}
        
        
        
        for key, value in compile_state["optimizer"][optimizer].items():
            if key == "detail_view":
                continue
            if type(value) == str:
                if value == "True":
                    compile_state["optimizer"][key] = True
                elif value == "False":
                    compile_state["optimizer"][key] = False
                elif value == "None":
                    compile_state["optimizer"][key] = None
                else:
                    compile_state["optimizer"][key] = value
            else:
                compile_state["optimizer"][key] = value

        if compile_state["loss"] != None:
            compile_state["loss"] = ["\'"+compile_state["loss"]+"\'"]
        if compile_state["metrics"] != None:
            compile_state["metrics"] = ["\'"+compile_state["metrics"]+"\'"]

        # print(compile_state)
        self.page.client_storage.set("compile", compile_state)
        compile_info.send(compile_state, 
                            project_path=self.page.client_storage.get("project_path")+"/Scripts"
                            )
