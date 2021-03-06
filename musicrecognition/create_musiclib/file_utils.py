import re
import subprocess

re_filetype = re.compile('[.]\w+$')

def get_filetype_song(songpath):
    """Returns the extension (including .) of the filename"""
    return re_filetype.search(songpath).group()


def get_name_song(file):
    """Returns the name of the song (the filename)"""
    return re_filetype.sub('', file)


def get_length_song(songpath):
    """Returns the length of the song in minutes (rounded down)"""
    process = subprocess.Popen(['ffmpeg', '-i', songpath],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    matches = re.search(
        (r"Duration:\s{1}(?P<hours>\d+?):"
         r"(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),"),
        str(stdout), re.DOTALL).groupdict()
    return int(matches['minutes'])

