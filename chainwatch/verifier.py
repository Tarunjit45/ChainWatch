from typing import List, Optional

from chainwatch.models import Event
from chainwatch.recorder import get_chain_path
from chainwatch.hashing import create_event_hash


class VerificationError(Exception):
    """Custom exception for verification failures."""

    def __init__(self, message: str, event: Optional[Event] = None):
        self.message = message
        self.event = event
        super().__init__(self.message)


def load_chain(chain_id: str) -> List[Event]:
    """
    Loads all events from a chain file.

    Args:
        chain_id: The ID of the chain.

    Returns:
        A list of events in the chain.
    """
    chain_path = get_chain_path(chain_id)
    if not chain_path.exists():
        raise FileNotFoundError(f"Chain '{chain_id}' not found.")

    with open(chain_path, "r") as f:
        lines = f.readlines()

    return [Event.model_validate_json(line) for line in lines]


def verify_chain(chain_id: str):
    """
    Verifies the integrity of a decision chain.

    This function checks for:
    - Missing events
    - Broken parent-child links
    - Hash mismatches
    - Out-of-order timestamps

    Args:
        chain_id: The ID of the chain to verify.

    Raises:
        VerificationError: If the chain is invalid.
    """
    try:
        events = load_chain(chain_id)
    except FileNotFoundError as e:
        raise VerificationError(str(e)) from e

    if not events:
        return  # An empty chain is considered valid

    parent_hash: Optional[str] = None
    last_event: Optional[Event] = None

    for i, event in enumerate(events):
        # Check for broken parent-child links
        if i == 0:
            if event.parent_event is not None:
                raise VerificationError("First event in the chain should not have a parent.", event)
        else:
            if event.parent_event != last_event.event_id:
                raise VerificationError(
                    f"Broken parent link. Event '{event.event_id}' should have parent "
                    f"'{last_event.event_id}', but has '{event.parent_event}'.",
                    event,
                )

        # Check for out-of-order timestamps
        if last_event and event.timestamp < last_event.timestamp:
            raise VerificationError(
                f"Out-of-order timestamp. Event '{event.event_id}' has a timestamp "
                f"earlier than its parent '{last_event.event_id}'.",
                event,
            )

        # Check for hash mismatches
        expected_hash = create_event_hash(event, parent_hash)
        if event.hash != expected_hash:
            raise VerificationError(
                f"Hash mismatch at event '{event.event_id}'. "
                f"Expected '{expected_hash}', but found '{event.hash}'.",
                event,
            )

        parent_hash = event.hash
        last_event = event
