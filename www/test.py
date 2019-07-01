import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='yc199510.', db='awesome')
    u = User(name='aowuchengzi', email='1533971306@qq.com', passwd='yc199510.',image='about:blank', admin=True)
    await u.save()
    ## 添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()