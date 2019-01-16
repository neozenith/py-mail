# 🐍 py-mail

Simple script to get richly formatted emails working

Following this article on [Real Python](https://realpython.com).

[https://realpython.com/python-send-email/ ](https://realpython.com/python-send-email/)

As well as this trick to embed images.

```html
<img alt="Embedded Image" width="158" height="158" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJ4A..." />
```

# Getting Started

Start local debugging server

If using a GMail account for testing follow this link [https://myaccount.google.com/lesssecureapps?pli=1](https://myaccount.google.com/lesssecureapps?pli=1)

```bash
python -m smtpd -c DebuggingServer -n localhost:1025
```


```bash
python mail.py
```
