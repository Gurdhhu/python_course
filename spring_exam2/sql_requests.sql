-- 1
select * from Users order by username;
-- 2
select * from Users order by registered desc limit 5;
-- 3
select username, count(*) from Users inner join Listened on Users.id = user_id 
group by user_id order by count(*) desc limit 5;
-- 4
select Artists.name, count(*) from Artists 
inner join Albums on Artists.id = artist_id 
group by artist_id;
-- 5
select Artists.name, count(Songs.name) from Artists 
inner join Albums on Artists.id = artist_id 
inner join Songs on Albums.id = album_id 
group by artist_id; 
-- 6
select Artists.name, Albums.name, count(Songs.id) from Artists 
inner join Albums on Artists.id = artist_id 
inner join Songs on Albums.id = album_id 
group by album_id 
order by count(Songs.id) desc limit 1;
-- 7
select Artists.name, Albums.name, total(duration) from Artists 
inner join Albums on Artists.id = artist_id 
inner join Songs on Albums.id = album_id 
group by album_id 
order by total(duration) desc limit 1;
-- 8
select Artists.name, Albums.name, 
total(duration) * 1.0 / count(Songs.id) as avg from Artists 
inner join Albums on Artists.id = artist_id 
inner join Songs on Albums.id = album_id 
group by album_id order by avg desc limit 1;
-- 9
select Artists.name, Albums.name, Songs.name, count(*) from Artists 
inner join Albums on Artists.id = artist_id 
inner join Songs on Albums.id = album_id 
inner join Listened on Songs.id = song_id 
group by song_id 
order by count(*) desc limit 5;
-- 10
select release_year, count(song_id) from Albums 
inner join Songs on album_id = Albums.id 
inner join Listened on song_id = Songs.id 
group by release_year 
order by count(song_id) desc limit 1;
-- 11
select Artists.name, Albums.name, Songs.name, start_time from Artists 
inner join Albums on Artists.id = artist_id 
inner join Songs on Albums.id = album_id 
inner join Listened on Songs.id = song_id 
inner join Users on Users.id = user_id 
where Users.id = 47 
order by start_time desc limit 20;
-- 12
select Users.username, Artists.name, Albums.name, Songs.name, count(*) from Artists 
inner join Albums on Artists.id = artist_id 
inner join Songs on Albums.id = album_id 
inner join Listened on Songs.id = song_id 
inner join Users on Users.id = user_id 
group by song_id, user_id 
order by user_id;
