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

    sender_email = "neozenith.dev@gmail.com"
    smtp_server = "localhost"
    port = 1025

    receiver_email = "neozenith.dev@gmail.com"
    message = """\
Subject: Hi there

    This message is sent from Python."""

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        if smtp_server != "localhost":
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted

            password = getpass.getpass(prompt="Type your password and press enter: ")
            server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, message)

        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    else:
        server.quit()


if __name__ == "__main__":
    main()
