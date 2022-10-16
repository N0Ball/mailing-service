from flask import Flask

from flaskr.mail_conn import MAIL

app = Flask(__name__)

@app.route("/")
def test():

    try:
        mail = MAIL()
    except AttributeError as e:
        return {
            'detail': f"{e}"
        }, 500

    return {
        'detail': 'success'
    }, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')