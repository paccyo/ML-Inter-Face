from packages.GenerateDataset import DatasetInfo
from packages.util.Calldict import preprocess_dicts, DROPDOWN, DETAIL, TEXTFIELD, MAIN

from packages.preprocessing_dataframe import Preprocess
from packages.GeneratePreprocessFile import PreprocessInfo
from packages.DS import DS
from packages.open_html import view_DS

from components.ML.test_._project._common.split_data import SplitData

import flet as ft
import pandas as pd
import glob
import os
import time
import asyncio

class CreateDatasetImage(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True

        project_info = self.page.client_storage.get("project_info")
        self.sample_data = project_info["data_info"]["image"]["sample_paths"][list(project_info["data_info"]["image"]["sample_paths"].keys())[0]]

        # self.data_sample_content = ft.Container(
        #     content=ft.Container(
        #         content=ft.Image(src=self.sample_data[0],fit=ft.ImageFit.CONTAIN),
        #     )
        # )
        # self.image()

        self.data_sample_content = ft.Container(
            content=ft.Column(
                controls=[
                    SplitData(self.page),
                    ft.Divider(),
                    ft.Row(
                        controls = [
                            ft.Container(
                                content=ft.Image(src=self.sample_data[n],fit=ft.ImageFit.CONTAIN),
                                padding=ft.padding.only(left=50, top=50, right=50),
                            ) for n in range(len(self.sample_data))
                        ],
                        scroll=ft.ScrollMode.ALWAYS,
                        expand=True
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(text="create_dataset",on_click=self.on_click_create_dataset),
                        height=50,
                        alignment=ft.alignment.center_right,
                    ),
                ],
                
            ),
            expand=True,
            padding=ft.padding.only(left=50, top=10, right=50),
        )


        self.preprocess_dicts = preprocess_dicts
        self.pre_dict = dict(**self.preprocess_dicts['ImageDataGenerator'], **self.preprocess_dicts["flow_from_directory"])


        self.pre_dicts = {
            'ImageDataGenerator': {
                'featurewise_center':False,
                'samplewise_center': False,
            },
            'flow_from_directory': {
                'target_size': (256, 256),
                'color_mode': '\'rgb\''
            }
        }

        self.page.client_storage.set("color_mode", self.pre_dicts['flow_from_directory']['color_mode'].replace("\'",""))
        self.page.client_storage.set("target_size", self.pre_dicts['flow_from_directory']['target_size'])

        self.preprocess = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.VerticalDivider(),
                                ft.Text(value=pre_name),
                                ft.Dropdown(
                                    value=value[0],
                                    options=[ft.dropdown.Option(str(x)) for x in value[2]],
                                    on_change = self.on_change_value,
                                    data={"name":pre_name}
                                ) if value[1] == DROPDOWN else ft.TextField(value=value[0],on_change=self.on_change_value)
                            ]
                        ), 
                        on_click=self.on_click_preprocess, 
                        height=100, 
                        data = {"hint":value[4],"video":ft.VideoMedia(value[5]) if value[5]!="None" else ft.VideoMedia("packages/data_expansion_video/none.mp4")}
                    ) for pre_name ,value in self.pre_dict.items()
                ],
                scroll=ft.ScrollMode.HIDDEN,
            ),
            width=500,
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


        self.preprocess_content = ft.Container(
            content=ft.Row(
                controls=[
                    self.preprocess,
                    self.video_content,
                ],
                expand=True,
                
            ),
            padding=ft.padding.all(50),
            expand=True, 
            # bgcolor=ft.colors.BLUE
        )

        self.content = ft.Tabs(
            tabs=[
                ft.Tab(text="データプレビュー", content=self.data_sample_content),
                ft.Tab(text="前処理", content=ft.Container(
                    content=self.preprocess_content,
                    expand=True,
                    )
                ),
            ]
        )

    def on_change_value(self,e):
        pass

    def on_click_preprocess(self, e):
        print(e.control.data["video"])
        if e.control.data["video"] != None:
            if 0<len(self.video_content.content.playlist):
                self.video_content.content.playlist_remove(0)
            self.video_content.content.playlist_add(e.control.data["video"])
        else:
            if 0<len(self.video_content.content.playlist):
                self.video_content.content.playlist_remove(0)
            pass
        print(self.video_content.content.playlist)
            # self.video_content.content.playlist_remove()

        self.video_content.content.update()
        
        self.page.run_task(self.update_video)

    async def update_video(self):
        await asyncio.sleep(0.2)
        self.update()

    def on_click_create_dataset(self,e):
        

        project_path = self.page.client_storage.get("project_file_path")
        project_info = self.page.client_storage.get("project_info")

        data_path = project_info["data_info"]["image"]["data_path"]
        train = self.data_sample_content.content.controls[0].train
        validation = self.data_sample_content.content.controls[0].validation
        test = self.data_sample_content.content.controls[0].test
        part_dict = {"train":train, "validation":validation, "test":test}
        print(part_dict)
        self.page.client_storage.set("part_dict", part_dict)

        info = DatasetInfo()

        info.send_image(
            part=part_dict, 
            data_path=data_path,
            project_path=project_path+"/Data",
            data_type="image"
        )

        preprocess_info = PreprocessInfo(data_type="image", dataset_path=project_path+"/Data/dataset", project_path=project_path+"/Scripts")
        preprocess_info.send(self.pre_dicts)


