class Song:
    def __init__(self, name, artist, album, position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = year
        self.duration = duration

    def __repr__(self):
        return 'Song \"%s\" by %s from album \"%s\" %i (track %s, %i s)' % (self.name, self.artist, self.album,
                                                                            self.year, self.position, self.duration)

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False


def import_songs(file_name):
    songlist = []
    with open(file_name, "r", encoding='utf8') as input_file:
        lines = input_file.readlines()
        for line in lines:
            attr = (line.split('\t'))
            songlist.append(Song(attr[0], attr[1], attr[2], attr[3], int(attr[4]), int(attr[5])))
    return songlist


def export_songs(songs, file_names):
    with open(file_names, 'w') as output_file:
        songs_output = ''
        for i in songs:
            songs_output += '\t'.join([i.name, i.artist, i.album, str(i.year), i.position, str(i.duration), '\n'])
        output_file.write(songs_output)


def shuffle_songs(songs):
    from random import shuffle
    return shuffle(songs)


songs = import_songs('songs1.txt')

# part1: the most frequent artists
artists_lib = {}
for song in songs:
    if song.artist not in artists_lib:
        artists_lib[song.artist] = 1
    else:
        artists_lib[song.artist] += 1
artists_freq = ['', 0]
for key in artists_lib:
    if artists_lib[key] > artists_freq[1]:
        artists_freq = [key, artists_lib[key]]
print(artists_freq[0])

# part2: the longest song
duration_lib = {}
for song in songs:
    duration_lib[song.name+';'+song.artist] = song.duration
duration_max = ['', 0]
for key in duration_lib:
    if duration_lib[key] > duration_max[1]:
        duration_max = [key, duration_lib[key]]
print('\t'.join(duration_max[0].split(';')))

# part3: the longest album
albums_lib = {}
for song in songs:
    if song.album+';'+song.artist not in albums_lib:
        albums_lib[song.album+';'+song.artist] = song.duration
    else:
        albums_lib[song.album+';'+song.artist] += song.duration
album_longest = ['', 0]
for key in albums_lib:
    if albums_lib[key] > album_longest[1]:
        album_longest = [key, albums_lib[key]]
print('\t'.join(album_longest[0].split(';')))


# part4: ten words. Эпопея начинается
# Сортировка по принципу "разделяй и властвуй"
def MergeLists(A, B):
    C = []
    count1 = 0
    count2 = 0
    while count1 < len(A) and count2 < len(B):
        tmp = A[count1]
        if A[count1][1] < B[count2][1]:
            tmp = B[count2]
            count2 += 1
        else:
            count1 += 1
        C.append(tmp)
    if len(B) > count2:
        C.extend(B[count2:])
    elif len(A) > count1:
        C.extend(A[count1:])
    return C


def MergeSortList(A):
    if len(A) <= 1:
        return A
    A[:int(len(A)/2)] = MergeSortList(A[:int(len(A)/2)])
    A[int(len(A)/2):] = MergeSortList(A[int(len(A)/2):])
    A = MergeLists(A[:int(len(A)/2)], A[int(len(A)/2):])
    return A


# Приведение слов в нужный формат
def filtration(x):
    outstring = []
    for i in x.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz ':
            outstring.append(i)
        else:
            outstring.append(' ')
    return((''.join(outstring)).split())

# Подсчет слов
words_lib = {}
for song in songs:
    for word in filtration(song.name):
        if word not in words_lib:
            words_lib[word] = 1
        else:
            words_lib[word] += 1

# Превращение в список, чтобы можно было отсортировать
words_list = []
for key in words_lib:
    words_list.append([key, words_lib[key]])

# Наконец, сортировка
out = []
if len(words_list) <= 10:
    for i in MergeSortList(words_list):
        out.append(i[0])
    print('\t'.join(out))
else:
    for i in MergeSortList(words_list)[:10]:
        out.append(i[0])
    print('\t'.join(out))

# Task5: the artist of many albums
artalb_lib = {}
for song in songs:
    if song.artist not in artalb_lib:
        artalb_lib[song.artist] = [song.album]
    else:
        if song.album not in artalb_lib[song.artist]:
            artalb_lib[song.artist].append(song.album)
art_max = ['', 0]
for key in artalb_lib:
    if len(artalb_lib[key]) > art_max[1]:
        art_max = [key, len(artalb_lib[key])]
print(art_max[0])
