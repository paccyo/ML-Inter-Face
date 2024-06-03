import flet as ft

def main(page: ft.Page):
    # Define the UI components
    page.title = "Neural Network Designer"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Sidebar with layer options
    sidebar = ft.Column(
        [
            ft.Text("Layer Options", style="headlineMedium"),
            ft.ElevatedButton("Dense", on_click=lambda e: add_layer("Dense")),
            ft.ElevatedButton("Conv", on_click=lambda e: add_layer("Conv")),
        ],
        alignment=ft.MainAxisAlignment.START,
        expand=False,
    )
    sidebar_container = ft.Container(
        sidebar,
        expand=False,
        margin=10,
        padding=15,
        bgcolor=ft.colors.GREY,
        border_radius=10,
        alignment=ft.alignment.top_center,
    )

    def on_drag_update(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    # Main design area with drag-and-drop functionality
    def add_layer(layer_type):
        if layer_type == 'Dense':
            rect = ft.GestureDetector(
                content=ft.Container(content=ft.Text(layer_type), bgcolor=ft.colors.CYAN, border_radius=15),
                width=100,
                height=50,
                mouse_cursor=ft.MouseCursor.MOVE,
                drag_interval=10,
                top=100,
                left=50,
                on_vertical_drag_update=on_drag_update
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
                on_vertical_drag_update=on_drag_update
            )
        design_area.content.controls.append(rect)
        page.update()

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

    # Layout
    page.add(
        ft.Row(
            [
                sidebar_container,
                ft.VerticalDivider(width=1, color="black"),
                design_area,
                ft.VerticalDivider(width=1, color="black"),
                preview_area,
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )
    )

# Start the app
ft.app(target=main)
