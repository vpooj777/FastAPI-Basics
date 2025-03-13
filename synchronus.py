from fastapi import FastAPI
import time

app = FastAPI()


def slow_function():
    time.sleep(5)  # Simulates a slow task (blocking)
    return {"message": "Task Complete"}


@app.get("/sync/")
def sync_endpoint():
    return slow_function()
