import smtplib
from flaskr import config
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

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

            print(f"Connected to mail: ${config.get('GOOGLE_MAIL')}")

        except Exception as e:
            raise AttributeError(f"SMTP failed to login with error {e}")

class MAIL_CONTENT_BASE:

    def __init__(self, configs:dict) -> None:

        if not ('subject' in configs or 'to' in configs):
            raise ValueError('Error: need to set subject and who to send')
        
        self.CONTENT = MIMEMultipart()
        self.CONTENT['subject'] = configs['subject']
        self.CONTENT['from'] = config.get('GOOGLE_MAIL')
        self.CONTENT['to'] = configs['to']
        self.BASE = None

    def gen(self) -> MIMEMultipart:
        return self.CONTENT

class MAIL_CONTENT_DECORATOR:

    def __init__(self, base:MAIL_CONTENT_BASE) -> None:
        self.BASE = base
        self.CONTENT = base.CONTENT

    def gen(self):
        return self.CONTENT

class MAIL_TEXT_CONTENT(MAIL_CONTENT_DECORATOR):

    def __init__(self, base: MAIL_CONTENT_BASE, text_content:str) -> None:
        super().__init__(base)
        self.TEXT_CONTENT = text_content

    def gen(self):

        self.CONTENT.attach(MIMEText(self.TEXT_CONTENT))

        return self.BASE.gen()

class MAIL_IMAGE_CONTENT(MAIL_CONTENT_DECORATOR):

    def __init__(self, base: MAIL_CONTENT_BASE, image:bytes) -> None:
        super().__init__(base)
        self.IMAGE = image

    def gen(self):

        self.CONTENT.attach(MIMEImage(self.IMAGE))

        return self.BASE.gen()
