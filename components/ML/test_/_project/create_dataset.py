from packages.GenerateDataset import DatasetInfo
# from components.ML.test_._project._common.data_split import DataSplit
import flet as ft
import pandas as pd

class CreateDatasetImage(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True

        self.content = ft.Tabs(
            tabs=[
                ft.Tab(text="データプレビュー", content=self.data_sample_content),
                ft.Tab(text="前処理", content=ft.Container(expand=True, bgcolor=ft.colors.BLUE)),
            ]
        )

class CreateDatasetDataFrame(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True


        self.description = set()
        self.target = None
        self.target_content = None

        self.part_dict = {"train":7,"validation":2,"test":1}

        project_info = self.page.client_storage.get("project_info")
        self.data = pd.read_csv(project_info["data_info"]["dataframe"])
        self.data_table = ft.Container(
            content=ft.DataTable(
                border=ft.border.all(2, "black"),
                # border_radius=10,
                # vertical_lines=ft.BorderSide(1, "blue"),
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
                    ) for num in range(10)
                ],
                expand=True
            ),
            expand=True
        )

        self.create_button = ft.Container(
            content=ft.ElevatedButton(text="create_dataset",on_click=self.on_click_create_dataset),
            alignment=ft.alignment.bottom_right,
            height=50,
        )

        self.data_sample_content = ft.Container(
            content = ft.Column(
                controls=[
                    # DataSplit(self.page),
                    self.data_table,
                    self.create_button,
                ]
            ),
            # expand=True,
            padding=ft.padding.only(top=50,right=50,left=50)
        )  


        self.content = ft.Tabs(
            tabs=[
                ft.Tab(text="データプレビュー",content=self.data_sample_content),
                ft.Tab(text="前処理",content=ft.Container(expand=True, bgcolor=ft.colors.AMBER_300)),
            ]
        )


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
            

    def on_click_create_dataset(self,e):
        info = DatasetInfo()

        project_path = self.page.client_storage.get("project_file_path")

        cols_dict = {}
        cols_dict["data"] = list(self.description)
        cols_dict["target"] = [self.target]

        info.send_dataframe(
            part=self.part_dict, 
            dataframe=self.data, 
            cols_dict=cols_dict,
            project_path=project_path+"/Data", 
            data_type="dataframe", 
            shuffle=True
        )