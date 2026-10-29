# test_db.py
# Tests the asynchronous SQLAlchemy connection to PostgreSQL by creating a table, inserting a test record, and retrieving the saved record.

import asyncio
from sqlalchemy import select
from app.database import engine, AsyncSessionLocal
from app.models import Base, FrameworkTest

# Runs the database operations asynchronously.
async def main():
    # Creates all database tables defined by the SQLAlchemy models if they do not exist.
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    # Opens an asynchronous database session for interacting with PostgreSQL.
    async with AsyncSessionLocal() as session:
        # Creates a test record with a confirmation message.
        record = FrameworkTest(
            message="SQLAlchemy connected successfully"
        )
        session.add(record)   # Adds the record to the current database session.
        await session.commit() # Saves the new record to the database.
        await session.refresh(record) # Refreshes the object to retrieve its latest database values.

        # Queries the database for the record using its primary key.
        result = await session.execute(
            select(FrameworkTest).where(
                FrameworkTest.id == record.id
            )
        )
        saved_record = result.scalar_one() # Retrieves the matching record from the query result.
        print(saved_record.message) # Prints the stored message to confirm that retrieval succeeded.

    await engine.dispose() # Closes the database engine and releases its connections.

# Runs the asynchronous test when this file is executed directly.
asyncio.run(main())