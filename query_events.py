import asyncio

from prefect.events import get_events_subscriber, ResourceSpecification
from prefect.events.filters import EventFilter, EventResourceFilter


async def query_events(trace_id: str):
    filter = EventFilter(
        resource=EventResourceFilter(
            labels=ResourceSpecification({"trace_id": "*"})
        )
    )
    async with get_events_subscriber(filter=filter) as subscriber:
        async for event in subscriber:
            print(event)



if __name__=="__main__":
    asyncio.run(query_events("testid123"))