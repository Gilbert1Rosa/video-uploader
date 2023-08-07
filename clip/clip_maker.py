from moviepy.editor import *


def make_clip(source, destination, start, end, default_fps=60):
    video = VideoFileClip(source).subclip(start, end)

    result = CompositeVideoClip([video])
    result.write_videofile(destination, fps=default_fps)
