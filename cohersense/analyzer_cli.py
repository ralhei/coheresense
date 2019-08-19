"""Command line interface for cohersense analyzer tool."""
import sys
import click

from .cli_utils import AliasedGroup, click_host, click_port


@click.group(cls=AliasedGroup)
def cli():
    """Command line interface for cohersense sensor."""


@cli.command()
@click_host
@click_port
def raspberry(host: str, port: int) -> None:
    """Analyize and show heart coherence metrics on raspberry.

    :param host: zeroMQ host to read data from.
    :param port: zeroMQ port on given host.

    This function should be used for displaying the results on a raspberry itself.
    Read pulse information from zeroMQ, analyze HRV and display heart coherence metrics.
    """
    click.echo(f'Analysze heart coherence, reading pulse data from {host}:{port}')


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
