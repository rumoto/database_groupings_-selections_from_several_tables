import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:********@localhost:5432/music_site')
connection = engine.connect()

# connection.execute("""create table if not exists genre (
# 		id serial primary key,
# 		name varchar(40)
# 		);
# 		create table if not exists singer (
# 		id serial primary key,
# 		name varchar(40)
# );
#
# create table if not exists singer_genre (
# 		singer_id integer references singer(id),
# 		genre_id integer references genre(id),
# 		constraint pk primary key (singer_id, genre_id)
# );
#
# create table if not exists album (
# 		id serial primary key,
# 		name varchar(40),
# 		year integer
# );
#
# create table if not exists album_singer (
# 		singer_id integer references singer(id),
# 		album_id integer references album(id),
# 		constraint pk1 primary key (singer_id, album_id)
# );
#
# create table if not exists track (
# 		id serial primary key,
# 		album_id integer references album(id),
# 		name varchar(40),
# 		duration integer
# );
#
# create table if not exists music_collection (
# 		id serial primary key,
# 		name varchar(40),
# 		year integer
# );
#
# create table if not exists track_collection (
# 		track_id integer references track(id),
# 		collection_id integer references music_collection(id),
# 		constraint pk2 primary key (track_id, collection_id)
# );
#
# """)
#
# connection.execute("""INSERT INTO genre (name)
#             VALUES ('Поп'),
#                    ('Рок'),
#                    ('Рэп'),
#                    ('Электронная музыка'),
#                    ('Шансон');""")
#
# connection.execute("""INSERT INTO singer (name)
#               VALUES ('Лолита'),
#                      ('Дискотека Авария'),
#                      ('Филипп Киркоров'),
#                      ('Нюша'),
#                      ('Любэ'),
#                      ('Дима Билан'),
#                      ('Валерия'),
#                      ('Руки Вверх');""")
#
# connection.execute("""INSERT INTO album (name, year)
#               VALUES ('Лето', 2018),
#                      ('Осень', 2019),
#                      ('Зима', 2001),
#                      ('Весна', 2009),
#                      ('Лучший альбом', 2018),
#                      ('От души', 2022),
#                      ('Альбом1', 2018),
#                      ('Альбом2', 2017);""")

# connection.execute("""INSERT INTO album_singer (singer_id, album_id)
#               VALUES (1, 1),
#                      (2, 2),
#                      (3, 3),
#                      (4, 4),
#                      (5, 5),
#                      (6, 6),
#                      (7, 7),
#                      (8, 8);""")

# connection.execute("""INSERT INTO track (album_id, name, duration)
#               VALUES (1, 'Трек1', 220),
#                      (2, 'Мой трек', 120),
#                      (3, 'My track', 300),
#                      (4, 'Мой любимый трек', 280),
#                      (5, 'Трек2', 219),
#                      (6, 'Трек3', 210),
#                      (7, 'Трек4', 260),
#                      (8, 'Трек5', 200),
#                      (1, 'Трек6', 120),
#                      (2, 'Трек7', 190),
#                      (3, 'Трек8', 230),
#                      (4, 'Самый длинный трек', 420),
#                      (5, 'Трек10', 320),
#                      (6, 'Трек11', 180),
#                      (7, 'Трек12', 170);""")
#
# connection.execute("""INSERT INTO music_collection (name, year)
#               VALUES ('Сборник1', 2018),
#                      ('Сборник2', 2019),
#                      ('Сборник3', 2001),
#                      ('Сборник4', 2009),
#                      ('Сборник5', 2020),
#                      ('Сборник6', 2022),
#                      ('Сборник7', 2018),
#                      ('Сборник8', 2017);""")
#
# connection.execute("""INSERT INTO singer_genre (singer_id, genre_id)
#               VALUES (1, 1),
#                      (1, 5),
#                      (2, 3),
#                      (3, 1),
#                      (4, 4),
#                      (5, 2),
#                      (6, 5),
#                      (7, 1),
#                      (8, 4);""")

# connection.execute("""INSERT INTO track_collection (track_id, collection_id)
#               VALUES (1, 1);""")

