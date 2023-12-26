from typing import Optional

from pydantic import BaseModel


class ConfigArchitecture(BaseModel):
    architecture: Optional[str] = None
    module: Optional[str] = None
