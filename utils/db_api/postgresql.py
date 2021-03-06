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
            PRIMARY KEY (id)
            );
        """
        await self.pool.execute(sql)

    async def create_table_talk(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Talks (
            user_id INT NOT NULL,
            Name_talk varchar(255) NOT NULL,
            theme_1 TEXT,
            theme_2 TEXT,
            theme_3 TEXT,
            theme_4 TEXT,
            theme_5 TEXT         
            );
        """
        await self.pool.execute(sql)

    async def add_user(self, id: int, name: str):
        sql = """
        INSERT INTO Users(id, Name) VALUES($1, $2)
        """
        await self.pool.execute(sql, id, name)

    async def add_talk(self, id: int, talk_name: str):
        sql = """
        INSERT INTO Talks(user_id, Name_talk) VALUES($1, $2)
        """
        await self.pool.execute(sql, id, talk_name)

    async def choose_talk(self, id: int):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"""
                SELECT name_talk FROM talks WHERE user_id = $1
                """
        return await self.pool.fetch(sql, id)

    async def show_talk_themes(self, id: int, theme_name: str):
        sql = f"""
                SELECT theme_1, theme_2, theme_3, theme_4, theme_5 FROM talks WHERE user_id = $1 AND name_talk = $2
                """
        return await self.pool.fetch(sql, id, theme_name)
