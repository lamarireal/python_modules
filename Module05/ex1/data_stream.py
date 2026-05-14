from typing import Any, List, Union, Dict
from abc import ABC, abstractmethod


class DataProcessor(ABC):
	def __init__(self):
		self._internal_data: List[tuple[int, str]] = []
		self._current_rank = 0

	@abstractmethod
	def validate(self, data: Any) -> bool:
		pass

	@abstractmethod
	def ingest(self, data: Any) -> None:
		pass

	def output(self) -> tuple[int, str]:
		if not self._internal_data:
			raise IndexError("No data left to output")
		return self._internal_data.pop(0)


class NumericProcessor(DataProcessor):
	def validate(self,
			data: Any
		) -> bool:

		if isinstance(data, (int, float)):
			return True
		if isinstance(data, list)and all(isinstance(x,
									(int, float))for x in data):
			return True
		return False

	def ingest(self, data: 
		Union[
			int,
			float,
			List[Union[
				int,
				float]
				]
			]
		) -> None:

		if not self.validate(data):
			raise ValueError("Improper numeric data")

		items = data if isinstance(data, list) else [data]
		for item in items:
			self._internal_data.append((self._current_rank, str(item)))
			self._current_rank += 1


class TextProcessor(DataProcessor):
	def validate(self, data: Any) -> bool:
		if isinstance(data, str):
			return True
		if isinstance(data, list) and all(isinstance(x, str) for x in data):
			return True
		return False
	
	def ingest(
			self,
			data: Union[
				int,
				str,
				List[Union[
					int,
					str]
				]
			]
		) -> None:
		if not data:
			raise ValueError("Improper numeric data")

		items = data if isinstance(data, list) else [data]
		for item in items:
			self._internal_data.append((self._current_rank, item))
			self._current_rank += 1


class LogProcessor(DataProcessor):
	def validate(self,
			data: Any
		) -> bool:

		def is_log_dict(d):
			return isinstance(d, dict)and all(isinstance(k, str) and
									 isinstance(v, str) for k,v in d.items())
		
		if is_log_dict(data):
			return True
		if isinstance(data, list) and all(is_log_dict(x) for x in data):
			return True
		return False
	
	def ingest(
			self,
			data: Union[
				Dict[str, str],
				List[Dict[str, str]]
				]
		) -> None:

		if not self.validate(data):
			raise ValueError("Improper numeric data")
		
		items = data if isinstance(data, list) else [data]
		for item in items:
			formatted_log = ", ".join([f"{k}: {v}" for k, v in item.items()])
			self._internal_data.append((self._current_rank, formatted_log))
			self._current_rank += 1
