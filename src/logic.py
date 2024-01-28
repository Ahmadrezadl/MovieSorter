import os
import re

# Constants for file types
FILE_TYPES = {
    'mkv': '.mkv',
    'mp4': '.mp4',
    'avi': '.avi',
    'srt': '.srt',
    'zip': '.zip'
}
SEASON_EPISODE_PATTERN = re.compile(r'^(S|s)(\d{2})(E|e)(\d{2})$')


def move_files_to_root_and_remove_empty_dirs(directory):
    """Move all files from subdirectories to the root and remove empty directories."""
    if len(directory) < 2:
        return
    for root, dirs, files in os.walk(directory):
        for file in files:
            os.rename(os.path.join(root, file), os.path.join(directory, file))
        if not os.listdir(root):
            os.rmdir(root)


def create_folders_for_files(directory, name_format, formats, year_in_bracket, rename_subtitle):
    """Organize files into folders based on the file type and name."""
    for file in os.listdir(directory):
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension not in formats:
            continue

        new_directory = construct_directory_name(file, directory, name_format, year_in_bracket)
        if not new_directory:
            continue

        try:
            os.makedirs(new_directory, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory {new_directory}: {e}")
            continue

        os.rename(os.path.join(directory, file), os.path.join(new_directory, file))

        if rename_subtitle and file_extension == FILE_TYPES['mkv']:
            rename_subtitle_files(new_directory, file)


def construct_directory_name(file, directory, name_format, year_in_bracket):
    """Construct the directory name based on the file name and provided format."""
    file_name_without_extension = os.path.splitext(file)[0]
    file_name_parts = re.split(r'\s|\.', file_name_without_extension)

    serial_info = parse_serial_info(file_name_parts)
    if serial_info:
        return construct_serial_directory_name(directory, serial_info, file_name_parts)

    return construct_movie_directory_name(directory, file_name_parts, name_format, year_in_bracket)


def parse_serial_info(file_name_parts):
    """Parse season and episode information from file name parts."""
    for part in file_name_parts:
        match = SEASON_EPISODE_PATTERN.match(part)
        if match:
            return {
                'season': match.group(1).upper() + match.group(2),
                'episode': match.group(3).upper() + match.group(4)
            }
    return None


def construct_serial_directory_name(directory, serial_info, file_name_parts):
    """Construct directory name for serials."""
    serial_name = ' '.join(
        file_name_parts[:file_name_parts.index(serial_info['season'] + serial_info['episode'].lower())])
    return os.path.join(directory, serial_name, serial_info['season'], serial_info['episode'])


def construct_movie_directory_name(directory, file_name_parts, name_format, year_in_bracket):
    """Construct directory name for movies."""
    year = next((part for part in file_name_parts if part.isdigit() and 1900 < int(part) < 3000), None)
    if not year:
        return None

    name = ' '.join(part for part in file_name_parts if part != year)
    formatted_year = f"({year})" if year_in_bracket else year
    folder_name = name_format.replace('{year}', formatted_year).replace('{name}', name)
    return os.path.join(directory, folder_name)


def rename_subtitle_files(directory, video_file_name):
    """Rename subtitle files to match the video file name."""
    video_name_without_extension = os.path.splitext(video_file_name)[0]
    subtitle_name = video_name_without_extension + FILE_TYPES['srt']

    for file in os.listdir(directory):
        if file.lower().endswith(FILE_TYPES['srt']):
            try:
                os.rename(os.path.join(directory, file), os.path.join(directory, subtitle_name))
            except FileExistsError:
                print('Multiple subtitle files exist.')
            break

