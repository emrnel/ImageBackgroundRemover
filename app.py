from flask import Flask, request, render_template, send_file, redirect, url_for
from rembg import remove
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('upload_form'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('upload_form'))

    if file:
        try:
            inputFile = file.read()
            outputFile = remove(inputFile)
            output = BytesIO(outputFile)
            output.seek(0)
            return send_file(output, mimetype='image/png', as_attachment=True, download_name='output.png')
        except Exception as e:
            print(f"Error: {e}")
            return redirect(url_for('upload_form'))


if __name__ == "__main__":
    app.run(debug=True)
