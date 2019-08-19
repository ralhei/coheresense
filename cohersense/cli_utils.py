"""Utility functions and classes for click. """
import click


class AliasedGroup(click.Group):
    """Allows to run commands with their shortest, unique command abbreviation."""
    # Source: https://click.palletsprojects.com/en/7.x/advanced/
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))


click_host = click.option('-H', '--host', default='localhost', help='Define host/interface to connect to for zeroMQ.')
click_port = click.option('-p', '--port', type=int, default=5555, help='Port number for zeroMQ')
