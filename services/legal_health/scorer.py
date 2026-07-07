from services.legal_health.rules import LEGAL_RULES


def calculate_score(profile):

    score = 100

    issues = []

    recommendations = []

    for field, rule in LEGAL_RULES.items():

        if not getattr(profile, field):

            score -= rule["penalty"]

            issues.append(rule["issue"])

            recommendations.append(rule["recommendation"])

    score = max(score, 0)

    return score, issues, recommendations