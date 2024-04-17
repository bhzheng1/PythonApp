import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="FastAPI, Docker")


@app.get("/")
async def root():
    return {"message": "Hello World"}


async def main():
    config = uvicorn.Config("app.main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
