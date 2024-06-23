from components.util.Calldict import (layer_dicts, TEXTFIELD, DROPDOWN, MAIN, DETAIL)
from packages.categorical.image.nn.GenerateModelFile import ModelInfo
from packages.categorical.image.nn import GenerateBatfile, copy_to_userproject
from packages import read_activate_path

import flet as ft
import flet.canvas as cv 
import copy

class ModelBuild(ft.Tab):
    def __init__(self, page: ft.Page, text: str | None = None, content: ft.Control | None = None, tab_content: ft.Control | None = None, icon: str | None = None, ref: ft.Ref | None = None, visible: bool | None = None, adaptive: bool | None = None):
        super().__init__(text, content, tab_content, icon, ref, visible, adaptive)
        self.page = page
        self.text="モデル構築"
        self.icon=ft.icons.NUMBERS
        # Sidebar with layer options
        self.sidebar_layers = ft.Column(
            [
                ft.Text("Layers", style="headlineMedium"),
            ],
            alignment=ft.MainAxisAlignment.START,
            scroll=ft.ScrollMode.HIDDEN,
            expand=False,
        )
        for layer_name in layer_dicts.keys():
            self.sidebar_layers.controls.append(ft.ElevatedButton(layer_name, on_click=self.add_layer))

        self.sidebar_layers_container = ft.Container(
            self.sidebar_layers,
            expand=True,
            margin=1,
            padding=20,
            # bgcolor=ft.colors.GREY,
            border_radius=10,
            alignment=ft.alignment.top_left,
            # height=300,
            # width=200
        )

        self.sidebar_layerparam = ft.Column(
            [
                ft.Text("Layer Options", style="headlineMedium"),
            ],
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.START,
            width=300,
            expand=True,
        )
        self.sidebar__layerparam_container = ft.Container(
            self.sidebar_layerparam,
            expand=True,
            margin=1,
            padding=20,
            width=300,
            bgcolor=ft.colors.CYAN,
            border_radius=0,
            alignment=ft.alignment.top_left
        )

        self.design_area = ft.Container(
            content=
                cv.Canvas(
                content=ft.Stack(
                    [
                        ft.Text("Design", style="headlineMedium" ,text_align=ft.alignment.top_center),
                        ft.ElevatedButton(text="build", on_click=self.model_build, right=0, bottom=0)
                    ],
                    expand=True,
                ),
                width=600,
                height=800,
                # bgcolor=ft.colors.BLUE,
                # border_radius=15
            )
        )
        

        # Preview area
        self.preview_area = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Preview", style="headlineMedium"),
                    ft.Image(src="https://example.com/your_image.png", fit=ft.ImageFit.CONTAIN)
                ],
                scroll=ft.ScrollMode.HIDDEN
                ),
            alignment=ft.alignment.top_center,
            expand=True,
            bgcolor=ft.colors.BLUE,
            border_radius=15,
        )


        
        
        self.content=ft.Row(
            [
                ft.Column(
                    [
                        self.sidebar_layers_container,
                        ft.Divider(color="black"),
                        self.sidebar__layerparam_container,
                    ],
                ),
                ft.VerticalDivider(width=1, color="black"),
                self.design_area,
                ft.VerticalDivider(width=1, color="black"),
                self.preview_area,
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        ) 




    def update_connect_layer(self):
        # # # print(self.design_area.content.shapes)
        layers= sorted(self.design_area.content.content.controls[2:], key = lambda x:x.top)
        self.design_area.content.shapes = []
        draw_line_list = []
        for layer in layers[:-1]:
            draw_line_list.append([layer.left+(layer.width//2),layer.top+layer.height])
        for i, layer in enumerate(layers[1:]):
            draw_line_list[i].append(layer.left+(layer.width//2))
            draw_line_list[i].append(layer.top)
        for draw_line_point in draw_line_list:
            self.design_area.content.shapes.append(
                cv.Line(
                    draw_line_point[0],
                    draw_line_point[1], 
                    draw_line_point[2], 
                    draw_line_point[3], 
                    ft.Paint(stroke_width=2, color=ft.colors.BLACK)
                )
            )
        self.design_area.update()

    def on_drag_update(self, e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()
        # # # print(design_area.content.controls)
        self.update_connect_layer()

    def on_tap_layer(self, e):
        
        layer_type = e.control.content.content.value
        detail_view = True if e.control.content.content.data["detail_view"] == "True" else False
        # # # print(layer_type)
        # # # print(layer_params)


        def on_change_params(e_control):
            if e_control.control.value.isdigit():
                value = int(e_control.control.value)
            else:
                value = e_control.control.value

            if e_control.control.data["index"] == None:
                e.control.content.content.data[e_control.control.data["param"]][0] = value
            else:
                # print(e_control.control.data["index"])
                # print(value,type(value))
                # print(e.control.content.content.data[e_control.control.data["param"]][0])
                # print(e.control.content.content.data[e_control.control.data["param"]][0][e_control.control.data["index"]])
                e.control.content.content.data[e_control.control.data["param"]][0] = list(e.control.content.content.data[e_control.control.data["param"]][0])
                e.control.content.content.data[e_control.control.data["param"]][0][e_control.control.data["index"]] = value
                e.control.content.content.data[e_control.control.data["param"]][0] = tuple(e.control.content.content.data[e_control.control.data["param"]][0])
            # e.control.content.content.data["Default"]["activate"] = edrop.control.value
            e.control.update()
        
        def on_change_detail_checkbox(e_checkbox):
            # # # print(e.control.content.content.data["detail_view"])
            if e_checkbox.control.value == True:
                e.control.content.content.data["detail_view"] = "True"
                update_layer_params(layer_type, True)
            else:
                e.control.content.content.data["detail_view"] = "False"
                update_layer_params(layer_type, False)

        def update_layer_params(layer_type, detail = False):
            data = layer_dicts
            # layer_params = data[layer_type]
            # print(e.control.content.content.data)
            layer_params = e.control.content.content.data
            params = []
            
            params.append(ft.Text(layer_type, style="headlineMedium"))
            params.append(ft.Checkbox(label="detail option", value=detail, on_change = on_change_detail_checkbox))
            
            for param, value in layer_params.items():
                if param in ["color", 'detail_view']:
                    continue
                rect = []
                param_value = value[0]
                control_type = value[1]
                main_detail = value[3]
                tips = value[4]
                if main_detail == MAIN or detail:
                    if control_type == TEXTFIELD:
                        if value[2] == 1:
                            rect = ft.Row( 
                                controls=[
                                    ft.Tooltip(
                                        message = tips,
                                        content=ft.Text(value=param+':')),
                                    ft.TextField(
                                        value=param_value,
                                        border="underline",
                                        text_size=20,
                                        on_change=on_change_params,
                                        data={"index":None,"param":param}
                                    )
                                ],
                                width=200,
                            )
                        elif value[2] == 2:
                            rect = ft.Row( 
                                controls=[
                                    ft.Tooltip(
                                        message = tips,
                                        content=ft.Text(value=param+':')),
                                    ft.Text(value='('),
                                    ft.TextField(
                                        value=param_value[0],
                                        border="underline",
                                        text_size=20,
                                        width=30,
                                        on_change=on_change_params,
                                        data={"index":0,"param":param}
                                    ),
                                    ft.Text(value=','),
                                    ft.TextField(
                                        value=param_value[1],
                                        border="underline",
                                        text_size=20,
                                        width=30,
                                        on_change=on_change_params,
                                        data={"index":1,"param":param}
                                    ),
                                    ft.Text(value=')'),
                                ],
                                width=200,
                            )

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
                                    options=[ft.dropdown.Option(str(x)) for x in value[2]],
                                    data={"index":None,"param":param}
                                )
                            ],
                            width=200,
                        )
                if rect != []:
                    params.append(rect)

            self.sidebar__layerparam_container.content.controls = params
            
            self.sidebar__layerparam_container.content.update()

        update_layer_params(layer_type, detail_view)


    def on_change_detail_checkbox(self, e):
        detail = e.control.value
        if detail == True:
            detail_view = True
            self.on_tap_layer()



    # Main design area with drag-and-drop functionality
    def add_layer(self, e):
        data = layer_dicts
        # # print(e.control.text)
        rect = ft.GestureDetector(
                content=ft.Container(content=ft.Text(e.control.text),bgcolor=data[e.control.text]["color"], border_radius=15),
                width=100,
                height=50,
                mouse_cursor=ft.MouseCursor.MOVE,
                drag_interval=10,
                top=100,
                left=50,
                on_vertical_drag_update=self.on_drag_update,
                on_tap=self.on_tap_layer,
                on_double_tap=self.on_double_tap_del_layer,
            )

        print(data[e.control.text])
        # copy.deepcopy(x)
        # rect.content.content.data = data[e.control.text]
        rect.content.content.data = copy.deepcopy(data[e.control.text])
        self.design_area.content.content.controls.append(rect)
        self.update_connect_layer()
        self.design_area.content.content.update()
    
    def on_double_tap_del_layer(self, e):
        # e.control
        for i,control in enumerate(self.design_area.content.content.controls):
            if e.control == control:
                self.design_area.content.content.controls.pop(i)
        self.update_connect_layer()
        self.page.update()

    def model_build(self, e):
        layers=sorted(self.design_area.content.content.controls[2:], key = lambda x:x.top)
        lay_format = {}
        for i,layer in enumerate(layers):
            # # # print(layer.content.content.data)
            # lay_format.append()
            layer_type = layer.content.content.value
            layer_detail = layer.content.content.data["detail_view"]
            layer_data = {}
            for param,value in layer.content.content.data.items():
                val = value[0]
                detail = value[3]
                if param not in ["color","detail_view"]:
                    if detail == MAIN or layer_detail == "True":
                        layer_data[param] = val
            # layer_data = {param:value[0] for param, value in layer.content.content.data.items() if param not in ["color","detail_view"]}
            # # print(layer_type+str(i).zfill(4))
            # # print(layer_data)
            for key, value in layer_data.items():
                if type(value) == str:
                    if value == "True":
                        layer_data[key] = True
                    elif value == "False":
                        layer_data[key] = False
                    elif value == "None":
                        layer_data[key] = None
                    else:
                        layer_data[key] = "\'" + value + "\'" 
                else:
                    pass
            lay_format[layer_type+str(i).zfill(4)] = layer_data     
        print(lay_format)
        self.page.client_storage.set("model",lay_format)
        model_info = ModelInfo()
        model_info.send(model_dict=lay_format,
                             project_path=self.page.client_storage.get("project_path")+"/Scripts",
                             shape=model_info.get_shape(image_size=self.page.client_storage.get("target_size"),
                                                color_mode=self.page.client_storage.get("color_mode"))
                             )
        
        copy_to_userproject.CopyModelGraph(target_path=self.page.client_storage.get("project_path")+"/Scripts")
        GenerateBatfile.generate_output_graph_bat(target_path=self.page.client_storage.get("project_path")+"/Scripts",
                                                  run_path=read_activate_path.read_activ_path(),
                                                  project_path=self.page.client_storage.get("project_path")+"/Result")
        GenerateBatfile.Runbat(self.page.client_storage.get("project_path")+"/Scripts"+"/output_model_graph_run.bat")

        self.preview_area.content.controls[1].src = self.page.client_storage.get("project_path")+"/Result/model.png"
        self.page.update()


        
