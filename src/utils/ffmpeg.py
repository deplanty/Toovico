import os


def convert(input_file:str, output_file:str, output_size:str=None):
    """
    Converts a given video to another format.

    Args:
        input_file (str): path to the input video.
        output_file (str): path to the output video.
        output_size (str, optional): size of the output video WxH.
    """

    if output_size:
        command = f"ffmpeg -y -i {input_file} -s {output_size} {output_file}"
    else:
        command = f"ffmpeg -y -i {input_file} {output_file}"

    os.system(command)


def to_video(input_folder:str, pattern_file:str, output_file:str, framerate:int=30):
    """
    Creates a video from all the images in a folder with a giver filename pattern.

    Args:
        input_folder (str): folder containing all the images.
        pattern_file (str): pattern of the images.
        output_file (str): path to the output video file.
    """

    input = os.path.join(input_folder, pattern_file)
    command = f"ffmpeg -framerate {framerate} -y -i {input} {output_file}"

    os.system(command)
