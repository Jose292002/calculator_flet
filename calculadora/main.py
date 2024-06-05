import flet as ft


def main(page: ft.Page):
    page.window_height=460
    page.window_width=300
    page.bgcolor = ft.colors.ON_PRIMARY
    page.window_resizable = False
    page.window_maximizable = False
    page.title = "Calculator"


    def get_data(e):
        data = e.control.data
        
        if data == "=":
            try:
                text.value = str(eval(text.value))
            except Exception as e:
                text.value = "ERROR"
        elif data == "C":
            text.value = ""
        elif data == "AC":
            text.value = text.value[:-1] if text.value else text.value
        elif data == "%":
            try:
                text.value == str(float(text.value)/100)
            except ValueError:
                text.value = "ERROR"
        elif data == ".":
            if not text.value or text.value[:-1] not in [".", "+", "-", "*", "/"]:
                text.value += data
        elif data == "±":
            text.value = "-" + text.value if text.value and text.value[0] != "-" else text.value[:-1]
        elif data in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "/", "*"]:
            text.value +=data
        
        page.update()

    text = ft.TextField(read_only=True, border_color=ft.colors.WHITE, text_align="right",
                        text_style=ft.TextStyle(size=30, color=ft.colors.WHITE))

    page.add(text)

    page.add(
        ft.Row([
            ft.ElevatedButton(text="1", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="1", on_click=get_data),
            ft.ElevatedButton(text="2", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="2", on_click=get_data),
            ft.ElevatedButton(text="3", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="3", on_click=get_data),
            ft.ElevatedButton(text="+", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="+", on_click=get_data),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),


         ft.Row([
            ft.ElevatedButton(text="4", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="4", on_click=get_data),
            ft.ElevatedButton(text="5", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="5", on_click=get_data),
            ft.ElevatedButton(text="6", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="6", on_click=get_data),
            ft.ElevatedButton(text="-", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="-", on_click=get_data),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),


         ft.Row([
            ft.ElevatedButton(text="7", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="7", on_click=get_data),
            ft.ElevatedButton(text="8", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="8", on_click=get_data),
            ft.ElevatedButton(text="9", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="9", on_click=get_data),
            ft.ElevatedButton(text="x", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="*", on_click=get_data),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),


         ft.Row([
            ft.ElevatedButton(text=".", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data=".", on_click=get_data),
            ft.ElevatedButton(text="0", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="0", on_click=get_data),
            ft.ElevatedButton(text="%", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="%", on_click=get_data),
            ft.ElevatedButton(text="÷", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="/", on_click=get_data),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),


         ft.Row([
            ft.ElevatedButton(text="C", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="C", on_click=get_data),
            ft.ElevatedButton(text="⌫", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="⌫", on_click=get_data),
            ft.ElevatedButton(text="±", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="±", on_click=get_data),
            ft.ElevatedButton(text="=", bgcolor=ft.colors.TRANSPARENT, color=ft.colors.WHITE,
                              style= ft.ButtonStyle(shape=ft.CircleBorder(), padding=25,
                                                    shadow_color=ft.colors.BLUE, side=ft.BorderSide(width=2, color=ft.colors.BLUE)),
                                                    elevation=5, data="=", on_click=get_data),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
    )


ft.app(target=main)
