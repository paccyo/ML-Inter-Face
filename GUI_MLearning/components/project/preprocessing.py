import flet as ft
from components.util.Calldict_Preprosess import (preprocess_dicts, TEXTFIELD, DROPDOWN)

class Preprocessing(ft.Tab):
    def __init__(self, page:ft.Page, text: str | None = None, content: ft.Control | None = None, tab_content: ft.Control | None = None, icon: str | None = None, ref: ft.Ref | None = None, visible: bool | None = None, adaptive: bool | None = None):
        super().__init__(text, content, tab_content, icon, ref, visible, adaptive)
        self.page = page
        self.text="前処理"
        self.icon=ft.icons.DATASET

        preprocess_control = []
        preprocess = preprocess_dicts["ImageDataGenerator"]
        for pre, value in preprocess.items():
            # print(pre,value)
            default_value = value[0]
            control_type = value[1]
            rect = []
            if control_type == TEXTFIELD:
                rect = ft.Row(
                    controls=[
                        ft.Text(value=pre+':'),
                        ft.TextField(
                            value=default_value,
                            border="underline",
                            text_size=20
                        )
                    ]
                )
            elif control_type == DROPDOWN:
                rect = ft.Row(
                    controls=[
                        ft.Text(value=pre+':'),
                        ft.Dropdown(
                            width=100,
                            height=50,
                            text_size=10,
                            scale=1,
                            value=default_value,
                            options=[ft.dropdown.Option(str(x)) for x in value[2]]
                        )
                    ]
                )
            elif control_type == [DROPDOWN, TEXTFIELD]:
                rect = ft.Row(
                    controls=[
                        ft.Text(value='use'+pre+':'),
                        ft.Dropdown(
                            width=100,
                            height=50,
                            text_size=10,
                            scale=1,
                            value=default_value[0],
                            on_change=self.on_change_disabled,
                            options=[ft.dropdown.Option(x) for x in value[2][0]]
                        )
                    ]
                )
                rect.controls[1].data = {"pre":pre}
                preprocess_control.append(rect)
                rect = ft.Row(
                    controls=[
                        ft.Text(value=pre+':'),
                        ft.TextField(
                            value=default_value[1],
                            border="underline",
                            text_size=20,
                            disabled=True
                        )
                    ]
                )
            if rect != []:
                preprocess_control.append(rect)


        self.content=ft.Column(
            controls=preprocess_control,
            alignment=ft.alignment.top_left,
            scroll=ft.ScrollMode.HIDDEN,
            expand=True,
        )

    def on_change_disabled(self, e):
        print(e.control.value)
        if e.control.value == "True":
            for control in self.content.controls:
                print(control.controls[0].value[:-1], e.control.data["pre"])
                if control.controls[0].value[:-1] == e.control.data["pre"]:
                    print(control.controls[1].disabled)
                    control.controls[1].disabled = False
                    print(control.controls[1].disabled)
                    break
            self.content.update()
        elif e.control.value == "None":
            for control in self.content.controls:
                print(control.controls[0].value[:-1], e.control.data["pre"])
                if control.controls[0].value[:-1] == e.control.data["pre"]:
                    print(control.controls[1].disabled)
                    control.controls[1].disabled = True
                    print(control.controls[1].disabled)
                    break
            self.content.update()