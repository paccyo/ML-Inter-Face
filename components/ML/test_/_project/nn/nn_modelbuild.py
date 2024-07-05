from packages.util.Calldict import (layer_dicts, TEXTFIELD, DROPDOWN, MAIN, DETAIL)

import flet as ft 
import flet.canvas as cv

class ModelBuild_NN(ft.Container):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
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
        )

        for layer_name in layer_dicts.keys():
            self.sidebar_layers_container.content.controls[1].controls.append(ft.ElevatedButton(layer_name,
                                                                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), 
                                                                #   on_click=self.add_layer
                                                                  ))

        self.sidebar__layer_param_container = ft.Container(
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
            alignment=ft.alignment.top_left
        )

        self.design_area = ft.Container(
            content=cv.Canvas(
                content=ft.Stack(
                    [
                        ft.Text("Design", style="headlineMedium" ,text_align=ft.alignment.top_center,left=0,right=0),
                        # ft.ElevatedButton(text="build", on_click=self.model_build, right=0, bottom=0)
                    ],
                    # expand=True,
                ),
                # expand=True,
            ),
            bgcolor=ft.colors.RED,
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
            bgcolor=ft.colors.BLUE,
            border_radius=15,
        )

        self.sidebar_content = ft.Column(
            [
                self.sidebar_layers_container,
                ft.Divider(),
                self.sidebar__layer_param_container,
            ],
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

        # self.content = ft.Row(
        #     controls=[
        #         ft.Container(width=200),
        #         ft.VerticalDivider(),
        #         ft.Container(
        #             # content = ft.Row(
        #             #     ft.Container(expand=True),
        #             #     ft.VerticalDivider(),
        #             #     ft.Container(width=200),
        #             # ),
        #             expand=True,
        #             bgcolor=ft.colors.RED
        #         )
        #     ],
        #     expand=True
        #     )
