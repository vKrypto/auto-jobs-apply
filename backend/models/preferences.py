from pydantic import BaseModel
from typing import List, Dict, Any

class JobFilters(BaseModel):
    location: str
    remote: bool = False
    experience_level: str = ""

class ApplicationSettings(BaseModel):
    auto_apply: bool = False
    resume_version: str = ""

class Preferences(BaseModel):
    keywords: List[str] = []
    job_filters: JobFilters
    application_settings: ApplicationSettings

    def to_dict(self):
        return {
            "keywords": self.keywords,
            "jobFilters": {
                "location": self.job_filters.location,
                "remote": self.job_filters.remote,
                "experienceLevel": self.job_filters.experience_level
            },
            "applicationSettings": {
                "autoApply": self.application_settings.auto_apply,
                "resumeVersion": self.application_settings.resume_version
            }
        }

