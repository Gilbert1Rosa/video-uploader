from moviepy.editor import *
from http import client


def make_clip(source, destination, start, end, default_fps=60):
    video = VideoFileClip(source).subclip(start, end)

    result = CompositeVideoClip([video])
    result.write_videofile(destination, fps=default_fps)


def upload(file_path, open_id, access_token):
    host = "open-api.tiktok.com"
    path = f'/share/video/upload/open_id={open_id}&access_token={access_token}'
    video_content = bytes("")  # Get content from "file_path"
    connection = client.HTTPConnection(host)
    connection.request(method="POST", url=path, body='{}')
    response = connection.getresponse()
    connection.close()


make_clip(sys.argv[1], sys.argv[2], "27:45", "46:50", int(sys.argv[3]))
