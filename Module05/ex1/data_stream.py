from typing import Any, List, Union, Dict
from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
	def __init__(self):
		self._internal_data: List[tuple[int, str]] = []
		self._current_rank = 0
		self._total_count = 0

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
	
	""" ? """
	@property
	def stats(self) -> tuple[int, int]:
		return self._total_count, len(self._internal_data)


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
			self._total_count += 1


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
			self._total_count += 1


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
			formatted_log = ", ".join([f"{v}" for v in item.values()])
			self._internal_data.append((self._current_rank, formatted_log))
			self._current_rank += 1
			self._total_count += 1


class DataStream:
	def __init__(self):
		self.processors: List[DataProcessor] = []

	def reg_processor(self, processor: DataProcessor) -> None:
		self.processors.append(processor)

	def process_stream(self, stream: list[typing.Any]) -> None:
		for element in stream:
			handled = False
			for proc in self.processors:
				if proc.validate(element):
					proc.ingest(element)
					handled = True
					break
			if not handled:
				print(f"DataStream Error - Can't process element in stream: {element}")

	def print_processors_stats(self) -> None:
		print("== DataStream statistics ==")
		if not self.processors:
			print("No processor found, no data")
			return

		for proc in self.processors:
			total, remaining = proc.stats
			name = proc.__class__.__name__.replace("Processor", "Processor")
			print(f"{name}: total {total} items processed, remaining {remaining} on processor")


def main():
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    num_proc = NumericProcessor()
    ds.reg_processor(num_proc)

    batch = [
        'Hello world', 
        [3.14, -1, 2.71], 
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 
        42, 
        ['Hi', 'five']
    ]

    print("Send first batch of data on stream:", batch)
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.reg_processor(text_proc)
    ds.reg_processor(log_proc)

    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3): num_proc.output()
    for _ in range(2): text_proc.output()
    for _ in range(1): log_proc.output()

    ds.print_processors_stats()

if __name__ == "__main__":
    main()
