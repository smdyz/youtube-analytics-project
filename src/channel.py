import json
import requests
import os
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv("API_KEY")
    __youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        __youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = __youtube.channels().list(id=self.__channel_id, part='snippet, statistics').execute()

        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.sub_quantity = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"])
        self.channel_views = int(self.channel["items"][0]["statistics"]["viewCount"])

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.sub_quantity + other.sub_quantity

    def __sub__(self, other):
        return self.sub_quantity - other.sub_quantity

    def __eq__(self, other):
        if self.sub_quantity == other.sub_quantity:
            return True
        return False

    def __lt__(self, other):
        if self.sub_quantity < other.sub_quantity:
            return True
        return False

    def __le__(self, other):
        if self.sub_quantity <= other.sub_quantity:
            return True
        return False

    def __gt__(self, other):
        if self.sub_quantity > other.sub_quantity:
            return True
        return False

    def __ge__(self, other):
        if self.sub_quantity >= other.sub_quantity:
            return True
        return False

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.__youtube

    def to_json(self, path):
        flag = True
        info = {'channel_id': self.__channel_id, 'title': self.title,
                'description': self.description, 'url': self.url, 'sub_quantity': self.sub_quantity,
                'video_count': self.video_count, 'channel_views': self.channel_views}
        with open(path, 'r') as f:
            if f == '':
                f.close()
                exit()

            lines = f.readlines()

            for line in lines:
                if line == json.dumps(info, indent=2, ensure_ascii=False)[2:46]:
                    flag = False
                    f.close()

        if flag:
            with open(path, 'a') as f:
                f.write(json.dumps(info, indent=2, ensure_ascii=False))
                f.write('\n\n')
                f.close()
