import os
from moviepy.editor import *


def remove_sound(video_file_path, out_folder_):
    out_file_name = video_file_path.split(".")[-2].split("/")[-1] + "_no_sound.mp4"
    out_file_path = os.getcwd() + "/" + out_folder_ + "/" + out_file_name

    video = VideoFileClip(video_file_path)
    video = video.without_audio()
    video.write_videofile(out_file_path)


if __name__ == "__main__":

    in_folder_name = "video_raw"
    out_folder_name = "video_no_sound"

    in_folder_path = os.getcwd() + "/" + in_folder_name
    in_file_list = os.listdir(in_folder_path)

    for file in in_file_list:
        in_file_path = in_folder_path + "/" + file

        remove_sound(in_file_path, out_folder_name)

