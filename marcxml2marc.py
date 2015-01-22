from flask import Flask, render_template, url_for, request, send_file
from flask_bootstrap import Bootstrap
from StringIO import StringIO
from pymarc import MARCWriter, parse_xml_to_array
import os
from datetime import date

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        files = request.files.getlist('file')
        if files:
            strIO = StringIO()
            writer = MARCWriter(strIO)
            for f in files:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
                f.save(filepath)
                for record in parse_xml_to_array(filepath):
                    writer.write(record)
                os.remove(filepath)
            strIO.seek(0)
            filename = request.form['name'] if request.form['name'] else "output.mrc"
            return send_file(strIO, attachment_filename=filename, as_attachment=True)
    return render_template("upload.html", n = "etd_hua_%s.mrc" % date.today().strftime("%Y%m%d"))

