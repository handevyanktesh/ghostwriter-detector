from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI, DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]