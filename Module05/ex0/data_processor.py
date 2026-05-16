from typing import Any, List, Union, Dict
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
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
    def validate(self, data: Any) -> bool:

        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            return True
        return False

    def ingest(
            self,
            data: Union[int, float, List[Union[int, float]]]) -> None:

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

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._internal_data.append((self._current_rank, item))
            self._current_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:

        def is_log_dict(d):
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

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
            raise ValueError("Improper log data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            level = item.get('log_level', '')
            msg = item.get('log_message', '')
            if level and msg:
                formatted_log = f"{level}: {msg}"
            else:
                formatted_log = ", ".join(
                    [f"{k}: {v}" for k, v in item.items()]
                )

            self._internal_data.append((self._current_rank, formatted_log))
            self._current_rank += 1


def run_tests() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, val = np.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(['Hello', 'Nexus', 'World'])
    rank, val = tp.output()
    print(f"Extracting 1 value...\nText value {rank}: {val}")

    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    lp.ingest(log_data)
    print(f"Extracting {len(log_data)} values...")
    for _ in range(len(log_data)):
        rank, val = lp.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    run_tests()
