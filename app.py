from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")
    job_description = request.form.get("job_description")

    # Check whether resume is uploaded
    if resume is None or resume.filename == "":
        return "Please upload a resume."

    # Check file type
    if not resume.filename.lower().endswith(".pdf"):
        return "Please upload only PDF files."

    # Check job description
    if not job_description or job_description.strip() == "":
        return "Please enter the job description."

    # Save the uploaded resume
    resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
    resume.save(resume_path)

    # Temporary values (we'll replace these with real analysis later)
    match_percentage = 80
    missing_skills = ["Docker", "REST API"]

    return render_template(
        "result.html",
        match_percentage=match_percentage,
        missing_skills=missing_skills
    )


if __name__ == "__main__":
    app.run(debug=True)