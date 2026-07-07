from services.legal_health.schemas import (
    CompanyProfile,
    LegalHealthResponse
)

from services.legal_health.scorer import calculate_score


class LegalHealthEngine:

    def analyze(self, profile: CompanyProfile):

        score, issues, recommendations = calculate_score(profile)

        if score >= 80:
            risk = "Low"

        elif score >= 50:
            risk = "Medium"

        else:
            risk = "High"

        return LegalHealthResponse(

            score=score,

            compliance_percentage=score,

            risk=risk,

            issues=issues,

            recommendations=recommendations

        )