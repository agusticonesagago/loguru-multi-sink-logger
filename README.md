# Loguru Multi-Sink Module

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Functions](#functions)
- [Usage](#usage)
- [Configure](#configure)
- [Feedback](#feedback)
- [License](#license)

## Introduction

Loguru Multi-Sink is a powerful extension to the Loguru logging library that allows for easy configuration of a logger with multiple file sinks based on user-defined configurations. This module provides enhanced control over the logging process by enabling the categorization and management of log messages according to their source or purpose.

With Loguru Multi-Sink, you can effortlessly configure your logger to send log messages to specific log files, streamlining the analysis and troubleshooting of issues in your application. The module is designed to be user-friendly and easy to set up, allowing you to quickly configure a multi-sink logger with just a few lines of code.


## Getting Started

Getting started with Loguru Multi-Sink is quick and easy thanks to Docker. To get started, you'll need to have Docker installed on your system. Once you have Docker installed, you can clone the repository and navigate to the root directory of the project in your terminal.

To start the application with Docker, simply run the following command:

```python
docker-compose up
```

This will start a container with Loguru Multi-Sink and all the necessary packages installed. Once the container is up and running, you can start using Loguru Multi-Sink right away.

Alternatively, if you prefer not to use Docker, you can still install the necessary packages using pip. To do this, navigate to the root directory of the project in your terminal and run the following command:

```python
pip install -r requirements.txt
```
This will install all the required packages and dependencies needed for Loguru Multi-Sink to function properly. Once the packages are installed, you can start using Loguru Multi-Sink in your own Python projects.

## Functions


### `_file_sink(file_path: str) -> Callable[[str], None]`

Returns a function that writes log messages to a file.

Parameters:
- `file_path`: The path to the file to write log messages to.

Returns:
A function that takes a string argument and writes it to the specified file.

### `configure_logger(configs: List[Dict[str, str]]) -> None`

Configure a logger with multiple file sinks, based on the given configurations.

Each configuration is represented as a dictionary with the following keys:
- `file_path`: The path to the file where the sink should write log messages.
- `file_name`: A short name to identify the sink in log records.
- Additional `key-value` pairs can be provided as keyword arguments to be passed to `logger.add()`.

The function removes the default sink (stdout) and adds a new sink for each configuration, using the `file_sink` function to create the sink function.

Parameters:
- `configs`: A list of sink configurations, where each configuration is a dictionary.

## Usage

1. To use the logging library in Python, you can start by importing the `configure_logger` function. This function can be called with a list of sink configurations, where each configuration is a dictionary containing the following:

   * **file_path**: The path to the file where the sink should write log messages.
   * **file_name**: A short name to identify the sink in log records.
   * Additional **key-value pairs** can be provided as keyword arguments to be passed to `logger.add()`.


    ```python
    from app.multi_sink import configure_logger

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
    ```

2. Use the logger object to write log messages. To specify which sink to use, add a file parameter to the logging call with the same value as the file_name key in the corresponding configuration. Example:

    ```python
    from loguru import logger

    logger.info("This message will be written to my_log_file1.txt", file="file1")
    logger.info("This message will be written to my_log_file2.txt", file="file2")
    ```

## Configure

Loguru Multi-Sink supports two ways of configuring the logger: basic configuration and advanced configuration.

### Basic Configuration

The basic configuration allows you to configure the `file_path`, `file_name`, and `level` parameters for each sink using a simple dictionary.

```python
from app.basic_multi_sink import configure_logger

configs = [
    {
        "file_path": "logs/file1.log",
        "file_name": "file1",
        "level": "INFO"
    },
    {
        "file_path": "logs/file2.log",
        "file_name": "file2",
        "level": "DEBUG"
    }
]

configure_logger(configs)
```

### Advanced Configuration
The advanced configuration allows you to configure each sink using all the possible keyword arguments supported by the `loguru.add()` function, as well as the `file_path` and `file_name` parameters.

```python
from app.multi_sink import configure_logger

configs = [
    {
        "file_path": "logs/file1.log",
        "file_name": "file1",
        "enqueue": True,
        "retention": "10 days",
        "rotation": "1 week",
        "compression": "zip",
        "backtrace": True,
        "diagnose": True,
        "level": "INFO"
    },
    {
        "file_path": "logs/file2.log",
        "file_name": "file2",
        "enqueue": True,
        "retention": "20 days",
        "rotation": "2 week",
        "compression": "zip",
        "backtrace": True,
        "diagnose": True,
        "level": "ERROR"
    }
]

configure_logger(configs)
```

## Feedback

We are committed to constantly improving and evolving this tool to meet the needs of our users. If you have any feedback or suggestions for how we can make the tool more useful or efficient, we would love to hear from you. You can get in touch with us through email or by submitting a pull request with your proposed changes. We value the input of our users and are always looking for ways to enhance the tool. So, please don't hesitate to reach out and let us know your thoughts!

## License

This project is licensed under the Creative Commons Attribution 4.0 license, which allows others to use and modify the code as long as proper attribution is given. If you use this project in your work, please make sure to include a reference to this repository and its creators.