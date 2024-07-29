from packages.util.Calldict import (layer_dicts, TEXTFIELD, DROPDOWN, MAIN, DETAIL)
from packages.GenerateModelFile import ModelInfo
from packages import GenerateBatfile, copy_to_userproject
from packages import read_activate_path
from packages import py_to_dict

import copy
import flet as ft 
import flet.canvas as cv
import pandas as pd



class ModelBuild_NN(ft.Container):
    class Pick_file_button(ft.ElevatedButton):
        def __init__(self, page:ft.Page):
            super().__init__()
            
            self.page = page
            self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
            # self.page.overlay.extend([self.pick_files_dialog])
            

            self.bottom = 0
            self.left = 0
            self.text = " "
            self.icon=ft.icons.FOLDER_OPEN
            # self.on_click=lambda _: self.get_directory_dialog.pick_files(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["csv"], allow_multiple=False)
            self.on_click=self.pick_files
            self.style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            self.width=50
            self.height=50

        async def pick_files(self,_):
            await self.pick_files_dialog.pick_files_async(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["py"], allow_multiple=False)

        async def pick_files_result(self, e: ft.FilePickerResultEvent):
            file = e.files[0]
            result = py_to_dict.convert_model_to_dict(file)




    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True


        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        # self.page.overlay.extend([self.pick_files_dialog])


        self.sidebar_layers_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Layers", style="headlineMedium"),
                    ft.Column(
                        controls=[],
                        alignment=ft.MainAxisAlignment.START,
                        scroll=ft.ScrollMode.HIDDEN,
                        expand=True
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            expand=True,
            alignment=ft.alignment.top_left,
            border=ft.border.only(bottom=ft.BorderSide(width=1)),
            padding=ft.padding.only(bottom=5)
        )

        for layer_name in layer_dicts.keys():
            self.sidebar_layers_container.content.controls[1].controls.append(
                ft.Tooltip(
                    message=layer_dicts[layer_name]['description'],
                    content=ft.ElevatedButton(
                        text=layer_name, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
                        on_click=self.add_layer,
                        expand=True,
                    ),
                    height=30,
                )
            )

        self.sidebar_layer_param_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Layer Options", style="headlineMedium"),
                    ft.Column(
                        controls = [],
                        scroll=ft.ScrollMode.HIDDEN,
                        alignment=ft.MainAxisAlignment.START,
                        expand=True,
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                expand=True,
            ),
            expand=True,
            alignment=ft.alignment.top_left,
        )

        self.design_area = ft.Container(
            content=cv.Canvas(
                content=ft.Stack(
                    [
                        ft.Text("Design", style="headlineMedium" ,text_align=ft.alignment.top_center,left=0,right=0),
                        ft.ElevatedButton(text="build", on_click=self.model_build, right=0, bottom=0),
                        # self.Pick_file_button(self.page),
                        ft.ElevatedButton(
                            bottom = 0,
                            left = 0,
                            text = " ",
                            icon=ft.icons.FOLDER_OPEN,
                            # self.on_click=lambda _: self.get_directory_dialog.pick_files(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["csv"], allow_multiple=False)
                            on_click=self.pick_files,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            width=50,
                            height=50,
                        )
                    ],
                ),
            ),
            bgcolor=ft.colors.GREY_100,
            expand=True,
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
            width=300,
            bgcolor=ft.colors.GREY_100,
            border_radius=15,
        )

        self.sidebar_content = ft.Column(
            [
                self.sidebar_layers_container,
                self.sidebar_layer_param_container,
            ],
            width=250,
        )

        
        self.content=ft.Row(
            [
                self.sidebar_content,
                ft.VerticalDivider(width=1, color="black"),
                self.design_area,
                ft.VerticalDivider(width=1, color="black"),
                self.preview_area,
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        ) 
    # happens when example is added to the page (when user chooses the FilePicker control from the grid)
    def did_mount(self):
        self.page.overlay.append(self.pick_files_dialog)
        self.page.update()

    # happens when example is removed from the page (when user chooses different control group on the navigation rail)
    def will_unmount(self):
        self.page.overlay.remove(self.pick_files_dialog)
        self.page.update()

    async def pick_files(self,_):
        await self.pick_files_dialog.pick_files_async(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["py"], allow_multiple=False)

    
    async def pick_files_result(self, e: ft.FilePickerResultEvent):
        file = e.files[0]
        result = py_to_dict.convert_model_to_dict(file.path)
        self.import_model_file_add_layer(result)
    
    def import_model_file_add_layer(self,result):
        top_num = 100
        # print(len(result))
        for layer in result:

            key = list(layer.keys())
            value = list(layer.values())
            rect = ft.GestureDetector(
                    content=ft.Container(content=ft.Text(key[0]),bgcolor=value[0]["color"], border_radius=15),
                    width=100,
                    height=50,
                    mouse_cursor=ft.MouseCursor.MOVE,
                    drag_interval=10,
                    top=top_num,
                    left=50,
                    on_vertical_drag_update=self.on_drag_update,
                    on_tap=self.on_tap_layer,
                    on_double_tap=self.on_double_tap_del_layer,
                )
            # print(value)
            rect.content.content.data = copy.deepcopy(value[0])
            self.design_area.content.content.controls.append(rect)
            
            top_num+=50
        self.update_connect_layer()
        self.design_area.content.content.update()


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


    def update_connect_layer(self):
        # # # print(self.design_area.content.shapes)
        layers= sorted(self.design_area.content.content.controls[3:], key = lambda x:x.top)
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
        
        print(e.control.content.content.data["detail_view"])
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

            self.sidebar_layer_param_container.content.controls = params
            
            self.sidebar_layer_param_container.content.update()

        update_layer_params(layer_type, detail_view)


    def on_change_detail_checkbox(self, e):
        detail = e.control.value
        if detail == True:
            detail_view = True
            self.on_tap_layer()



    # Main design area with drag-and-drop functionality

    
    def on_double_tap_del_layer(self, e):
        # e.control
        for i,control in enumerate(self.design_area.content.content.controls):
            if e.control == control:
                self.design_area.content.content.controls.pop(i)
        self.update_connect_layer()
        self.page.update()

    def model_build(self, e):
        layers=sorted(self.design_area.content.content.controls[3:], key = lambda x:x.top)
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
        project_path = self.page.client_storage.get("project_file_path")
        model_info = ModelInfo(mode="NN")
        project_info = self.page.client_storage.get("project_info")
        data_type = project_info["data_type"]
        if data_type == "image":
            model_info.send(model_dict=lay_format,
                                    project_path=project_path+"/Scripts",
                                    shape=model_info.get_image_shape(image_size=self.page.client_storage.get("target_size"),
                                                    color_mode=self.page.client_storage.get("color_mode"))
                                    )
        elif data_type == "dataframe":
            df = pd.read_csv(project_path+"/Data/original_data.csv")
            print(df)
            target_num = model_info.get_classnums(df=df, col_name=self.page.client_storage.get("target_column"))
            self.page.client_storage.set("class_num",target_num)
            model_info.send(model_dict=lay_format,
                            project_path=project_path+"/Scripts",
                            shape=model_info.get_dataframe_shape(dataset_path=project_path+"/Data/dataset"))
        copy_to_userproject.CopyModelGraph(target_path=project_path+"/Scripts")
        GenerateBatfile.generate_output_graph_bat(target_path=project_path+"/Scripts",
                                                  run_path=read_activate_path.read_activ_path(),
                                                  project_path=project_path+"/Result")
        GenerateBatfile.Runbat(project_path+"/Scripts"+"/output_model_graph_run.bat")

        self.preview_area.content.controls[1].src = project_path+"/Result/model.png"
        self.page.update()


    

    
            
