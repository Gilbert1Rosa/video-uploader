from http import client


def upload(file_path, open_id, access_token):
    host = "open-api.tiktok.com"
    path = f'/share/video/upload/open_id={open_id}&access_token={access_token}'
    video_content = bytes("")  # Get content from "file_path"
    connection = client.HTTPConnection(host)
    connection.request(method="POST", url=path, body='{}')
    response = connection.getresponse()
    connection.close()