import click


@click.group(short_help="ua2 CLI.")
def ua2():
    """ua2 CLI.
    """
    pass


@ua2.command()
@click.argument("name", default="ua2")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [ua2]
