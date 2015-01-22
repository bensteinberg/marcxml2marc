marcxml2marc
============

This is a [Flask](http://flask.pocoo.org/) application for converting MARC-XML to MARC, using [pymarc](https://github.com/edsu/pymarc). 

You need virtualenv and pip, and foreman, from the [Heroku toolbelt](https://toolbelt.heroku.com/) or [otherwise](https://github.com/ddollar/foreman).
```
git clone https://github.com/bensteinberg/marcxml2marc.git
cd marcxml2marc
virtualenv-2.7 venv
source venv/bin/activate
pip install -r requirements.txt
foreman start
```
The application should now be running at http://localhost:5000/.  You can use it in a browser or on the command line, something like so:
```
curl -X POST -F "file=@/path/to/file1.xml" -F "file=@/path/to/file2.xml" http://127.0.0.1:5000/ > test.mrc
```