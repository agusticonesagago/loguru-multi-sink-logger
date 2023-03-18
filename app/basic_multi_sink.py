"""This module provides functionality to configure a logger with multiple file sinks, based on the given configurations.

The `configure_logger` function creates a new sink for each configuration in the configs parameter, and adds the
sink to the logger. The module also includes a main function that demonstrates the usage of the `configure_logger` function.
"""
from loguru import logger
from typing import List, Dict


def configure_logger(configs: List[Dict[str, str]]) -> None:
    """Configure a logger with multiple file sinks, based on the given configurations.

    Each configuration is represented as a dictionary with the following keys:
    - "file_path": The path to the file where the sink should write log messages.
    - "file_name": A short name to identify the sink in log records.
    - "level": The minimum severity level for log messages to be processed by the sink.

    The function removes the default sink (stdout) and adds a new sink for each configuration.

    :param configs: A list of sink configurations, where each configuration is a dictionary.
    """
    logger.remove()  # Remove the default sink (stdout)
    for config in configs:
        logger.add(config["file_path"], level=config["level"], filter=lambda record, name=config["file_name"]: record["extra"].get("file") == name)

if __name__ == "__main__":
    configs = [
        {
            "file_path": "my_log_file1.txt",
            "file_name": "file1",
            "level": "INFO"
        },
        {
            "file_path": "my_log_file2.txt",
            "file_name": "file2",
            "level": "INFO"
        }
    ]
    configure_logger(configs)

    logger.info("This message will be written to my_log_file1.txt", file="file1")
    logger.info("This message will be written to my_log_file2.txt", file="file2")
