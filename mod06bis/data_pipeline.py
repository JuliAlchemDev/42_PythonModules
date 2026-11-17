from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    def process_output(
        self,
            data: list[tuple[int, str]]) -> None:
        ...


class CSVExport():
    def process_output(
        self,
            data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(item for _, item in data))


class JSONExport():
    def process_output(
        self,
            data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = ", ".join(f'"item_{rank}": "{value}"' for rank, value in data)
        print("{" + pairs + "}")


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
            return (all((isinstance(item, (int, float))
                    and not isinstance(item, bool))
                    for item in data)
                    )
        else:
            return (
                isinstance(data, (int, float))
                and not isinstance(data, bool))

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

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper data type, "
                             "dict of string key-value pairs")
        if not isinstance(data, list):
            data = [data]
        for log in data:
            level = log.get("log_level", "UNKNOWN")
            message = log.get("log_message", "")
            self.queue.append(f"{level}: {message}")


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(
            self, proc: DataProcessor) -> None:
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
        print("\n== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        else:
            for proc in self.processors:
                name = type(proc).__name__.replace("Processor", " Processor")
                remaining = len(proc.queue)
                total = remaining + proc.rank
                print(f"{name}: total {total} items processed, "
                      f"remaining {remaining} on processor")

    def output_pipeline(
            self,
            nb: int,
            plugin: ExportPlugin) -> None:
        for proc in self.processors:
            count = min(nb, len(proc.queue))
            data = []
            for _ in range(count):
                data.append(proc.output())
            plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    data_batch = [
        'Hello world', [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ], 42, ['Hi', 'five']]

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print(f"\nSend first batch of data on stream: {data_batch}")
    stream.process_stream(data_batch)
    stream.print_processors_stats()

    csv = CSVExport()
    plugin_name = type(csv).__name__.replace("Export", "")
    count = 3
    print(
        "\n"
        f"Send {count} processed data from each processor"
        f" to a {plugin_name} plugin:")
    stream.output_pipeline(count, csv)

    stream.print_processors_stats()

    data_batch = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']

    print(f"\nSend another batch of data: {data_batch}")
    stream.process_stream(data_batch)
    stream.print_processors_stats()

    json = JSONExport()
    plugin_name = type(json).__name__.replace("Export", "")
    count = 5
    print(
        "\n"
        f"Send {count} processed data from each processor"
        f" to a {plugin_name} plugin:")
    stream.output_pipeline(count, json)

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
