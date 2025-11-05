from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Application(BaseModel):
    application_id: str
    job_title: str
    company: str
    success: bool = False
    timestamp: Optional[datetime] = None
    cover_letter: Optional[str] = ""

    def to_dict(self):
        return {
            "applicationId": self.application_id,
            "jobTitle": self.job_title,
            "company": self.company,
            "success": self.success,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "coverLetter": self.cover_letter
        }

