import flet as ft
import inspect

def main(page: ft.Page):
    # Define the UI components
    page.title = "Neural Network Designer"
    page.vertical_alignment = ft.MainAxisAlignment.START

    def on_drag_update(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()
        # print(design_area.content.controls)
        layer = []
        # for x in design_area.content.controls[1:]:
            # layer.append([x.top,x.content.content.value])
            # print(x.content.content.data)
        layer.sort()
        # print(layer)


    def on_tap_layer(e):

        def on_change_activate(edrop):
            print(edrop.control.value)
            print(e.control.content.content.data)
            e.control.content.content.data["Default"]["activate"] = edrop.control.value
            e.control.update()

        # print(inspect.getmembers(e))
        print(e.control.content.content.value)
        print(e.control.content.content.data)
        params = []
        params.append(ft.Text(e.control.content.content.value, style="headlineMedium"),)
        params.append(ft.Text('input:'+str(e.control.content.content.data["Default"]["input"]), size=20))
        params.append(ft.Text('output:'+str(e.control.content.content.data["Default"]["output"]), size=20))
        params.append(ft.Row([
            ft.Text('activate:', size=20),
            ft.Dropdown(
                width=100,
                height=50,
                value=e.control.content.content.data["Default"]["activate"],
                on_change=on_change_activate,
                options=[
                    ft.dropdown.Option("relu"),
                    ft.dropdown.Option("softmax"),
                    ft.dropdown.Option("sigmoid"),
                ])
        ]))
        sidebar__layerparam_container.content.controls = params

        page.update()
    
        
    
    # Main design area with drag-and-drop functionality
    def add_layer(layer_type):
        data = {"Default":{"input":0,"output":0,"activate":"relu"},"Dense":{"units":0},"Conv":{"kernel Size":(0,0)}}
        if layer_type == 'Dense':
            rect = ft.GestureDetector(
                content=ft.Container(content=ft.Text(layer_type), bgcolor=ft.colors.CYAN, border_radius=15),
                width=100,
                height=50,
                mouse_cursor=ft.MouseCursor.MOVE,
                drag_interval=10,
                top=100,
                left=50,
                on_vertical_drag_update=on_drag_update,
                on_tap=on_tap_layer,
            )
        elif layer_type == 'Conv':
            rect = ft.GestureDetector(
                content=ft.Container(content=ft.Text(layer_type), bgcolor=ft.colors.ORANGE, border_radius=15),
                width=100,
                height=50,
                mouse_cursor=ft.MouseCursor.MOVE,
                drag_interval=10,
                top=100,
                left=50,
                on_vertical_drag_update=on_drag_update,
                on_tap=on_tap_layer,
            )
        rect.content.content.data = data
        design_area.content.controls.append(rect)
        page.update()

    # Sidebar with layer options
    sidebar_layers = ft.Column(
        [
            ft.Text("Layers", style="headlineMedium"),
            ft.ElevatedButton("Dense", on_click=lambda e: add_layer("Dense")),
            ft.ElevatedButton("Conv", on_click=lambda e: add_layer("Conv")),
        ],
        alignment=ft.MainAxisAlignment.START,
        expand=False,
    )
    sidebar_layers_container = ft.Container(
        sidebar_layers,
        expand=True,
        margin=1,
        padding=20,
        # bgcolor=ft.colors.GREY,
        border_radius=10,
        alignment=ft.alignment.top_left,
        # height=300,
        # width=200
    )

    sidebar_layerparam = ft.Column(
        [
            ft.Text("Layer Options", style="headlineMedium"),
        ],
        scroll=ft.ScrollMode.HIDDEN,
        alignment=ft.MainAxisAlignment.START,
        expand=False,
    )
    sidebar__layerparam_container = ft.Container(
        sidebar_layerparam,
        expand=True,
        margin=1,
        padding=20,
        bgcolor=ft.colors.CYAN,
        border_radius=10,
        alignment=ft.alignment.top_left,
        # height=300,
        # width=200
    )

    design_area = ft.Container(content=ft.Stack(
        [
            ft.Text("Design", style="headlineMedium" ,text_align=ft.alignment.top_center)
        ],
        expand=True,    
        ),
        width=400,
        height=800,
        bgcolor=ft.colors.BLUE,
        border_radius=15
    )

    # Preview area
    preview_area = ft.Container(
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



    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="モデル構築",
                content=ft.Row(
                    [
                        ft.Column(
                            [
                                sidebar_layers_container,
                                ft.Divider(color="black"),
                                sidebar__layerparam_container,
                            ]
                        ),
                        ft.VerticalDivider(width=1, color="black"),
                        design_area,
                        ft.VerticalDivider(width=1, color="black"),
                        preview_area,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                )
                # ft.Container(
                #     content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )

    page.add(t)
    # Layout
    # page.add(
        
    #     ft.Row(
    #         [   ft.Column([sidebar_container,
    #                 ft.Divider(color="black"),
    #                 sidebar_container1
    #             ]),
    #             ft.VerticalDivider(width=1, color="black"),
    #             design_area,
    #             ft.VerticalDivider(width=1, color="black"),
    #             preview_area,
    #         ],
    #         alignment=ft.MainAxisAlignment.START,
    #         expand=True,
    #     )
    # )

# Start the app
ft.app(target=main)
