import flet as ft
import flet.canvas as cv 
from components.util.Calldict import (dicts, TEXTFIELD, DROPDOWN)

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
        for layer_name in dicts.keys():
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
                    ft.Image(src="https://example.com/your_image.png", fit=ft.ImageFit.CONTAIN, height=300, width=300)
                ]),
            alignment=ft.alignment.top_center,
            expand=True,
            bgcolor=ft.colors.BLUE,
            border_radius=15
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
        # print(self.design_area.content.shapes)
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
        # print(design_area.content.controls)
        self.update_connect_layer()

    def on_tap_layer(self, e):
        data = dicts
        def on_change_params(e_control):
            # print(e_control.control.text)
            print(e_control.control.data)
            print(e_control.control.value)
            print(e.control.content.content.data)
            e.control.content.content.data[e_control.control.data["param"]][0] = e_control.control.value
            # e.control.content.content.data["Default"]["activate"] = edrop.control.value
            e.control.update()


        layer_type = e.control.content.content.value
        layer_params = data[layer_type]
        print(layer_type)
        print(layer_params)
        params = []

        params.append(ft.Text(layer_type, style="headlineMedium"))
        for param, value in layer_params.items():
            print(param,value)
            rect = []
            param_value = value[0]
            control_type = value[1]
            if control_type == TEXTFIELD:
                rect = ft.Row(
                    controls=[
                        ft.Text(value=param+":", size=20),
                        ft.TextField(
                            value=param_value,
                            border="underline",
                            text_size=20,
                            on_change=on_change_params
                        )
                    ],
                    width=200,
                    # scroll=ft.ScrollMode.HIDDEN,
                )
                rect.controls[1].data = {"param":param}
            elif control_type == DROPDOWN:
                rect = ft.Row(
                    controls=[
                        ft.Text(param+":", size=20),
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
                    # scroll=ft.ScrollMode.HIDDEN,
                )
                rect.controls[1].data = {"param":param}
            if rect != []:
                params.append(rect)
            

        # print(param)
        


        self.sidebar__layerparam_container.content.controls = params
        # print(self.sidebar__layerparam_container.content.controls)
        
        self.sidebar__layerparam_container.content.update()

        

    # Main design area with drag-and-drop functionality
    def add_layer(self, e):
        data = dicts
        print(e.control.text)
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
            )

        rect.content.content.data = data[e.control.text]
        self.design_area.content.content.controls.append(rect)
        self.update_connect_layer()
        self.design_area.content.content.update()

    def model_build(self, e):
        layers=sorted(self.design_area.content.content.controls[2:], key = lambda x:x.top)
        lay_format = {}
        for i,layer in enumerate(layers):
            # print(layer.content.content.data)
            # lay_format.append()
            layer_type = layer.content.content.value
            layer_data = {param:value[0] for param, value in layer.content.content.data.items() if param != "color"}
            print(layer_type+str(i).zfill(4))
            print(layer_data)
            lay_format[layer_type+str(i).zfill(4)] = layer_data        
        