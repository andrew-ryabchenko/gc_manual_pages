from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('./index.html')

@application.route('/btm-installation-manual')
def btm_installation_manual():
    return render_template('./btm-installation-manual.html')

@application.route('/manuals/<kiosk>')
def manuals(kiosk):
    return render_template(f'./{kiosk}-manual.html')

application.run(debug=True)