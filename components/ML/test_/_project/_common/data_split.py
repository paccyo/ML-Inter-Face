import flet as ft

class DataSplit(ft.Container):
    def __init__(self, page:ft.Page):
        self.page = page

        # self.height = 50

        self.train = ft.Container(
            bgcolor=ft.colors.ORANGE_300,
            alignment=ft.alignment.center,
            width=100,
            # expand=1,
        )
        self.test = ft.Container(
            bgcolor=ft.colors.BROWN_400,
            alignment=ft.alignment.center,
            width=100,
            # expand=1,
        )

        self.val = ft.Container(
            bgcolor=ft.colors.RED_300,
            alignment=ft.alignment.center,
            width=100,
            expand=1,
        )
        
        self.bgcolor = ft.colors.AMBER

        self.content = ft.Row(
            controls=[
                # self.train,
                # ft.GestureDetector(
                #     content=ft.VerticalDivider(),
                #     drag_interval=10,
                #     on_pan_update=self.move_vertical_divider_1,
                #     on_hover=self.show_draggable_cursor,
                # ),
                # self.test,
                # ft.GestureDetector(
                #     content=ft.VerticalDivider(),
                #     drag_interval=10,
                #     on_pan_update=self.move_vertical_divider_2,
                #     on_hover=self.show_draggable_cursor,
                # ),
                # self.val,
            ],
            spacing=0,
            width=400,
            height=400,
        )


    async def move_vertical_divider_1(self, e: ft.DragUpdateEvent):
        self.max_width = self.page.width-100
        if (e.delta_x > 0 and self.train.width < self.max_width) or (e.delta_x < 0 and self.train.width > 10):
            self.train.width += e.delta_x
        await self.train.update_async()
    
    async def move_vertical_divider_2(self, e: ft.DragUpdateEvent):
        self.max_width = self.page.width-100
        if (e.delta_x > 0 and self.train.width+self.test.width < self.max_width) or (e.delta_x < 0 and self.test.width >= 0):
            self.test.width += e.delta_x
        await self.test.update_async()


    async def show_draggable_cursor(self, e: ft.HoverEvent):
        self.max_width = self.page.width-100
        e.control.mouse_cursor = ft.MouseCursor.RESIZE_LEFT_RIGHT
        await e.control.update_async()