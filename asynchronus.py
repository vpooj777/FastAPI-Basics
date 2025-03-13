from fastapi import FastAPI
import asyncio  # Used for async operations

app = FastAPI()


async def slow_function():
    await asyncio.sleep(5)  # Simulates a slow task (non-blocking)
    return {"message": "Task Complete"}


@app.get("/async/")
async def async_endpoint():
    return await slow_function()
