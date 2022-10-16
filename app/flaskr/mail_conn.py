import smtplib
from flaskr import config

class MAIL:

    def __init__(self, host:str = "smtp.gmail.com", port:str = "587") -> None:

        self.SMTP = smtplib.SMTP(host=host, port=port)
        self.conn()

    def conn(self):

        if not (config.get('GOOGLE_MAIL') or config.get('GOOGLE_SECRET')):
            raise AttributeError("SMTP failed to login with error no GOOGLE_MAIL or GOOGLE_SECRET is set in environment")

        try:

            self.SMTP.ehlo()
            self.SMTP.starttls()
            self.SMTP.login(config.get('GOOGLE_MAIL'), config.get('GOOGLE_SECRET'))

            print("Connected to mail: ${config.GOOGLE_MAIL}")

        except Exception as e:
            raise AttributeError(f"SMTP failed to login with error {e}")
