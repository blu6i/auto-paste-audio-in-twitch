import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
from pytube import YouTube


# Возвращает ид плейлиста
def is_get_id_playlist(url):
    query = parse_qs((urlparse(url)).query, keep_blank_values=True)
    return query['list'][0]


# Возвращает длительность клипа в минутах и секундах
def is_get_len_music(link):
    len_music = YouTube(link).length
    len_in_minuts = len_music // 60
    len_in_seconds = len_music % 60
    return [len_in_minuts, len_in_seconds]


def is_write_in_file(arr_link_music):
    print('Записываю все в файл')
    with open('music_list.txt', 'w') as file:
        for link in arr_link_music:
            file.write(link + '\n')
            # file.write('\n')


# Добавляет длительность клипов
def is_len_clip(arr_music):
    print('Вычесляю длительность клипов')
    return [is_get_len_music(link) for link in arr_music]


# Добавляет всю информацию в одну матрицу
def is_add_full_info(arr_len_music, arr_music):
    print('Формирую матрицу со всей информацией')
    return [[f'{arr_len_music[i][0]}m {arr_len_music[i][1]}s', arr_music[i]] for i in range(len(arr_len_music))]


# Вывод матрицы
def is_print_info(arr_len_music, info_bar, clips_items):
    for i in info_bar:
        print(*i)
    just_seconds = sum([sum([i[0] * 60 for i in arr_len_music]), sum([i[1] for i in arr_len_music])])
    print(f'Всего времени: {just_seconds // 60 // 60}h {just_seconds // 60 % 60}m {just_seconds % 60}s')
    print(f'Всего клипов: {len(clips_items)}')


def is_get_arr_link(playlist_items):
    arr_music = []
    count_fallse = 0
    all_count = len(playlist_items)
    seichas = 0
    for t in playlist_items:
        if YouTube(f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}').length < 600:
            arr_music.append(f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}')
        else:
            count_fallse += 1
        seichas += 1
        print(f'Удачно: {seichas-count_fallse}. Не удачно: {count_fallse}\n'
              f'Осталось:{all_count-seichas}')
    return arr_music

def main(url_playlist):
    playlist_items = []  # id клипов
    playlist_id = is_get_id_playlist(url_playlist)
    apy_key = 'AIzaSyBa6BzhpVLy4jYhaNolOPSAMXau9m0Tnao'  # Токен
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=apy_key)
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()
    # Конструктор массива со ссылками на клипы

    while request is not None:
        response = request.execute()
        playlist_items += response['items']
        request = youtube.playlistItems().list_next(request, response)
    arr_music = is_get_arr_link(playlist_items)
    # arr_music = [
    #     f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}'
    #     for t in playlist_items
    #     if YouTube(f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}').length < 600
    #
    # ]
    arr_len_music = is_len_clip(arr_music)  # Массив с длиной клипов
    info_bar = is_add_full_info(arr_len_music, arr_music)  # Массив со всей информацией
    is_print_info(arr_len_music, info_bar, arr_music)  # Вывод информации
    is_write_in_file(arr_music)  # Запись в файл


if __name__ == '__main__':
    main('https://youtube.com/playlist?list=PLgULlLHTSGIQ9BeVZY37fJP50CYc3lkW2&si=nJe7o4Hk4k2fjrhO')
