import click

from logic import createFolder


@click.command()
@click.argument('directory')
@click.argument('format')
def main(directory,format):
    createFolder(directory,format,True,True,True,True,True,True,True,True,True,False)


if __name__ == "__main__":
    main()