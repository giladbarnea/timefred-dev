import click
from timefred import store


@click.group('finish_group')
def finish_group():
	print('finish_group()')


@finish_group.command()
@click.argument('what')
def finish(what):
	print(f'finish({what = })')
	print(f'{store.data = }')
	# store.work = what
