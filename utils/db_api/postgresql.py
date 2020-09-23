import asyncio

import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncpg.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(user=config.PGUSER,
                                password=config.PGPASSWORD,
                                host=config.ip))

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id INT NOT NULL,
            Name varchar(255) NOT NULL,
            Talk varchar(255),
            PRIMARY KEY (id)
            );
        """
        await self.pool.execute(sql)

    async def add_user(self, id: int, name: str):
        sql = """
        INSERT INTO Users(id, Name) VALUES($1, $2)
        """
        await self.pool.execute(sql, id, name)

    async def add_talk(self, talk, id):
        sql = """
        UPDATE Users SET talk=$1 WHERE id=$2
        """
        await self.pool.execute(sql, talk, id)

    async def delete_users(self):
        await self.pool.execute("DELETE FROM Users WHERE True")
