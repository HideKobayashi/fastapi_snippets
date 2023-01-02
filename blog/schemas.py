from pydantic import BaseModel


class Blog(BaseModel):
    """ブログ登録・更新のスキーマ"""

    title: str
    body: str

    class Config:
        orm_mode = True


class ShowBlog(Blog):
    """ブログ取得のスキーマ"""


class User(BaseModel):
    """ユーザ登録・更新のスキーマ"""

    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    """ユーザ取得のスキーマ"""

    name: str
    email: str

    class Config:
        orm_mode = True
