from app import app,db,os,secure_filename
from app.models import Noodle
from app.forms import MyForm, ItemEntry, UploadFileForm 
from flask import render_template

@app.route('/',methods=["GET", "POST"])
def home():
    items = Noodle.query.all()
    print(items)
    return render_template("index.html",items=items)

@app.route('/upload', methods=['GET',"POST"])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "Image has been uploaded"
    return render_template('upload.html', form=form)