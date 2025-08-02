import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("SUPABASE_DB_URL")

async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)