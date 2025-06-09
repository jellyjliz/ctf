from flask import Flask, request, session, redirect, send_file
import random
from ctf_questions import QUESTIONS

app = Flask(__name__)
app.secret_key = "ctf_secret_key"

LEVELS = ["easy", "medium", "hard"]

def get_next_questions(level):
    used_ids = session.get("used", {}).get(level, [])
    available = [q for q in QUESTIONS[level] if q["id"] not in used_ids]
    return random.sample(available, min(3, len(available)))

@app.route("/")
def index():
    session.clear()
    session["used"] = {}
    session["solved"] = {}
    return send_file("index.html")

@app.route("/level/<level>", methods=["GET", "POST"])
def level(level):
    if level not in LEVELS:
        return redirect("/")

    if request.method == "POST":
        correct_answers = 0
        for qid in request.form:
            answer = request.form[qid].strip()
            for q in QUESTIONS[level]:
                if q["id"] == qid and answer.lower() == q["answer"].lower():
                    correct_answers += 1
                    session["used"].setdefault(level, []).append(qid)
        session["solved"][level] = session["solved"].get(level, 0) + correct_answers

        if session["solved"][level] >= 3:
            next_level_index = LEVELS.index(level) + 1
            if next_level_index < len(LEVELS):
                return redirect(f"/level/{LEVELS[next_level_index]}")
            else:
                return redirect("/win")

    questions = get_next_questions(level)
    html = open("level.html").read()
    question_html = ""
    for q in questions:
        question_html += f"<p><b>{q['id']}</b>: {q['question']}<br><input name='{q['id']}' required></p>"
    html = html.replace("{{level}}", level.title()).replace("{{questions}}", question_html)
    return html

@app.route("/win")
def win():
    return send_file("win.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
