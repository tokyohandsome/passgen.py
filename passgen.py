import flet as ft
import string, secrets

def main(page: ft.Page):
    page.title = "Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.TextField(
            label="Password with reveal button", password=True, can_reveal_password=True
            )
        )

ft.app(target=main, view=ft.WEB_BROWSER)
