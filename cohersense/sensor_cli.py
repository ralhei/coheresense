"""Command line interface for cohersense sensor tool."""
import sys
import click

from .cli_utils import AliasedGroup, click_host, click_port


@click.group(cls=AliasedGroup)
def cli():
    """Command line interface for cohersense sensor."""


@cli.command()
@click.argument('recorder-file', required=False, type=click.File('w'))
@click_host
@click_port
def record(recorder_file, host: str, port: int) -> None:
    """Record pulse from ear clip sensor (or the like).

    :param recorder_file: Optional output file for logging recorded pules times, e.g. for later re-play
    :param port: zeroMQ port

    The recorded pulse time is then sent to the output queue (e.g. ZMQ) for the consumers.
    """
    click.echo(f'Record called with output {recorder_file}, connecting to {host}:{port}')


@cli.command()
@click.argument('recorder-file', type=click.File('r'))
@click.option('-l', '--loop', is_flag=True, help='Play recorded data in endless loop')
@click_host
@click_port
def play(recorder_file, loop: bool, host: str, port: int) -> None:
    """(Re-)Play recoreded pulses from a file.

    :param recorder_file: File containing recorded pulse data.
    :param loop: If true play data in endless loop.
    :param host: zeroMQ interface (e.g. 'localhost' for privacy, or '0.0.0.0' for being readable from everywhere).
    :param port: zeroMQ port

    The recorded pulse time is then sent to the output queue (e.g. ZMQ) for the consumers.
    """
    click.echo(f'Play called from file {recorder_file} (loop={loop}), connecting to {host}:{port}')


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
