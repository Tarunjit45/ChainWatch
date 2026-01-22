from typing import Optional

from chainwatch.models import Event
from chainwatch.verifier import VerificationError


def generate_failure_report(error: VerificationError):
    """
    Generates a user-friendly failure report.

    Args:
        error: The verification error that occurred.
    """
    print("Chain Verification: ❌ FAILED")
    print(f"Reason: {error.message}")

    if error.event:
        print("\nFailure Cause:")
        print(f"The error occurred at event: {error.event.event_id}")
        print(f"Event details: {error.event.model_dump_json(indent=2)}")

        if "Hash mismatch" in error.message:
            print("\nDownstream Impact:")
            print(
                "A hash mismatch indicates that the event's content has been tampered with "
                "or corrupted. This invalidates this event and all subsequent events in the chain."
            )
        elif "Broken parent link" in error.message:
            print("\nDownstream Impact:")
            print(
                "A broken parent link means the order of the chain is compromised. "
                "The relationship between this event and the previous one is broken, "
                "making the chain's history unreliable from this point forward."
            )
        elif "Out-of-order timestamp" in error.message:
            print("\nDownstream Impact:")
            print(
                "An out-of-order timestamp suggests that events were not recorded in the "
                "correct chronological sequence. This can compromise the integrity of the "
                "entire chain's timeline."
            )
