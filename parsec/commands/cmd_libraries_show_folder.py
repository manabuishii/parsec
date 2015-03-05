import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_show_folder')
@click.argument("library_id", type=str)
@click.argument("folder_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, library_id, folder_id):
    """Get details about a given folder. The required ``folder_id`` can be obtained from the folder's library content details.
    """
    return ctx.gi.libraries.show_folder(library_id, folder_id)
