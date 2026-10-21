from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class ConfigUpdateRequest(BaseModel):
    provider: Optional[str] = None
    selected_embed_model: Optional[str] = None
    selected_llm_model: Optional[str] = None
    chunk_size: Optional[int] = None
    chunk_overlap: Optional[int] = None

class IngestRequest(BaseModel):
    docs_dir: Optional[str] = "./docs"

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, description="User question or prompt")

class HealthResponse(BaseModel):
    status: str
    provider: str
    database: str