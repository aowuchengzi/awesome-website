import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='yc199510.', db='awesome')
    u = User(name='Test', email='test@qq.com', password='123456',image='about:blank')
    await u.save()
    ## 添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed