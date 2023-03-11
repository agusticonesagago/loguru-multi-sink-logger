"""This module provides functionality to configure a logger with multiple file sinks, based on the given configurations.

The module includes a `_file_sink` function that returns a function that writes log messages to a file. The `configure_logger`
function uses the `_file_sink` function to create a new sink for each configuration in the configs parameter, and adds the
sink to the logger. The module also includes a main function that demonstrates the usage of the `configure_logger` function.
"""
from loguru import logger
from typing import Callable, List, Dict, Any

def _file_sink(file_path: str) -> Callable[[str], None]:
    """Returns a function that writes log messages to a file.

    :param file_path: The path to the file to write log messages to.
    :return: A function that takes a string argument and writes it to the specified file.
    """
    def _write_message(message: str) -> None:
        """Writes the specified message to the file specified by `file_path`.

        :param message: The message to write to the file.
        """
        with open(file_path, "a") as f:
            f.write(message + "\n")
    return _write_message


def configure_logger(configs: List[Dict[str, Any]]) -> None:
    """Configure a logger with multiple file sinks, based on the given configurations.

    Each configuration is represented as a dictionary with the following keys:
    - "file_path": The path to the file where the sink should write log messages.
    - "file_name": A short name to identify the sink in log records.
    - Additional key-value pairs can be provided as keyword arguments to be passed to `logger.add()`.

    The function removes the default sink (stdout) and adds a new sink for each configuration,
    using the `_file_sink` function to create the sink function.

    :param configs: A list of configurations, where each configuration is a dictionary that includes
    the necessary keys as well as any additional key-value pairs to be passed to `logger.add()`.
    """
    logger.remove()  # Remove the default sink (stdout)
    for config in configs:
        sink = _file_sink(config["file_path"])
        kwargs = {key: value for key, value in config.items() if key not in ["file_path", "file_name"]}
        logger.add(sink, filter=lambda record, name=config["file_name"]: record["extra"].get("file") == name, **kwargs)

if __name__ == "__main__":
    configs = [
        {
            "file_path": "my_log_file1.txt",
            "file_name": "file1",
            "level": "ERROR"
        },
        {
            "file_path": "my_log_file2.txt",
            "file_name": "file2",
            "format": "{time} - {level} - {message}"
        }
    ]
    configure_logger(configs)

    logger.info("This message will be written to my_log_file1.txt", file="file1")
    logger.info("This message will be written to my_log_file2.txt", file="file2")
    logger.error("This message will be written with ERROR to my_log_file1.txt", file="file1")
