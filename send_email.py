import base64
import smtplib, ssl
import getpass


def embed_html_b64image(filename, alt_text="", encoding="image/png", style=""):
    """Embed image as base64 data in an HTML img tag"""

    with open(filename, mode="rb") as file:
        fileContent = file.read()

    b64fileContent = base64.standard_b64encode(fileContent)
    return f"<img alt='{alt_text}' style='{style}'src='data:{encoding};base64,{b64fileContent.decode()}'/>"


def main():
    print("Welcome")

    login_user = "neozenith.dev@gmail.com"

    smtp_host = "smtp.gmail.com"
    port = 465  # For SSL
    password = getpass.getpass(prompt="Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_host, port, context=context) as server:
        server.login(login_user, password)


if __name__ == "__main__":
    main()
