import click
from timefred import store

@click.group('on_group')
def on_group():
	print('on_group()')

@on_group.command()
@click.argument('what')
def on(what):
	print(f'on({what = })')
	print(f'{store.data = }')
	store.work = what
