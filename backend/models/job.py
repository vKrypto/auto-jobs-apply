from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    title: str
    company: str
    location: str
    remote: bool = False
    description: Optional[str] = ""
    salary: Optional[str] = ""

    def to_dict(self):
        return {
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "remote": self.remote,
            "description": self.description,
            "salary": self.salary
        }

