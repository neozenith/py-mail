import base64
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
from string import Template

server = {"host": "localhost", "port": 1025, "login": "neozenith.dev@gmail.com"}

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = "neozenith.dev@gmail.com"
message["To"] = "neozenith.dev@gmail.com"
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a>
       has many great tutorials.
       $(chart)
    </p>
  </body>
</html>
"""

message.attach(MIMEText(text, "plain"))
message.attach(MIMEText(html, "html"))


def embed_html_b64image(filename, alt_text="", encoding="image/png", style=""):
    """Embed image as base64 data in an HTML img tag"""

    with open(filename, mode="rb") as file:
        fileContent = file.read()

    b64fileContent = base64.standard_b64encode(fileContent)
    return f"<img alt='{alt_text}' style='{style}'src='data:{encoding};base64,{b64fileContent.decode()}'/>"


def connect_email_server(host, port, user="", password=None):
    # Create a secure SSL context
    context = ssl.create_default_context()

    email_server = smtplib.SMTP(host, port)
    email_server.ehlo()  # Can be omitted
    if server["host"] != "localhost":
        email_server.starttls(context=context)  # Secure the connection
        email_server.ehlo()  # Can be omitted

        password = getpass.getpass(prompt="Type your password and press enter: ")
        email_server.login(user, password)

    return email_server


def main():
    print("Welcome")

    email_server = connect_email_server(server["host"], server["port"], server["login"])

    if email_server:
        email_server.sendmail(message["From"], message["To"], message.as_string())

        email_server.quit()


if __name__ == "__main__":
    main()
