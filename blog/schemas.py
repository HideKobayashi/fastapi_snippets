from pydantic import BaseModel


class Blog(BaseModel):
    """レコード更新時に使うスキーマ"""

    title: str
    body: str

    class Config:
        orm_mode = True


class ShowBlog(Blog):
    """戻り値用のスキーマ"""
