import json
import requests
import os
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key: str = os.getenv("AIzaSyBjD6--COMCnKq1ApAkfdppxWC96_2ly_I")
        # self.youtube = build('youtube', 'v3', developerKey=self.api_key)  тут непонятная ошибка

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # channel = self.youtube.channels().list(id=self.channel_id).execute()  данная часть не срабатывает из-за ошибки выше
        # print(channel)
        pass
