from typing import Any, List, Union, Dict, Protocol
from abc import ABC, abstractmethod
import typing


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataProcessor(ABC):
    def __init__(self) -> None:
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

    @property
    def stats(self) -> tuple[int, int]:
        return self._total_count, len(self._internal_data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(
                isinstance(x, (int, float)) for x in data):
            return True
        return False

    def ingest(self, data: Union[
            int,
            float,
            List[Union[
                int,
                float]
                ]
            ]) -> None:

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
            data: Union[str, List[str]]) -> None:
        if not data:
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._internal_data.append((self._current_rank, item))
            self._current_rank += 1
            self._total_count += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:

        def is_log_dict(d):
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items())

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
                ]) -> None:

        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            formatted_log = f"{item['log_level']}: {item['log_message']}"
            self._internal_data.append((self._current_rank, formatted_log))
            self._current_rank += 1
            self._total_count += 1


class DataStream:
    def __init__(self) -> None:
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
                print(
                    f"DataStream Error - Can't process element in "
                    f"stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            total, remaining = proc.stats
            name = proc.__class__.__name__.replace("Processor", "Processor")
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            extracted_data = []
            for _ in range(nb):
                try:
                    extracted_data.append(proc.output())
                except IndexError:
                    break

            if extracted_data:
                plugin.process_output(extracted_data)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        csv_string = ",".join(val for _, val in data)
        print(csv_string)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_parts = [f'"item_{rank}": "{val}"' for rank,  val in data]
        json_string = "{" + ", ".join(json_parts) + "}"
        print(json_string)


def main():
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    ds.reg_processor(num_proc)
    ds.reg_processor(text_proc)
    ds.reg_processor(log_proc)

    batch_1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch_1}")
    ds.process_stream(batch_1)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    batch_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print(f"\nSend another batch of data: {batch_2}")
    ds.process_stream(batch_2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
