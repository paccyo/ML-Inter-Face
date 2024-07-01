import flet as ft

class ProjectNavigationRail(ft.NavigationRail):
    def __init__(self, page:ft.Page, on_change=None):
        super().__init__()
        self.page = page
        self.on_change = on_change

        self.selected_index=0
        self.label_type=ft.NavigationRailLabelType.ALL
        self.min_width=100
        self.min_extended_width=400
        self.leading=ft.Text(value="Tasks")
        # self.leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add")
        self.group_alignment=-0.9

        self.create_dataset = ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER_OUTLINED, color=ft.colors.RED),
            selected_icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER, color=ft.colors.RED),
            label="データセット作成"
        )

        self.algorithm_select = ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.SETTINGS_OUTLINED, color=ft.colors.RED),
            selected_icon_content=ft.Icon(ft.icons.SETTINGS, color=ft.colors.RED),
            label="機械学習アルゴリズム選択",
        )

        self.model_build = ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER_OUTLINED, color=ft.colors.RED),
            selected_icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER, color=ft.colors.RED),
            label="モデル構築",
            disabled=True
        )

        self.model_compile = ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER_OUTLINED, color=ft.colors.RED),
            selected_icon_content=ft.Icon(ft.icons.CREATE_NEW_FOLDER, color=ft.colors.RED),
            label="コンパイル",
            disabled=True
        )

        self.model_train = ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.WORK_OUTLINED, color=ft.colors.RED),
            selected_icon_content=ft.Icon(ft.icons.WORK, color=ft.colors.RED),
            label="モデルの学習",
            disabled=True
        )

        self.destinations=[
            self.create_dataset,
            self.algorithm_select,
            self.model_build,
            self.model_compile,
            self.model_train,
        ]
