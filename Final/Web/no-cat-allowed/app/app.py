from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

def check_payload(payload):
    blacklist = [
        'cat', '__builtins__', 'exec', 'eval', 'request', 'config', 'import',
        'more', 'less', 'head', 'tail', 'nl', 'tac', 'awk', 'sed', 'grep'
    ]
    for bl in blacklist:
        if bl in payload:
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        inputstring = request.form.get('inputstring')
        if check_payload(inputstring):
            return "Not allowed."
        template = '' + inputstring + '\n\n'
        result = render_template_string(template, inputstring=inputstring)
        return result
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
