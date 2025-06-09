from flask import Flask, render_template, request, redirect, session
import random
from ctf_questions import QUESTIONS

app = Flask(__name__)
app.secret_key = "ctf_secret_key"

LEVELS = ["easy", "medium", "hard"]
GLOBAL_USED = {level: set() for level in LEVELS}

@app.route("/")
def index():
    session.clear()
    return render_template("index.html", levels=LEVELS)

@app.route("/select/<level>", methods=["GET", "POST"])
def select_questions(level):
    if level not in LEVELS:
        return redirect("/")

    used_ids = GLOBAL_USED[level]
    available = [q for q in QUESTIONS[level] if q["id"] not in used_ids]
    choices = [q["id"] for q in available]

    if request.method == "POST":
        selected = request.form.getlist("questions")
        if len(selected) != 3:
            return render_template("select.html", level=level, choices=choices, error="Select exactly 3 questions.")
        session.setdefault("selected", {})[level] = selected
        for qid in selected:
            GLOBAL_USED[level].add(qid)
        return redirect(f"/level/{level}")

    return render_template("select.html", level=level, choices=choices, error=None)

@app.route("/level/<level>", methods=["GET", "POST"])
def level(level):
    if level not in LEVELS or "selected" not in session or level not in session["selected"]:
        return redirect("/")

    selected_ids = session["selected"][level]
    questions = [q for q in QUESTIONS[level] if q["id"] in selected_ids]
    correct = 0

    if request.method == "POST":
        for q in questions:
            answer = request.form.get(q["id"], "").strip().lower()
            if answer == q["answer"].lower():
                correct += 1
        if correct >= 3:
            next_index = LEVELS.index(level) + 1
            if next_index < len(LEVELS):
                return redirect(f"/select/{LEVELS[next_index]}")
            else:
                return redirect("/win")
        return render_template("level.html", level=level, questions=questions, error="You must answer at least 3 correctly.")

    return render_template("level.html", level=level, questions=questions, error=None)

@app.route("/win")
def win():
    return render_template("win.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
