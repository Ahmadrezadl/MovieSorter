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


def create_folders_for_files(directory, name_format, mkv_format, mp4_format, avi_format, srt_format, zip_format,
                             same_name, series_files, movie_files, episode_folders):
    for file in os.listdir(directory):
        if file.lower().endswith(".mkv") and mkv_format:
            file_name = file.replace(".mkv", "")
        elif file.lower().endswith(".mp4") and mp4_format:
            file_name = file.replace(".mp4", "")
        elif file.lower().endswith(".avi") and avi_format:
            file_name = file.replace(".avi", "")
        elif file.lower().endswith(".srt") and srt_format:
            file_name = file.replace(".srt", "")
        elif file.lower().endswith(".zip") and zip_format:
            file_name = file.replace(".zip", "")
        else:
            continue

        file_name = remove_symbols(file_name)
        season_episode_pattern = re.compile(r'(S\d{2})(E\d{2})', re.IGNORECASE)

        folder_words = re.split(r'\s', file_name)

        movie_name = ""
        year = None
        season = None
        episode = None
        series = False

        for word in folder_words:
            if word.isdigit() and 1900 < int(word) < 3000:
                year = word
                break
            match = season_episode_pattern.match(word)
            if match:
                series = True
                season, episode = match.groups()
                break
            movie_name += word + " "

        movie_name = movie_name.strip()


        folder_name = name_format
        folder_name = folder_name.replace('{name}', str(movie_name))
        if year:
            folder_name = folder_name.replace('{year}', str(year))
        else:
            folder_name = re.sub(r'[\S]*\{year\}[\S]*', '', folder_name)

        folder_name.strip()

        if folder_name[-1] == ' ':
            folder_name = folder_name[:-1]

        new_dir = directory + "\\" + folder_name
        create_folder(new_dir)

        if series and season and episode:
            new_dir = new_dir + "\\" + season
            create_folder(new_dir)

            if episode_folders:
                new_dir = new_dir + "\\" + episode
                create_folder(new_dir)

        os.rename(os.path.join(directory, file), new_dir + "\\" + file)

        rename_subtitle_files(new_dir)



def create_folder(new_dir):
    try:
        os.mkdir(new_dir)
    except OSError:
        pass


def remove_symbols(folder_name):
    return folder_name.replace(".", " ").replace("_", " ").replace("-", " ").replace("(", "").replace(")", "").strip()


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


def rename_subtitle_files(directory, ):
    """Rename subtitle files to match the video file name."""
    video_name_without_extension = None
    for file in os.listdir(directory):
        for video_type in ['mkv', 'mp4', 'avi']:
            if file.lower().endswith(video_type):
                video_name_without_extension = file.rsplit(video_type, 1)[0]
                break
        if video_name_without_extension:
            break

        # If no video file is found, exit the function
    if not video_name_without_extension:
        return
    subtitle_name = video_name_without_extension + FILE_TYPES['srt']

    for file in os.listdir(directory):
        if file.lower().endswith(FILE_TYPES['srt']):
            try:
                os.rename(os.path.join(directory, file), os.path.join(directory, subtitle_name))
            except FileExistsError:
                pass
            break
