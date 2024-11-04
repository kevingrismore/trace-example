from prefect import flow
from prefect.events import emit_event
from prefect.client.schemas.objects import Flow, FlowRun, State

def emit_trace_event(obj: Flow, run: FlowRun, state: State) -> None:
    """
    Emit an event with the trace_id of the flow run
    """
    trace_id = run.parameters.get("trace_id")

    if not trace_id:
        raise ValueError("No trace_id provided")

    emit_event(
        event=f"trace.{state.name}",
        resource={
            f"prefect.resource.id": f"prefect.flow-run.{run.id}",
            "trace_id": trace_id,
        },
    )


@flow(
        log_prints=True,
        on_running=[emit_trace_event],
        on_completion=[emit_trace_event],
        on_failure=[emit_trace_event],
        on_cancellation=[emit_trace_event],
        on_crashed=[emit_trace_event],
)
def my_flow(trace_id: str):
    print(f"Saw trace_id: {trace_id}")

if __name__ == "__main__":
    my_flow(trace_id="abcdef12345")