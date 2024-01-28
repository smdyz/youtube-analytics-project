import os
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv("API_KEY")

    def __init__(self, video_id: str):
        """
        Класс Video принимает атрибут:
        video_id: id выбранного видео с платформы YouTube

        остальные атрибуты класса:
        youtube: объект для работы с объектом YouTube API
        title: название видео
        url: ссылка на видео
        viewCount: количество просмотров видео
        likeCount: количество лайков видео
        """
        try:
            self.video_id = video_id
            self.youtube = build('youtube', 'v3', developerKey=self.api_key)
            self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=video_id).execute()
            self.title = self.video_response["items"][0]["snippet"]["title"]
            self.url = f"https://www.youtube.com/{'watch?v='}{self.video_id}"
            self.viewCount = self.video_response["items"][0]["statistics"]["viewCount"]
            self.likeCount = self.video_response["items"][0]["statistics"]["likeCount"]
        except IndexError:
            self.video_id = video_id
            self.youtube = None
            self.video_response = None
            self.title = None
            self.url = None
            self.viewCount = None
            self.likeCount = None

    def __str__(self):
        return self.title


# video1 = Video('AWX4JnAnjBE')
# print(video1.likeCount, video1.url, video1.title)
# print(json.dumps(video1.video_response, indent=2, ensure_ascii=False))


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id: str):
        """
        Класс PLVideo - дочерний класс от Video

        video_id: id выбранного видео (наследованный аргумент)
        playlist_id: id плейлиста, в котором находится данное видео
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id
