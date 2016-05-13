-- 1.
select * from Users;
-- 2.
select count(*) from Users;
-- 3.
select count(*) from Users where birth_date >= date("1976-05-12");
-- 4.
select country, count(*) from Users group by country;
-- 5.
select name, count(*) as num from users group by name having num > 1;
-- 6.
select count(*) from Orders where created >= date("2016-01-01") and created < date("2017-01-01");
-- 7.
select date(created), count(*) as num from Orders 
group by date(created) 
order by num desc limit 1;
-- 8.
select 100 - sum(paid) * 100.0 / count(*) from Orders;
-- 9.
select * from Goods where name like "%bread%";
-- 10. 
select id, name, count(*) as num from GoodsInOrders 
inner join Goods on id = good_id 
group by good_id 
order by num desc limit 10;
-- 11.
select sum(price) from Goods 
inner join GoodsInOrders on Goods.id = good_id 
inner join Orders on Orders.id = order_id 
where paid = 1;
-- 12.
select Goods.id, Goods.name from Goods 
inner join GoodsInOrders on Goods.id = good_id 
inner join Orders on order_id = Orders.id 
inner join Users on Users.id = user_id 
where gender = "F" 
group by Goods.name 
order by count(*) desc 
limit 10;
-- 13.
select Users.id, Users.name from Users 
inner join Orders on Users.id = user_id 
inner join GoodsInOrders on Orders.id = order_id 
inner join Goods on Goods.id = good_id 
where units = "KG" 
group by user_id 
order by sum(quantity) 
desc limit 1;








