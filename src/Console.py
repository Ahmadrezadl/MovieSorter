import click

from logic import create_folders_for_files


@click.command()
@click.argument('directory')
@click.argument('format')
def main(directory, format):
    create_folders_for_files(directory, format, True, True, True)


if __name__ == "__main__":
    main()