# sel1 = connection.execute("""SELECT name, year FROM album
#            WHERE year = 2018;
#            """).fetchall()
# print('Название и год выхода альбомов, вышедших в 2018 году: ', sel1)
#
# sel2 = connection.execute("""SELECT name, duration FROM track
#            ORDER BY duration DESC;
#            """).fetchone()
# print('название и продолжительность самого длительного трека: ', sel2)
#
# sel3 = connection.execute("""SELECT name FROM track
#            WHERE duration >= 210;
#            """).fetchall()
# print('название треков, продолжительность которых не менее 3,5 минуты: ', sel3)
#
# sel4 = connection.execute("""SELECT name FROM music_collection
#            WHERE year BETWEEN 2018 AND 2020;
#            """).fetchall()
# print('названия сборников, вышедших в период с 2018 по 2020 год включительно: ', sel4)
#
# sel5 = connection.execute("""SELECT name FROM singer
#            WHERE name NOT LIKE '%% %%';
#            """).fetchall()
# print('исполнители, чье имя состоит из 1 слова: ', sel5)
#
# sel6 = connection.execute("""SELECT name FROM track
#            WHERE name iLIKE '%%мой%%';
#            """).fetchall()
# print('название треков, которые содержат слово "мой"/"my":', sel6)



print ('1. количество исполнителей в каждом жанре:')
sel7 = connection.execute("""SELECT name, COUNT(name) FROM genre
           LEFT JOIN singer_genre ON genre.id = singer_genre.genre_id
           GROUP BY name;
           """).fetchall()
for el in sel7:
    print(el[0],el[1])

print ('2. количество треков, вошедших в альбомы 2019-2020 годов:')
sel8 = connection.execute("""SELECT count(album_id) FROM track
           LEFT JOIN album ON track.album_id = album.id
           WHERE album.year BETWEEN 2019 AND 2020;
           """).fetchall()
print(sel8)
#print('Количество треков, вошедших в альбомы 2019-2020 годов:', sel8[0][0])


print ('3. средняя продолжительность треков по каждому альбому;')
sel9 = connection.execute("""SELECT album_id, AVG(duration) FROM track
           LEFT JOIN album ON track.album_id = album.id
           GROUP BY album_id;
           """).fetchall()
print(sel9)

print ('4. все исполнители, которые не выпустили альбомы в 2020 году;')
sel10 = connection.execute("""SELECT s.name FROM singer s
            LEFT JOIN album_singer a_s ON s.id = a_s.singer_id
            LEFT JOIN album a ON a_s.album_id = a.id
            WHERE year != 2020;
            """).fetchall()
print(sel10)

print ('5. названия сборников, в которых присутствует конкретный исполнитель (выберите сами);')
sel11 = connection.execute("""SELECT mc.name FROM music_collection mc
           LEFT JOIN track_collection tc ON mc.id = tc.collection_id
           LEFT JOIN track t ON tc.track_id = t.id
           LEFT JOIN album al ON t.album_id = al.id
           LEFT JOIN album_singer a_s ON al.id = a_s.album_id
           LEFT JOIN singer s ON a_s.singer_id = s.id
           WHERE s.name = 'Лолита';
           """).fetchall()
print(sel11)

print ('6. Название альбомов, в которых присутствуют исполнители более 1 жанра;')
sel12 = connection.execute("""SELECT al.name FROM album al
            JOIN album_singer a_s ON al.id = a_s.album_id
            JOIN singer s ON a_s.singer_id = s.id
            JOIN singer_genre sg ON s.id = sg.singer_id
            JOIN genre g ON sg.genre_id = g.id
            GROUP BY al.name
            HAVING COUNT(g.name) > 1;
           """).fetchall()
print(sel12)

print ('7. Наименование треков, которые не входят в сборники;')
sel13 = connection.execute("""SELECT name FROM track
            WHERE ID NOT IN (
                SELECT DISTINCT track_id from track_collection);
           """).fetchall()
print(sel13)

print ('8. Исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);')
sel14 = connection.execute("""SELECT s.name FROM singer s
            JOIN album_singer a_s ON s.id = a_s.singer_id
            JOIN album a ON a_s.album_id = a.id
            JOIN track t ON a.id = t.album_id
            WHERE t.duration = (
                SELECT MIN(duration) FROM track);
           """).fetchall()
print(sel14)

print ('9. Название альбомов, содержащих наименьшее количество треков;')
sel14 = connection.execute("""SELECT a.name, COUNT(t.id) FROM album a
                                JOIN track t ON a.id = t.album_id
                                GROUP BY a.name
                                HAVING COUNT(t.id) = (
                                    SELECT MIN(count) FROM (
                                        SELECT a.name, COUNT(t.id) FROM album a
                                        JOIN track t ON a.id = t.album_id
                                        GROUP BY a.name) temp);""").fetchall()
print(sel14)
