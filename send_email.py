import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import getpass
from string import Template


def main():
    print("Python Email Sender")

    host = "smtp.gmail.com"
    port = 587
    login = "neozenith.dev@gmail.com"
    attachment = "plot-red-dot.png"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = "neozenith.dev@gmail.com"
    message["To"] = "neozenith.dev@gmail.com"
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    # TODO: refactor content templating
    html = Template(
        """\
    <html>
      <body>
        <p>Hi,<br>
          How are you?<br>
          <a href="http://www.realpython.com">Real Python</a>
          has many great tutorials.
          <img src="cid:$chart" />
        </p>
      </body>
    </html>
    """
    ).substitute(chart=attachment)

    message.attach(MIMEText(text, "plain"))
    message.attach(MIMEText(html, "html"))

    with open(attachment, "rb") as fp:
        msgImage = MIMEImage(fp.read())
        msgImage.add_header("Content-ID", f"<{attachment}>")
    message.attach(msgImage)

    with smtplib.SMTP(host, port) as server:

        if host != "localhost":
            context = ssl.create_default_context()
            server.starttls(context=context)
            # login = input(f"Username for {host}:")
            password = getpass.getpass(prompt="Type your password and press enter: ")
            server.login(login, password)

        server.sendmail(message["From"], message["To"], message.as_string())


if __name__ == "__main__":
    main()