class CreateDatasetDataFrame(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True


        self.description = set()
        self.target = None
        self.target_content = None

        self.ds = None

        self.project_info = self.page.client_storage.get("project_info")
        self.data = pd.read_csv(self.project_info["data_info"]["dataframe"])
        self.data_table = ft.Container(
            content=ft.DataTable(
                border=ft.border.all(2, "black"),
                # border_radius=10,
                vertical_lines=ft.BorderSide(1),
                # horizontal_lines=ft.BorderSide(1, "green"),
                # sort_column_index=0,
                # sort_ascending=True,
                # heading_row_color=ft.colors.BLACK12,
                # heading_row_height=100,
                # data_row_color={"hovered": "0x30FF0000"},
                # show_checkbox_column=True,
                # divider_thickness=0,
                # column_spacing=200,
                
                columns=[
                    ft.DataColumn(
                        ft.TextButton(content=ft.Container(content=ft.Text(value=column)), on_click=self.on_click_columns_button, data={"now":None,"index":i}),
                        on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                    ) for i, column in enumerate(self.data.columns[:8])
                ],
                rows=[
                    ft.DataRow(
                        [ft.DataCell(ft.Text(self.data[column][num])) for column in self.data.columns],
                    ) for num in range(8)
                ],
                expand=True
            ),
            expand=True
        )

        self.data_table = ft.Container(
            content=ft.Row(
                controls=[
                ],
                scroll=ft.ScrollMode.ALWAYS,
                expand=True
            ),
            border=ft.border.all(),
            expand=True
        )
        self.data_table.content.controls = self.data_table_update()

        self.create_button = ft.Container(
            content=ft.ElevatedButton(text="create_dataset",on_click=self.on_click_create_dataset),
            alignment=ft.alignment.center_right,
            width=200,
            height=50,
        )

        self.analyze_button = ft.Container(
            content=ft.ElevatedButton(text="data_analyze",on_click=self.on_click_data_analyze),
            alignment=ft.alignment.center,
            height=50,
            width=200,
        )

        self.analyze_view_buttons = ft.Container(
            content=ft.Row(
                controls = [],
                scroll=ft.ScrollMode.ALWAYS
            ),
            alignment=ft.alignment.center_left,
            expand=True,
            height=50,
        )

        self.buttons_content = ft.Row(
            controls=[
                self.analyze_button,
                # self.analyze_view_buttons,
                self.create_button,
            ],
            height=50,
        )

        self.data_sample_content = ft.Container(
            content = ft.Column(
                controls=[
                    SplitData(self.page),
                    ft.Divider(),
                    self.data_table,
                    self.buttons_content,
                ]
            ),
            # expand=True,
            padding=ft.padding.only(top=10,right=50,left=50),
            expand=True
        ) 

        self.fill_option = {}

        self.preprocess_content_app = ft.Container(
            content=ft.Row(
                controls=[
                    ft.VerticalDivider(),
                    ft.Text(value="カラム名", width=450),
                    ft.VerticalDivider(),
                    ft.Text(value="欠損値数", expand=True),
                    ft.VerticalDivider(),
                    ft.Text(value="欠損値補完の値",width=300),
                    ft.VerticalDivider(),
                    ft.Text(value="実行ボタン",width=80)
                ]
            ),
            height=100,
        )

        self.preprocess_content = ft.Container(
            content=ft.Column(
                controls=[]
            ),
            expand=True,
        )
        self.preprocess_content.content.controls = self.preprocess_content_update()

        self.preprocess = ft.Container(
            content=ft.Column(
                controls=[
                    self.preprocess_content_app,
                    ft.Divider(),
                    self.preprocess_content,
                ],
                scroll=ft.ScrollMode.HIDDEN,
            ),
        )

        self.content = ft.Tabs(
            tabs=[
                ft.Tab(text="データプレビュー",content=self.data_sample_content),
                ft.Tab(text="前処理",content=self.preprocess),
            ]
        )


    def data_table_update(self):
        return [ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.TextButton(
                                        content=ft.Container(
                                            content=ft.Text(value=column), 
                                            width=150, 
                                            alignment=ft.alignment.center
                                        ),
                                        on_click=self.on_click_columns_button,
                                        data={"now":None,"index":i}
                                    ),
                                alignment=ft.alignment.center)
                            ]+[
                                ft.Container(
                                    content=ft.Text(self.data[column][n]), 
                                    height=50, 
                                    alignment=ft.alignment.center, 
                                    border=ft.border.only(top=ft.BorderSide(width=1))) for n in range(10)
                            ],
                            width=200,
                        ),
                        border=ft.border.only(left=ft.BorderSide(width=1))
                    )
                    for i, column in enumerate(self.data.columns)
                ]
    
    
    def preprocess_content_update(self):
        name_width = 450
        option_width = 300
        button_width = 80
        return [ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.VerticalDivider(),
                            ft.Text(value=name,width=name_width),
                            ft.VerticalDivider(),
                            ft.Text(value="欠損値数："+str(value), expand=True),
                            ft.VerticalDivider(),
                            ft.Dropdown(
                                value=self.fill_option[name] if name in self.fill_option else None,
                                options=[ft.dropdown.Option("average"),ft.dropdown.Option("median"),],
                                on_change = self.on_change_fill_option,
                                width=option_width,
                                data={"column":name},
                            ) if _isnum else ft.Dropdown(value=self.fill_option[name] if name in self.fill_option else None, options=[], on_change = self.on_change_fill_option, width=option_width,data={"column":name}),
                            ft.VerticalDivider(),
                            ft.ElevatedButton(text="fill",on_click=self.on_click_fill_nan,data={"column":name},width=button_width)
                        ]
                    ), 
                    height=100, 
                ) for (name ,value),_isnum in zip(self.data.isnull().sum().items(), [type(x)!=str for x in [self.data[column][0] for column in self.data.columns]])
            ]


    def on_click_data_analyze(self,e):
        path = self.page.client_storage.get("project_file_path")
        path = path + "/Result"
        if self.ds == None:
            os.makedirs(name=path, exist_ok=True)
            self.ds = DS()
            self.ds.send(self.data, export_dir_result=path)
        view_DS(path+"/DS_result/AutoViz/")
        # self.analyze_view_buttons.update()



    def on_click_columns_button(self, e):
        columns_name = e.control.content.content.value

        if e.control.data["now"] == None:
            e.control.content.bgcolor = ft.colors.YELLOW
            e.control.data["now"] = "description"
            self.description.add(columns_name)

        elif e.control.data["now"] == "description":
            if self.target == None:
                pass
            else:
                self.target_content.content.bgcolor = None
                self.target_content.data["now"] = None
            e.control.content.bgcolor = ft.colors.RED
            e.control.data["now"] = "target"
            self.description.discard(columns_name)
            self.target_content = e.control
            self.target = columns_name
            
        elif e.control.data["now"] == "target":
            e.control.content.bgcolor = None
            e.control.data["now"] = None
            self.target = None

        self.update()

    def on_change_fill_option(self,e):
        self.fill_option[e.control.data["column"]] = e.control.value


    def on_click_fill_nan(self,e):
        preprocess = Preprocess(self.project_info["data_info"]["dataframe"])
        if self.fill_option[e.control.data["column"]]:
            result = preprocess.deal_null(col_name=e.control.data["column"], deal_type=self.fill_option[e.control.data["column"]])
            self.data = preprocess.MarginFrame(original=self.data, edit_part=result, target_col=e.control.data["column"])
            self.preprocess_content.content.controls = self.preprocess_content_update()
            self.preprocess_content.update()

        self.data_table.content.controls = self.data_table_update()
        self.data_table.update()



    def on_click_create_dataset(self,e):
        info = DatasetInfo()

        project_path = self.page.client_storage.get("project_file_path")

        cols_dict = {}
        cols_dict["data"] = list(self.description)
        cols_dict["target"] = [self.target]
        train = self.data_sample_content.content.controls[0].train
        validation = self.data_sample_content.content.controls[0].validation
        test = self.data_sample_content.content.controls[0].test
        part_dict = {"train":train, "validation":validation, "test":test}
        print(part_dict)
        self.page.client_storage.set("part_dict", part_dict)
        self.page.client_storage.set("target_column", self.target)
        info.send_dataframe(
            part=part_dict, 
            dataframe=self.data, 
            cols_dict=cols_dict,
            project_path=project_path+"/Data", 
            data_type="dataframe", 
            shuffle=True,
        )

