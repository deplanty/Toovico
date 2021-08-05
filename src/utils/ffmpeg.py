import os


def convert(input_file, output_file, output_size:str=None):
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
