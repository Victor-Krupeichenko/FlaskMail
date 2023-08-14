from flask import Blueprint, request, render_template, redirect, url_for
from recipient_list_file.form_upload_file import FileUploadForms
from recipient_list_file.utils import validate_file, inserting_data

recipient_router = Blueprint("recipient", __name__, template_folder="templates", static_folder="static")


@recipient_router.route('/recipient-file', methods=["GET", "POST"])
def recipient_form():
    """Рендеринг формы и получение из формы файла со списком получателей"""
    form = FileUploadForms()
    if request.method == "GET":
        return render_template("recipient_file_form.html", form=form)
    elif request.method == "POST":
        file_path = request.files.get("file")
        result = validate_file(file_path, "email", "name")
        if result:
            inserting_data(result)
    return redirect(url_for("home"))
