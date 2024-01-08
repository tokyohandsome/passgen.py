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
    
    pw_len = ft.TextField(value=default_pw_len, text_align=ft.TextAlign.RIGHT, width=100)
    pw_view = ft.TextField(value=password, text_align=ft.TextAlign.LEFT, width=300)
    #password = generate_password(pw_len.value)

    def minus_click(e):
        pw_len.value = str(int(pw_len.value) - 1)
        page.update()

    def plus_click(e):
        pw_len.value = str(int(pw_len.value) + 1)
        page.update()

    def generate_password(e):
        pw_view.value = passgen(int(pw_len.value))
        page.update()

    def copy_password(e):
        page.set_clipboard(pw_view.value)
        page.update
        
    page.add(
        ft.Column(controls=[
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
                ft.IconButton(ft.icons.COPY, on_click=copy_password)
                ],
            alignment=ft.MainAxisAlignment.CENTER,
            )
        ]
        )
    )


ft.app(target=main)