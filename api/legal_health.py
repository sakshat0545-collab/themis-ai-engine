from fastapi import APIRouter

from services.legal_health.schemas import (
    CompanyProfile
)

from services.legal_health.engine import (
    LegalHealthEngine
)

router = APIRouter()

engine = LegalHealthEngine()


@router.post("/legal-health")

def analyze_company(profile: CompanyProfile):

    return engine.analyze(profile)