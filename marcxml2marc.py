from flask import Flask, render_template, url_for, request, send_file
from flask_bootstrap import Bootstrap
from StringIO import StringIO
from pymarc import MARCWriter, parse_xml_to_array
from os import remove
from datetime import date
from tempfile import mkstemp

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        files = request.files.getlist('file')
        if files:
            strIO = StringIO()
            writer = MARCWriter(strIO)
            for f in files:
                (handle, filepath) = mkstemp()
                f.save(filepath)
                for record in parse_xml_to_array(filepath):
                    writer.write(record)
                remove(filepath)
            strIO.seek(0)
            try:
                filename = request.form['name']
            except:
                filename = "output.mrc"
            return send_file(strIO, attachment_filename=filename, as_attachment=True)
    return render_template("upload.html", n = "etd_hua_%s.mrc" % date.today().strftime("%Y%m%d"))

