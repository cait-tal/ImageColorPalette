from flask import Flask, render_template, url_for, flash, request, redirect
from werkzeug.utils import secure_filename
import os
import shutil
from ColorPalette import ColorPalette

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["UPLOAD_FOLDER"] = "static/temporary/"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "tga"}

# Check if submitted file is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        file = request.files["file"]
        if not os.path.exists(app.config["UPLOAD_FOLDER"]):
            os.mkdir(app.config["UPLOAD_FOLDER"])
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            file_path = f"temporary/{filename}"
            colors = ColorPalette(filepath=f'static/{file_path}')
            return render_template("index.html", image=file_path, colors=colors.hex_codes)
        else:
            flash("That is not an accepted file type.")
            return render_template("index.html", image=None, colors=None)
    try:
        shutil.rmtree(app.config["UPLOAD_FOLDER"])
    except OSError as e:
        flash("Something went wrong, please try again.")
    return render_template("index.html", image=None, colors=None)


if __name__ == '__main__':
    app.run(debug=False)




