import os
from peewee import * # type: ignore

db = SqliteDatabase(os.getenv("DB_PATH"), pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = IntegerField(primary_key=True)
    language = TextField(default="en_en")

    def get_mention_str(self) -> str:
        """returns the user mention string <@discord_user_id>"""
        return f'<@{self.id}>'