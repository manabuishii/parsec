import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_show_dataset')
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, dataset_id):
    """Get details about a given history dataset.
    """
    return ctx.gi.histories.show_dataset(history_id, dataset_id)
