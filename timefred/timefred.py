import click
from timefred.action import on_group

main = click.CommandCollection(sources=[on_group])
