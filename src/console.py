import click
from logic import create_folders_for_files

@click.command()
@click.argument('directory')
@click.argument('name_format')
@click.option('--mkv_format', default=True, type=bool, help='Process MKV files')
@click.option('--mp4_format', default=True, type=bool, help='Process MP4 files')
@click.option('--avi_format', default=True, type=bool, help='Process AVI files')
@click.option('--srt_format', default=True, type=bool, help='Process SRT files')
@click.option('--zip_format', default=True, type=bool, help='Process ZIP files')
@click.option('--same_name', default=True, type=bool, help='Maintain same name for files')
@click.option('--serial_files', default=True, type=bool, help='Process Serial files')
@click.option('--movie_files', default=True, type=bool, help='Process Movie files')
@click.option('--episode_folders', default=True, type=bool, help='Create folders for episodes')
def main(directory, name_format, mkv_format, mp4_format, avi_format, srt_format, zip_format, same_name, serial_files, movie_files, episode_folders):
    """A script to organize files into folders."""
    create_folders_for_files(directory, name_format, mkv_format, mp4_format, avi_format, srt_format, zip_format, same_name, serial_files, movie_files, episode_folders)

if __name__ == "__main__":
    main()
