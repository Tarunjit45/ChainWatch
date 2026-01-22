import typer
from typing_extensions import Annotated
import json
from pathlib import Path
import datetime

from chainwatch.models import Event
from chainwatch.recorder import record_event
from chainwatch.verifier import verify_chain, VerificationError
from chainwatch.replay import replay_chain
from chainwatch.report import generate_failure_report

app = typer.Typer()


@app.command()
def record(
    event_file: Annotated[
        Path,
        typer.Argument(
            ...,
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ]
):
    """
    Records an event from a JSON file.
    """
    try:
        with open(event_file, "r") as f:
            event_data = json.load(f)

        # Add a timestamp if it's not present
        if "timestamp" not in event_data:
            event_data["timestamp"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        else:
            # Ensure the timestamp is in the correct format
            event_data["timestamp"] = datetime.datetime.fromisoformat(event_data["timestamp"]).isoformat()


        # A hash will be calculated and added by the recorder, so we can add a placeholder
        if "hash" not in event_data:
            event_data["hash"] = ""

        event = Event.model_validate(event_data)
        record_event(event)
        print(f"Event '{event.event_id}' recorded in chain '{event.chain_id}'.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file: {event_file}")
        raise typer.Exit(code=1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise typer.Exit(code=1)


@app.command()
def verify(chain_id: str):
    """
    Verifies the integrity of a decision chain.
    """
    try:
        verify_chain(chain_id)
        print("Chain Verification: ✅ PASSED")
    except VerificationError as e:
        generate_failure_report(e)
        raise typer.Exit(code=1)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise typer.Exit(code=1)


@app.command()
def replay(chain_id: str):
    """
    Replays a decision chain step-by-step.
    """
    try:
        replay_chain(chain_id)
    except VerificationError as e:
        print("Chain is invalid and cannot be replayed.")
        generate_failure_report(e)
        raise typer.Exit(code=1)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
