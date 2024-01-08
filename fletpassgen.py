import flet as ft
import string, secrets

def main(page: ft.Page):
    page.title = "Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    default_pw_len = 12
    password = "Click [Generate] button"
    
    def passgen(len_pw, punctuation = string.punctuation):
        letters = string.ascii_letters
        digits = string.digits
        punctuation = punctuation
        return(''.join(secrets.choice(punctuation + letters + digits) for i in range(len_pw)))

    def change_sp_char(e):
        sp_char.value = radio_sp_char.value
        page.update()    
    
    pw_len = ft.TextField(value=default_pw_len, text_align=ft.TextAlign.RIGHT, width=100)
    pw_view = ft.TextField(value=password, text_align=ft.TextAlign.LEFT, width=300)
    sp_char = ft.TextField(value=string.punctuation, text_align=ft.TextAlign.LEFT, width=300)
    radio_sp_char = ft.RadioGroup(value=string.punctuation, content=ft.Row([
            ft.Radio(value=string.punctuation, label="All"),
            ft.Radio(value="!@$%^&*+#", label="Simple"),
            ft.Radio(value="-_", label="URL safe"),
            ft.Radio(value="none", label="None"), 
            ]), on_change=change_sp_char
            ) 

    def minus_click(e):
        pw_len.value = str(int(pw_len.value) - 1)
        page.update()

    def plus_click(e):
        pw_len.value = str(int(pw_len.value) + 1)
        page.update()

    def generate_password(e):
        if sp_char.value == "none":
            pw_view.value = passgen(int(pw_len.value), '') 
        else:
            pw_view.value = passgen(int(pw_len.value), sp_char.value)
        page.update()

    def copy_password(e):
        page.set_clipboard(pw_view.value)
        page.update



    page.add(
        ft.Column([
            ft.Row([
                ft.Text(value="Num of characters: "),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                pw_len,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.FloatingActionButton("Generate", on_click=generate_password, width=100)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(controls=[
                ft.Text(value="Password: "),
                pw_view,
                ft.IconButton(ft.icons.COPY, tooltip="Copy", on_click=copy_password)
                ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row([
                ft.Text("Special characters: "),
                sp_char,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(controls=[
                radio_sp_char
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            )
        ]
        )
    )


ft.app(target=main)