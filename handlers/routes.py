from flask import render_template, request
from modules import languageL1


def configure_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if (request.method == 'POST'):
            string = request.form['string']
            language = request.form['language']
            if (language == "L1"):
                isAccepted = languageL1.get_is_accepted(string)
                detailProcess = languageL1.get_detail_process(string)
                isSend = True
                templateData = {
                    'isSend': isSend,
                    'isAccepted': isAccepted,
                    'detailProcess': detailProcess,
                    'string': string,
                    'language': language
                }
                # elif (language == "L2"):
                # elif (language == "L3"):
            return render_template('index.html', **templateData)
        else:
            return render_template('index.html')
