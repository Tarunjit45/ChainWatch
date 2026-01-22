
from typing import List

from chainwatch.models import Event
from chainwatch.verifier import load_chain, VerificationError


def replay_chain(chain_id: str):
    """
    Replays a decision chain step-by-step.

    Args:
        chain_id: The ID of the chain to replay.

    Raises:
        VerificationError: If the chain is invalid.
    """
    try:
        events = load_chain(chain_id)
    except FileNotFoundError as e:
        raise VerificationError(str(e)) from e

    if not events:
        print("Chain is empty.")
        return

    for i, event in enumerate(events):
        print(f"Step {i + 1}: {event.type} - {event.name or 'N/A'}")
        if event.input:
            print(f"  Input: {event.input}")
        if event.output:
            print(f"  Output: {event.output}")
