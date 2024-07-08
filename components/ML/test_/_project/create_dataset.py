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

        project_info = self.page.client_storage.get("project_info")
        self.data = pd.read_csv(project_info["data_info"]["table"][0])
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
                        ft.Text(column),
                        on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                    ) for column in self.data.columns[:8]
                ],
                rows=[
                    ft.DataRow(
                        [ft.DataCell(ft.Text(cell)) for cell in self.data[column][:10]],
                    ) for column in self.data.columns[:8]
                ],
                expand=True
            ),
            expand=True
        )

        self.data_sample_content = ft.Container(
            content = ft.Column(
                controls=[
                    # DataSplit(self.page),
                    self.data_table,
                ]
            ),
            # expand=True,
            padding=ft.padding.all(value=50)
        )  


        self.content = ft.Tabs(
            tabs=[
                ft.Tab(text="データプレビュー",content=self.data_sample_content),
                ft.Tab(text="前処理",content=ft.Container(expand=True, bgcolor=ft.colors.AMBER_300)),
            ]
        )