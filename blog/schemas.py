from pydantic import BaseModel


class Blog(BaseModel):
    """ブログ登録・更新のスキーマ"""

    title: str
    body: str

    class Config:
        orm_mode = True


class ShowBlog(Blog):
    """戻り値用のスキーマ"""


class User(BaseModel):
    """ユーザ登録・更新のスキーマ"""

    name: str
    email: str
    password: str
