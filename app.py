from flask import Flask, render_template, json

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
# Импортируем файл
with open("candidates.json", "rt", encoding="utf-8") as candidates:
    data = json.load(candidates)
# Начало приложения
app = Flask(__name__)
if __name__ == '__main__':
    # Главная страница выводит всех кандидатов
    @app.route("/")
    def page_index():
        all_candidates = load_candidates_from_json(data)

        return render_template('list.html', candidates=all_candidates)

    # вывод кандидата по индексу, адрес страницы соответствует id
    @app.route("/candidate/<int:x>")
    def page_candidate(x):
        candidate = get_candidate(data, x)

        return render_template('card.html', name=candidate["name"], photo=candidate["picture"],
                               position=candidate["position"], skills=candidate["skills"])

    # Вывод кандидатов по имени
    @app.route("/search/<name>")
    def page_search(name):
        name_candidates = get_candidates_by_name(data, name)

        return render_template('search.html', candidates=name_candidates, count=len(name_candidates))

    # вывод кандидата по навыкам
    @app.route("/skill/<skill_name>")
    def page_skill(skill_name):
        skill_candidates = get_candidates_by_skill(data, skill_name)

        return render_template('skill.html', candidates=skill_candidates, count=len(skill_candidates), skill=skill_name)

app.run()
