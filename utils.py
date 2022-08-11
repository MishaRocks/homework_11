def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    all_candidates = []
    for candidate in path:
        all_candidates.append([candidate['id'], candidate['name']])
    return all_candidates


def get_candidate(path, candidate_id):
    """возвращает одного кандидата по его id"""
    for candidate in path:
        if candidate_id == candidate["id"]:
            return candidate


def get_candidates_by_name(path, candidate_name):
    """возвращает кандидатов по имени"""
    name_candidates = []
    for candidate in path:
        names = candidate["name"].split()
        if candidate_name.title() in names:
            name_candidates.append([candidate['id'], candidate['name']])
    return name_candidates


def get_candidates_by_skill(path, skill_name):
    """возвращает кандидатов по навыку"""
    skills_candidates = []
    for candidate in path:
        skills = candidate["skills"].lower().split(', ')
        if skill_name.lower() in skills:
            skills_candidates.append([candidate['id'], candidate['name']])
    return skills_candidates

