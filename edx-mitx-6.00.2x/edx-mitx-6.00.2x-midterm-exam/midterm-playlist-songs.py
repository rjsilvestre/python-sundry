def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    avail_size = max_size
    if songs[0][2] <= avail_size:
        avail_size -= songs[0][2]
        playlist.append(songs[0][0])
    else:
        return playlist
    sorted_songs = sorted(songs[1:], key=lambda song: song[2])
    for song in sorted_songs:
        if song[2] <= avail_size and song[0] not in playlist:
            playlist.append(song[0])
            avail_size -= song[2]
    return playlist

# Test cases
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
print(song_playlist(songs, 12))    # ['Roar', 'Wannabe']
print(song_playlist(songs, 13))    # ['Roar', 'Wannabe', 'Timber']
