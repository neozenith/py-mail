import base64
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
from string import Template


def embed_html_b64image(filename, alt_text="", encoding="image/png", style=""):
    """Embed image as base64 data in an HTML img tag"""

    with open(filename, mode="rb") as file:
        fileContent = file.read()

    b64fileContent = base64.standard_b64encode(fileContent)
    return f"<img alt='{alt_text}' style='{style}'src='data:{encoding};base64,{b64fileContent.decode()}'/>"


def main():
    print("Python Email Sender")

    host = "smtp.gmail.com"
    port = 587
    login = "neozenith.dev@gmail.com"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = "neozenith.dev@gmail.com"
    message["To"] = "neozenith.dev@gmail.com"
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    chart_embedding = embed_html_b64image("plot-red-dot.png", alt_text="6 scatterplots")
    html = Template(
        """\
    <html>
      <body>
        <p>Hi,<br>
          How are you?<br>
          <a href="http://www.realpython.com">Real Python</a>
          has many great tutorials.
          $chart
        </p>
      </body>
    </html>
    """
    ).substitute(chart=chart_embedding)

    message.attach(MIMEText(text, "plain"))
    message.attach(MIMEText(html, "html"))

    with smtplib.SMTP(host, port) as server:

        if host != "localhost":
            context = ssl.create_default_context()
            server.starttls(context=context)
            password = getpass.getpass(prompt="Type your password and press enter: ")
            server.login(login, password)

        server.sendmail(message["From"], message["To"], message.as_string())


if __name__ == "__main__":
    main()
