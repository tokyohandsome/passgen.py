import flet as ft
import string, secrets

def main(page: ft.Page):
    page.title = "Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width= 480
    page.window_height = 280
    page.window_resizable = False
    default_pw_len = 18
    password = "Click [Generate] button"
    
    def passgen(len_pw, punct):
        letters = string.ascii_letters
        digits = string.digits
        punctuation = punct
        while True:
            password = ''.join(secrets.choice(punctuation + letters + digits) for i in range(len_pw))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= (int(len_pw/5))
                and (punctuation == '' 
                     or sum(password.count(punctuation[c]) for c in range(len(punctuation))) >= (int(len_pw/6))
                     )
                     ):
                break
        return password

    def change_sp_char(e):
        sp_char.value = radio_sp_char.value
        page.update()    

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
    
    pw_view = ft.TextField(value=password, text_align=ft.TextAlign.LEFT, width=300)
    pw_len = ft.TextField(value=default_pw_len, input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]"), 
                          text_align=ft.TextAlign.RIGHT, width=80, on_submit=generate_password)
    sp_char = ft.TextField(value="!@$%^&*+#", text_align=ft.TextAlign.LEFT, width=290, 
                           on_submit=generate_password)
    radio_sp_char = ft.RadioGroup(value="!@$%^&*+#", content=ft.Row([
            ft.Radio(value=string.punctuation, label="All"),
            ft.Radio(value="!@$%^&*+#", label="Simple"),
            ft.Radio(value="-_", label="URL safe"),
            ft.Radio(value="none", label="None"), 
            ]), on_change=change_sp_char
            ) 
    
    page.add(
        ft.Column([
            ft.Row([
                ft.Text(value="Num of characters: "),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                pw_len,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.FloatingActionButton("Generate", on_click=generate_password, width=100)
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
            ft.Row(controls=[
                ft.Text(value="Password: "),
                pw_view,
                ft.IconButton(ft.icons.COPY, tooltip="Copy", on_click=copy_password)
                ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
            ft.Column([
                ft.Row([
                    ft.Text("Special characters: "),
                    sp_char, 
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                ft.Row(controls=[
                    radio_sp_char
                ],
                alignment=ft.MainAxisAlignment.END, width=440
            )])
        ], width = 460, alignment=ft.MainAxisAlignment.SPACE_EVENLY, 
        )
    )

ft.app(main)
