from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.queue = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
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


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(
            self, proc: DataProcessor
            ) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break
                if not handled:
                    print(
                        "DataStream error - Can't process element in stream:",
                        data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                name = type(proc).__name__.replace("Processor", " Processor")
                remaining = len(proc.queue)
                total = remaining + proc.rank
                print(f"{name}: total {total} items processed, "
                      f"remaining {remaining} on processor")


def main():
    print("=== Code Nexus - Data Stream ===")
    data_batch = [
        'Hello world', [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ], 42, ['Hi', 'five']
        ]

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    stream.register_processor(NumericProcessor())

    print(f"\nSend first batch of data on stream: {data_batch}")
    stream.process_stream(data_batch)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
