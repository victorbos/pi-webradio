import vlc
from playlist import playlist

class Player:
    playing = False
    station = "Sky Radio 80's"
    stations = sorted(playlist)

    media_player = vlc.MediaPlayer()
    media_list = vlc.MediaList()
    media_list.add_media(playlist[station])

    medialist_player = vlc.MediaListPlayer()
    medialist_player.set_media_player(media_player)
    medialist_player.set_media_list(media_list)

    def start(self):
        self.playing = True
        self.medialist_player.play()

    def stop(self):
        self.playing = False
        self.medialist_player.stop()

    def get_station(self):
        return self.station

    def set_station(self, station):
        self.station = station
        self.media_list.remove_index(0)
        self.media_list.add_media(playlist[self.station])
        
        if self.playing:
            self.restart()

    def set_stream(self, stream):
        self.media_list.remove_index(0)
        self.media_list.add_media(stream)

        if self.playing:
            self.restart()

    def up(self):
        self.switch(1)

    def down(self):
        self.switch(-1)

    def switch(self, direction):
        current = self.stations.index(self.station)
        next = current + direction

        if next < 0:
            next = len(self.stations) - 1
            
        if next > len(self.stations) - 1:
            next = 0

        self.set_station(self.stations[next])

    def get_info(self):
        if self.playing:
            title = self.media_player.get_media().get_meta(vlc.Meta.Title)
            now_playing = self.media_player.get_media().get_meta(vlc.Meta.NowPlaying)
            return(title, now_playing)
        else:
            return("off", "none")

    def volume(self, volume):
        self.media_player.audio_set_volume(volume)

    def restart(self):
        self.medialist_player.stop()
        self.medialist_player.play()