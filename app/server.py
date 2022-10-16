from flask import Flask, request

from flaskr import mail
from flaskr.mail_conn import MAIL_CONTENT_BASE, MAIL_TEXT_CONTENT

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_message():

    try:
        
        if not (request.form.get('subject') or request.form.get('to')):
            return {
                'detail': 'Error, `subject` and `to` field are required'
            }, 400

        mime_content = MAIL_CONTENT_BASE(request.values)
        mime_content = MAIL_TEXT_CONTENT(mime_content, request.form.get('content') or 'Test Content')
        mime = mime_content.gen()

        mail.SMTP.send_message(mime)

    except ValueError as e:
        return {
            'detail': e
        }, 500

    return {
        'detail': f'success send to {request.form.get("to")} with content {request.form.get("content") or "Test Content"}'
    }, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')