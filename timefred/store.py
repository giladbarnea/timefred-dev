import toml
from toml.encoder import TomlPreserveInlineDictEncoder, TomlArraySeparatorEncoder
import os
from pathlib import Path
import functools as ft
from timefred.time import today, now


class Store:
	def __init__(self) -> None:
		self._path = Path(os.environ.get('TIMEFRED_STORE', '~/.timefred.toml')).expanduser()
		self._path.touch()
		self._work = None

	# @ft.cached_property
	@property
	def data(self) -> dict:
		with open(self._path) as datafile:
			data = toml.load(datafile)
		return data

	# @ft.cached_property
	@property
	def work(self):
		return self._work

	@work.setter
	def work(self, what):
		self._work = what
		data = self.data
		# data[today()] = {now():dict(work=what)}
		# data[today()] = dict(what=what, start=now())
		data[today()] = [{
			what: dict(
					start=now()
					)
			}]
		# data['work'] = what
		with open(self._path, 'a') as datafile:
			toml.dump(data, datafile, TomlPreserveInlineDictEncoder())


store = Store()
