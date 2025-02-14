import pytest
from src.channel import Channel
from src.video import Video, PLVideo
from src.playlist import PlayList


moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
highload = Channel('UCwHL6WHUarjGfUM_586me8w')

video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


# def test_channel():
#     assert moscowpython.print_info() == """{
#   "kind": "youtube#channelListResponse",
#   "etag": "Jn8bAzcjn3NlP5XnjWjA07DVSgg",
#   "pageInfo": {
#     "totalResults": 1,
#     "resultsPerPage": 5
#   },
#   "items": [
#     {
#       "kind": "youtube#channel",
#       "etag": "lMEMwE3DwyatYjrkY7Dsmwr61jE",
#       "id": "UC-OVMPlMA3-YCIeg4z5z23A",
#       "snippet": {
#         "title": "MoscowPython",
#         "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
#         "customUrl": "@moscowdjangoru",
#         "publishedAt": "2012-07-13T09:48:44Z",
#         "thumbnails": {
#           "default": {
#             "url": "https://yt3.ggpht.com/ytc/AIf8zZTv3icfUESIyeI-LBz7mGlmu81dYEGEh0Zp3nfwKw=s88-c-k-c0x00ffffff-no-rj",
#             "width": 88,
#             "height": 88
#           },
#           "medium": {
#             "url": "https://yt3.ggpht.com/ytc/AIf8zZTv3icfUESIyeI-LBz7mGlmu81dYEGEh0Zp3nfwKw=s240-c-k-c0x00ffffff-no-rj",
#             "width": 240,
#             "height": 240
#           },
#           "high": {
#             "url": "https://yt3.ggpht.com/ytc/AIf8zZTv3icfUESIyeI-LBz7mGlmu81dYEGEh0Zp3nfwKw=s800-c-k-c0x00ffffff-no-rj",
#             "width": 800,
#             "height": 800
#           }
#         },
#         "localized": {
#           "title": "MoscowPython",
#           "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
#         },
#         "country": "RU"
#       },
#       "statistics": {
#         "viewCount": "2496950",
#         "subscriberCount": "26900",
#         "hiddenSubscriberCount": false,
#         "videoCount": "729"
#       }
#     }
#   ]
# }"""


def test_str():
    assert str(moscowpython) == 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'


def test_add():
    assert moscowpython + highload >= 100100


def test_sub():
    assert 40000 < highload - moscowpython < 65000
    assert -65000 < moscowpython - highload < -40000


def test_eq():
    assert False == (moscowpython == highload)
    moscowpython.sub_quantity = 10
    highload.sub_quantity = 10
    assert True == (moscowpython == highload)
    moscowpython.sub_quantity = 9
    highload.sub_quantity = 10


def test_lt():
    assert True == (moscowpython < highload)
    moscowpython.sub_quantity = 10
    highload.sub_quantity = 9
    assert False == (moscowpython < highload)
    moscowpython.sub_quantity = 9
    highload.sub_quantity = 10


def test_le():
    assert True == (moscowpython <= highload)
    moscowpython.sub_quantity = 10
    highload.sub_quantity = 9
    assert False == (moscowpython <= highload)
    moscowpython.sub_quantity = 9
    highload.sub_quantity = 10


def test_gt():
    assert False == (moscowpython > highload)
    moscowpython.sub_quantity = 10
    highload.sub_quantity = 9
    assert True == (moscowpython > highload)
    moscowpython.sub_quantity = 9
    highload.sub_quantity = 10


def test_ge():
    assert False == (moscowpython >= highload)
    moscowpython.sub_quantity = 10
    highload.sub_quantity = 9
    assert True == (moscowpython >= highload)
    moscowpython.sub_quantity = 9
    highload.sub_quantity = 10


def test_get_service():
    assert str(Channel.get_service())[:-20] == '<googleapiclient.discovery.Resource object at'


def test_str_video():

    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_duration():
    assert str(pl.total_duration) == "1:49:52"


def test_video_init_error():
    broken_video = Video('broken_video_id')
    assert broken_video.video_id == 'broken_video_id'
    assert broken_video.title is None
    assert broken_video.likeCount is None
