from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.queue: list[str] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.queue:
            raise IndexError("No data in queue")
        rank = self.rank
        self.rank += 1
        item = self.queue.pop(0)
        return (rank, item)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return (
                all((isinstance(item, (int, float))
                    and not isinstance(item, bool))
                    for item in data)
                )
        else:
            return (
                isinstance(data, (int, float))
                and not isinstance(data, bool)
            )

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            self.queue += [str(item) for item in data]
        else:
            self.queue.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return (all(isinstance(item, str) for item in data))
        else:
            return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper data type, should be text")
        if isinstance(data, list):
            self.queue += [str(item) for item in data]
        else:
            self.queue.append(str(data))


class LogProcessor(DataProcessor):
    def _is_str_dict(self, data: Any) -> bool:
        return (isinstance(data, dict) and
                all((isinstance(key, str) and
                    isinstance(value, str))
                    for (key, value) in data.items())
                )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return (all(self._is_str_dict(item) for item in data))
        else:
            return self._is_str_dict(data)

    # TODO: compare and correct!
    # def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
    #     if not self.validate(data):
    #         raise ValueError("Improper data type, "
    #                          "dict of string key-value pairs")
    #     if not isinstance(data, list):
    #         data = [data]
    #     for log in data:
    #         level = log.get("log_level", "UNKNOWN")
    #         message = log.get("log_message", "")
    #         self.queue.append(f"{level}: {message}")

    def ingest(self, data: dict[str, str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper data type, "
                             "dict of string key-value pairs")
        if isinstance(data, list):
            self.queue += [item for item in data]
        else:
            self.queue.append(data)


def test_num_processor() -> None:
    print("\nTesting Numeric Processor...")
    processor = NumericProcessor()

    test_validate = [42, "Hello"]
    for test in test_validate:
        print(f"Trying to validate input {test}:",
              processor.validate(test))

    test_ingest = "foo"
    print(f"Test invalid ingestion of string '{test_ingest}' "
          "without prior validation:")
    try:
        processor.ingest(test_ingest)
    except Exception as error:
        print("Got exception:", error)

    test_processing = [1, 2, 3, 4, 5]
    processor.ingest(test_processing)
    print("Processing data: ", test_processing)

    extract_count = 3
    print(f"Extracting {extract_count} values...")
    for _ in range(extract_count):
        i, value = processor.output()
        print(f"Numeric value {i}: {value}")


def test_text_processor() -> None:
    print("\nTesting Text Processor...")
    processor = TextProcessor()

    test_validate = 42
    print(
        f"Trying to validate input '{test_validate}':",
        processor.validate(test_validate))

    test_processing = ['Hello', 'Nexus', 'World']
    try:
        processor.ingest(test_processing)
        print("Processing data: ", processor.queue)
    except Exception as error:
        print("Got exception:", error)

    try:
        i, value = processor.output()
        print("Extracting 1 value...",
              f"\nText value {i}: {value}"
              )
    except IndexError as error:
        print("Got exception:", error)


def test_log_processor() -> None:
    print("\nTesting Log Processor...")
    processor = LogProcessor()

    test_validate = 'Hello'
    print(
            f"Trying to validate input '{test_validate}':",
            processor.validate(test_validate))

    test_processing = [
        {'log_level': 'NOTICE',
            'log_message': 'Connection to server'},
        {'log_level': 'ERROR',
            'log_message': 'Unauthorized access!!'}]
    print("Processing data: ", test_processing)
    try:
        processor.ingest(test_processing)
    except ValueError as error:
        print("Got exception:", error)

    extract_count = 2
    print(f"Extracting {extract_count} values...")
    for _ in range(extract_count):
        i, value = processor.output()
        # print(f"Log entry {i}: {value}")
        print(f"Log entry {i}: {value['log_level']}: {value['log_message']}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    test_num_processor()
    test_text_processor()
    test_log_processor()


if __name__ == "__main__":
    main()
