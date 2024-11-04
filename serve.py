# from prefect.docker import DockerImage
from prefect.events import DeploymentEventTrigger

from flow import my_flow

if __name__ == "__main__":
    my_flow.serve(
        name="trace-example",
        # work_pool_name="local",
        # image=DockerImage(
        #     name="kevingrismoreprefect/trace-example",
        #     tag="latest",
        #     platform="linux/amd64",
        # ),
        triggers=[
            DeploymentEventTrigger(
                match={"prefect.resource.id":"prefect.webhook.trace-demo"},
                expect=["trace.Trigger"],
                parameters={"trace_id": "{{ event.resource.trace_id }}"},
            )
        ]
    )