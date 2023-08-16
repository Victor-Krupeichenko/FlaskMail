import os
from flask import Blueprint, render_template, request, redirect, url_for, send_file
from report.forms import ReportForm
from report.utils import get_report_recipient, create_pdf_report

report = Blueprint("report", __name__, template_folder="templates", static_folder="static")

_SAVE_PATH_FILE = "report"
_FILE_NAME = "recipient_list.pdf"


@report.route("/report", methods=["GET", "POST"])
def report_recipient():
    """Получает данные о конкретном получателе"""
    form = ReportForm()
    if request.method == "GET":
        return render_template("report_to_recipient.html", form=form)
    if form.validate_on_submit():
        name = form.data.get("report")
        recipients = get_report_recipient(name)
        create_pdf_report(recipients, save_folder_file=_SAVE_PATH_FILE, file_name=_FILE_NAME)
        return render_template("report_to_recipient.html", form=form, recipients=recipients)
    return redirect(url_for("home"))


@report.route("/download_report", methods=["GET"])
def download_report():
    """Скачать файл report"""
    pdf_path = os.path.join(_SAVE_PATH_FILE, _FILE_NAME)
    return send_file(pdf_path, as_attachment=True)
