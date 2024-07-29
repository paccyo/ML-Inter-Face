import flet as ft

class SplitData(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page

        self.height = 60

        async def move_left_vertical_divider(e: ft.DragUpdateEvent):
            width = self.page.width-100
            test_width = width-(self.validation_content.width+self.train_content.width)
            print(width, self.train_content.width, self.validation_content.width, test_width)
            if (e.delta_x > 0 and self.train_content.width/width < 0.9 and test_width > 250) or (e.delta_x < 0 and self.train_content.width/width > 0.1):
                self.train_content.width += e.delta_x
            self.ratio_update()
            await self.validation_content.update_async()
            await self.train_content.update_async()
        

        async def move_right_vertical_divider(e: ft.DragUpdateEvent):
            width = self.page.width-100
            test_width = width-(self.validation_content.width+self.train_content.width)
            print(width, self.train_content.width, self.validation_content.width, test_width)
            if (e.delta_x > 0 and self.validation_content.width/width < 0.9 and test_width > 250) or (e.delta_x < 0 and self.validation_content.width/width > 0.1):
                self.validation_content.width += e.delta_x
            self.ratio_update()
            await self.validation_content.update_async()
            
        

        async def show_draggable_cursor(e: ft.HoverEvent):
            e.control.mouse_cursor = ft.MouseCursor.RESIZE_LEFT_RIGHT
            await e.control.update_async()


        self.train_content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="train"),
                    ft.Text(value=""),
                ]
            ),
            bgcolor=ft.colors.BLUE,
            width=500,
        )

        self.validation_content =  ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="validation"),
                    ft.Text(value=""),
                ]
            ),
            bgcolor=ft.colors.AMBER,
            width=100,
        )

        self.test_content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="test"),
                    ft.Text(value=""),
                ]
            ),
            bgcolor=ft.colors.YELLOW,
            expand=True,
        )


        self.right_divider = ft.GestureDetector(
            content=ft.VerticalDivider(),
            drag_interval=5,
            on_pan_update=move_left_vertical_divider,
            on_hover=show_draggable_cursor
        )
        
        self.left_divider = ft.GestureDetector(
            content=ft.VerticalDivider(),
            drag_interval=5,
            on_pan_update=move_right_vertical_divider,
            on_hover=show_draggable_cursor
        )

        width = self.page.width-350
        test_width = width-(self.validation_content.width+self.train_content.width)
        self.train = int(((self.train_content.width/width)+0.06)*10)
        self.validation = int(((self.validation_content.width/width)+0.06)*10)
        self.test = 10-self.train-self.validation
        self.train_content.content.controls[1].value = self.train
        self.validation_content.content.controls[1].value = self.validation
        self.test_content.content.controls[1].value = self.test
        
        self.content = ft.Row(
            controls=[
                self.train_content,
                self.right_divider,
                self.validation_content,
                self.left_divider,
                self.test_content
            ]
        )

    def ratio_update(self):
        width = self.page.width-350
        test_width = width-(self.validation_content.width+self.train_content.width)
        self.train = int(((self.train_content.width/width)+0.06)*10)
        self.validation = int(((self.validation_content.width/width)+0.06)*10)
        self.test = 10-self.train-self.validation
        self.train_content.content.controls[1].value = self.train
        self.validation_content.content.controls[1].value = self.validation
        self.test_content.content.controls[1].value = self.test
        self.train_content.content.update()
        self.validation_content.content.update()
        self.test_content.content.update()

