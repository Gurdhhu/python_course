import sqlite3 as sq


query = "select Users.name, Orders.id, sum(price) from Users " \
        "inner join Orders on Users.id = user_id " \
        "inner join GoodsInOrders on Orders.id = order_id " \
        "inner join Goods on Goods.id = good_id " \
        "where paid = 0 and Users.id = ? " \
        "group by Orders.id"


def unpaid(user_id):
    with sq.connect("data.sqlite") as db:
        cur = db.cursor()
        data = cur.execute(query, [user_id]).fetchall()

    return data

print(unpaid(23))