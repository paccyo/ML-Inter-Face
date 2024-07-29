from packages.util.Calldict import ML_dicts, DETAIL,DROPDOWN,MAIN,TEXTFIELD
from packages.GenerateModelFile import ModelInfo

import flet as ft
import asyncio

class ModelBuild_ML(ft.Container):
    def __init__(self, page:ft.Page, algorythm = None):
        super().__init__()
        self.page = page
        self.algorythm = algorythm

        self.expand = True

        self.dicts = ML_dicts[self.algorythm]
        
        self.detail = False

        self.params_content = ft.Container(
            content=ft.Column(
                controls=[],
            ),
            expand=True,
            width=500,
            padding=ft.padding.all(50)
        )

        # ft.Checkbox(label="detail option", value=detail, on_change = on_change_detail_checkbox)
        self.params_content.content.controls = self.params_content_update()

        self.build_button = ft.Container(
            content=ft.ElevatedButton(
              text="build",
              on_click=self.on_click_build_button,  
            ),
            alignment=ft.alignment.bottom_right,
            width=500,
            height=100,
        )

        self.video_content = ft.Container(
            content=ft.Video(
                playlist=[ft.VideoMedia("packages/data_expansion_video/none.mp4")],
                fit=ft.ImageFit.CONTAIN,
                playlist_mode=ft.PlaylistMode.LOOP,
                autoplay=True,
            ),
            expand=True,
        )


        self.content = ft.Row(
            controls=[
                
                ft.Column(
                    controls=[
                        ft.Checkbox(label="detail option", value=False, on_change = self.on_change_detail_checkbox),
                        self.params_content,
                        self.build_button,
                    ]
                ),
                ft.VerticalDivider(),
                self.video_content
            ],
            expand=True
        )

    def on_change_detail_checkbox(self,e):
        self.detail = e.control.value
        self.params_content.content.controls = self.params_content_update()
        self.params_content.update()

    def params_content_update(self):
        rect_list = []
        for key, value in self.dicts.items():
            if key in ['detail_view']:
                continue
            rect = []
            def_value = value[0]
            option = value[2]
            input_type = value[1]
            main_detail = value[3]
            hint = value[4]
            video = value[5]
            if main_detail == MAIN or self.detail:
                if input_type == TEXTFIELD:
                    rect = ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.VerticalDivider(),
                                ft.Text(value=key),
                                ft.TextField(
                                    value=def_value,
                                    on_change=self.on_change_params,
                                    data={"key":key},
                                )
                            ]
                        ),
                        height=100,
                        on_click=self.on_click_video,
                        data={"video":ft.VideoMedia(video) if video != "None" else ft.VideoMedia("packages/data_expansion_video/none.mp4")}
                    )
                elif input_type == DROPDOWN:
                    rect = ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.VerticalDivider(),
                                ft.Text(value=key),
                                ft.Dropdown(
                                    value=def_value,
                                    options=[ft.dropdown.Option(x) for x in option],
                                    on_change=self.on_change_params,
                                    data={"key":key},
                                )
                            ]
                        ),
                        height=100,
                        on_click=self.on_click_video,
                        data={"video":ft.VideoMedia(video) if video != "None" else ft.VideoMedia("packages/data_expansion_video/none.mp4")}
                    )

            if rect != []:
                rect_list.append(rect)
        return rect_list

    def on_click_video(self,e):
        print(e.control.data["video"])

        self.video_content.content.pause()
        if e.control.data["video"] != None:
            self.video_content.content.playlist_add(e.control.data["video"])
            if 0<len(self.video_content.content.playlist):
                self.video_content.content.playlist_remove(0)
        else:
            if 0<len(self.video_content.content.playlist):
                self.video_content.content.playlist_remove(0)
            pass
        print(self.video_content.content.playlist)
            # self.video_content.content.playlist_remove()

        self.video_content.content.update()
        
    #     self.page.run_task(self.update_video)

    # async def update_video(self):
    #     await asyncio.sleep(0.2)
    #     self.update()        

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
            if type(v) == str:
                send_dict[key] = "\'"+v+"\'"
            else:
                send_dict[key] = v

        
        modelinfo.send(
            model_dict=send_dict, 
            project_path=self.page.client_storage.get("project_file_path")+"/Scripts"
        )
