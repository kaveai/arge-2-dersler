from pydantic import BaseModel
from typing import List, Dict, Optional

# Argument Models for Queries
class Argument(BaseModel):
    body: str
    domain: str

class ArgumentResponse(BaseModel):
    body: str
    evaluation: Dict