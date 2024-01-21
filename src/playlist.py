# import datetime
#
# from googleapiclient.discovery import build

from pytube import Playlist, YouTube
from src.video import Video
from datetime import timedelta
import os
from googleapiclient.discovery import build


class PlayList(Video):
    api_key: str = os.getenv("API_KEY")

    def __init__(self, playlist_id: str):
        # super().__init__(video_id)
        self.playlist_id = playlist_id

        self.__youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.__pl_response = self.__youtube.playlistItems().list(playlistId=self.playlist_id,
                                                             part='contentDetails').execute()
        self.__video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__pl_response['items']]
        self.__video_response = self.__youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(self.__video_ids)).execute()

        self.url = f"https://www.youtube.com/{'playlist?list='}{self.playlist_id}"

        # использование библиотеки pytube
        self.pl_obj = Playlist(self.url)
        self.title = self.pl_obj.title

        self.__total_duration = timedelta(0)

    @property
    def total_duration(self):
        for i in self.__video_response["items"]:

            videos = i["contentDetails"]["duration"]
            times = []
            str_int = ''  # строка для нового числа
            j = 0

            while j < len(videos):
                j += 1
                while j < len(videos) and '0' <= videos[j] <= '9':
                    str_int += videos[j]
                    j += 1
                if str_int != '':
                    times.append(int(str_int))
                str_int = ''

            if len(times) == 1:
                self.__total_duration += (timedelta(minutes=times[0]))
            elif len(times) == 2:
                self.__total_duration += (timedelta(minutes=times[0], seconds=times[1]))

        return self.__total_duration

    def show_best_video(self):
        best_count = 0
        best_vid = ""
        for i in self.__video_response["items"]:
            count = int(i["statistics"]["likeCount"])
            if best_count < count:
                best_count = count
                best_vid = i["id"]
        return f"https://youtu.be/{best_vid}"


