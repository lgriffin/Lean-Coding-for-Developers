import asyncio

class BackpressureQueue:
    def __init__(self, max_depth: int = 1000):
        self._queue: asyncio.Queue = asyncio.Queue(maxsize=max_depth)

    async def publish(self, message: dict):
        await self._queue.put(message)  # Blocks when full — backpressure

    async def consume(self) -> dict:
        return await self._queue.get()  # Blocks when empty — pull

    @property
    def pressure(self) -> float:
        return self._queue.qsize() / self._queue.maxsize
