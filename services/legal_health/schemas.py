from pydantic import BaseModel
from typing import List


class CompanyProfile(BaseModel):

    company_name: str

    gst_registered: bool

    trademark_registered: bool

    founder_agreement: bool

    privacy_policy: bool

    employee_count: int


class LegalHealthResponse(BaseModel):

    score: int

    compliance_percentage: int

    risk: str

    issues: List[str]

    recommendations: List[str]