import asyncio
from sqlalchemy import select
from app.database import engine, AsyncSessionLocal
from app.models import Base, FrameworkTest

async def main():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        record = FrameworkTest(
            message="SQLAlchemy connected successfully"
        )
        session.add(record)
        await session.commit()
        await session.refresh(record)

        result = await session.execute(
            select(FrameworkTest).where(
                FrameworkTest.id == record.id
            )
        )
        saved_record = result.scalar_one()
        print(saved_record.message)

    await engine.dispose()

asyncio.run(main())