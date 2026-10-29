import asyncio
from sqlalchemy import text
from app.database import engine

async def main():
    async with engine.connect() as connection:
        result = await connection.execute(text("SELECT version()"))
        print(result.scalar())

    await engine.dispose()

asyncio.run(main())