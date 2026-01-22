import hashlib
import json
from typing import Dict, Any, Optional

from chainwatch.models import Event


def calculate_hash(event_data: Dict[str, Any], parent_hash: Optional[str]) -> str:
    """
    Calculates the SHA256 hash of an event's data and its parent's hash.

    Args:
        event_data: The event data to hash (excluding the 'hash' field itself).
        parent_hash: The hash of the parent event.

    Returns:
        The calculated SHA256 hash as a hex digest.
    """
    # Create a dictionary with the event data and parent hash
    hash_payload = {
        "data": event_data,
        "parent_hash": parent_hash,
    }

    # Sort the keys to ensure a consistent hash
    encoded_payload = json.dumps(hash_payload, sort_keys=True).encode("utf-8")

    return hashlib.sha256(encoded_payload).hexdigest()


def create_event_hash(event: Event, parent_hash: Optional[str]) -> str:
    """
    Creates a hash for a given event.

    This function takes an Event object, removes the existing hash,
    and calculates a new hash based on the event's content and the
    parent's hash.

    Args:
        event: The event to hash.
        parent_hash: The hash of the parent event.

    Returns:
        The new hash for the event.
    """
    # Exclude the hash field from the event data for hashing
    event_dict = event.model_dump(exclude={"hash"})
    # The timestamp is a datetime object, so we need to convert it to a string
    event_dict["timestamp"] = event.timestamp.isoformat()

    return calculate_hash(event_dict, parent_hash)
