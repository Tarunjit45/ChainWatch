import json
from pathlib import Path
from typing import Optional

from chainwatch.models import Event
from chainwatch.hashing import create_event_hash


def get_chain_path(chain_id: str) -> Path:
    """Returns the path to the chain file."""
    return Path("chains") / f"{chain_id}.jsonl"


def get_last_event(chain_id: str) -> Optional[Event]:
    """
    Retrieves the last event from a chain.

    Args:
        chain_id: The ID of the chain.

    Returns:
        The last event in the chain, or None if the chain is empty.
    """
    chain_path = get_chain_path(chain_id)
    if not chain_path.exists():
        return None

    with open(chain_path, "r") as f:
        lines = f.readlines()
        if not lines:
            return None
        last_line = lines[-1]
        return Event.model_validate_json(last_line)


def record_event(event: Event):
    """
    Records an event to the appropriate chain file.

    This function calculates the event's hash and appends the event
    to the chain file.

    Args:
        event: The event to record.
    """
    chain_path = get_chain_path(event.chain_id)
    chain_path.parent.mkdir(parents=True, exist_ok=True)

    last_event = get_last_event(event.chain_id)
    parent_hash = last_event.hash if last_event else None

    # Set the parent event if it's not already set
    if not event.parent_event and last_event:
        event.parent_event = last_event.event_id

    # Calculate and set the event's hash
    event.hash = create_event_hash(event, parent_hash)

    with open(chain_path, "a") as f:
        f.write(event.to_jsonl() + "\n")
