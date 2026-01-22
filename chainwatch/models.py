from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
import datetime

class Event(BaseModel):
    """
    Represents a single step in an AI decision chain.
    """
    event_id: str = Field(..., description="Unique identifier for the event.")
    chain_id: str = Field(..., description="Identifier for the entire decision chain.")
    type: str = Field(..., description="Type of the event (e.g., 'prompt', 'tool_call', 'decision').")
    name: Optional[str] = Field(None, description="Name of the event (e.g., 'credit_checker').")
    input: Optional[Dict[str, Any]] = Field(None, description="Input to the event.")
    output: Optional[Dict[str, Any]] = Field(None, description="Output of the event.")
    timestamp: datetime.datetime = Field(..., description="Timestamp of when the event occurred.")
    parent_event: Optional[str] = Field(None, description="ID of the parent event in the chain.")
    hash: str = Field(..., description="Hash of the event content and parent hash.")

    def to_jsonl(self) -> str:
        """Serializes the event to a JSONL string."""
        return self.model_dump_json()
