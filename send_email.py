import flet as ft
import smtplib
from email.message import EmailMessage

def main(page: ft.Page):
    page.title = "send email"

	# Function to send an email in the background
   def send_email():
	    msg = EmailMessage()
	    msg.set_content("Hello, this is a test email!")
	
	    msg['Subject'] = "Test Email"
	    msg['From'] = "your_email@example.com"
	    msg['To'] = "vzonetech800@gmail.com"
	
	    with smtplib.SMTP('smtp.gmail.com', 587) as server:
	        server.login("vzonetech800.com", "ici c'est confidentiel")
	        server.send_message(msg)
	
	
	    def on_button_click(e):
	        send_email()

    button = ft.ElevatedButton(
        text="Send Email",
        on_click=on_button_click
    )

    page.add(button)

ft.app(target=main)