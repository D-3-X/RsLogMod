# RsLogMod

**RsLogMod** is a flexible and powerful Python logging module designed to help manage log files with features such as log rotation, customizable log paths, and various log levels. It's designed to be simple to use while offering extensive customization options.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Default Behavior](#default-behavior)
- [Log Levels & Prefixes](#log-levels--prefixes)
- [Customization](#customization)
  - [Set Log Folder Path](#set-log-folder-path)
  - [Set Archive Folder Path](#set-archived-log-folder-path)
  - [Set Maximum Log Size](#set-maximum-log-size)
  - [Enable or Disable Log Rotation](#enable-or-disable-log-rotation)
  - [Display Configuration](#display-configuration)
- [Configuration](#configuration)
- [License](#license)

## Installation

To install the module:

```bash
pip install rslogmod
```

Import the module into your project:

```python
from RsLogMod import rlog, Configure
```

## Getting Started

Here’s a quick example to get you started with logging:

```python
from RsLogMod import rlog, Configure

# set a folder path this path will be saved in the rlogmod config file so this only needs to be done once
Configure.set_log_folder_path('path/to/target/folder')

# Log a simple message
rlog(log_name='my_log', log_level=1, log_entry='This is a log entry.')
```

### Explanation

- **`log_name`**: The name of the log file (e.g., `my_log`).
- **`log_level`**: The log level, where `1` corresponds to `INFO`.
- **`log_entry`**: The message you want to log.

This will create a log file named `my_log.log` (if it doesn't already exist) in the configured directory with the entry formatted as shown below.

### Example Output

If the example above is executed with `log_level=1`, the log entry will look like this in the log file:

```
[INFO] 2024-12-02 13:20: This is a log entry.
```

Here’s how the output would differ for each log level:

- **`log_level=0`**: `[DEBUG] 2024-12-02 13:20: This is a log entry.`
- **`log_level=1`**: `[INFO] 2024-12-02 13:20: This is a log entry.`
- **`log_level=2`**: `[ERROR] 2024-12-02 13:20: This is a log entry.`
- **`log_level=3`**: `[CRITICAL] 2024-12-02 13:20: This is a log entry.`
- **`log_level=4`**: `[SEC-ALERT] 2024-12-02 13:20: This is a log entry.`
- **`log_level=5`**: `[SEC-BREACH] 2024-12-02 13:20: This is a log entry.`

## Default Behavior

RsLogMod comes with the following default behaviors:

1. **Log Rotation Enabled by Default**: Log rotation is enabled by default. This means that when a log file reaches the maximum size, it will automatically be archived, and a new log file will be created.

2. **Default Maximum Log Size**: The default maximum log file size is set to 50 MB. This can be adjusted using the configuration settings.

3. **No Log Folder Path Set**: If you do not set a log folder path using the `Configure.set_log_folder_path()` method, RsLogMod will **only log to the terminal** and will not create any log files. 

4. **Configuration Persistence**: Once you set the log folder path, this path will be stored in the `configs.json` file, and all subsequent logs will be written to files within that directory. You only need to set the log folder path once; it will persist across sessions unless explicitly changed.

These defaults ensure that RsLogMod is ready to use out of the box, but also easily customizable for different environments and needs.

## Log Levels & Prefixes

RsLogMod supports several log levels, each with its own prefix:

- **`0`**: `[DEBUG]`  
  - For detailed debugging information.
- **`1`**: `[INFO]`  
  - For general information about program execution.
- **`2`**: `[ERROR]`  
  - For errors that occur during execution.
- **`3`**: `[CRITICAL]`  
  - For critical issues that need immediate attention.
- **`4`**: `[SEC-ALERT]`  
  - For security-related alerts.
- **`5`**: `[SEC-BREACH]`  
  - For security breaches or serious security issues.

## Customization

To customize how `RsLogMod` operates, such as changing the log file directory, archived log folder path, setting the maximum log file size, or enabling log rotation, you can use the `Configure` class.

### Set Log Folder Path

```python
from RsLogMod import Configure

# Set log folder path
Configure.set_log_folder_path('/new/log/directory')
```

### Set Archived Log Folder Path


```python
from RsLogMod import Configure

# Set the path to the desired folder for storing old logs
Configure.set_archive_path('/new/archive/directory')
```

### Set Maximum Log Size

```python
from RsLogMod import Configure

# Set max size for log files to 20 MB
Configure.set_log_file_max_size(20)
```

### Enable or Disable Log Rotation

```python
from RsLogMod import Configure

# Enable log rotation
Configure.enable_log_rotation(True)
```

### Display Configuration

```python
from RsLogMod import Configure

# Display the current configuration
Configure.display()
```

### Explanation

- **`Configure`**: This class manages the configuration settings for RsLogMod, such as where log files are stored, how large they can grow before being rotated, and whether log rotation is enabled.
- **`set_log_folder_path(path: str)`**: Sets the directory where logs are saved.
- **`set_log_file_max_size(mega_bytes: int)`**: Sets the maximum size for log files in megabytes.
- **`enable_log_rotation(value: bool)`**: Enables or disables log rotation.
- **`display()`**: Prints the current configuration in a JSON format for easy viewing.

## Configuration

RsLogMod uses a `configs.json` file to store its settings. Here’s an example configuration file:

```json
{
  "log_rotation": true,
  "max_size_in_mega_bytes": 10,
  "log_folder": "/path/to/logs",
  "archive_folder": "/path/to/logs/archived"
}
```

- **log_rotation**: Enables or disables log rotation.
- **max_size_in_mega_bytes**: The maximum size of a log file before it is rotated.
- **log_folder**: The directory where log files will be stored.
- **archive_folder**: The directory where old log files will be stored after rotation.

These settings can be updated programmatically using the `Configure` class, as shown in the examples above.

## License

This project is licensed under the [MIT License](https://github.com/D-3-X/Rodent-REPO/blob/main/licenses/MIT_License.txt). See the LICENSE file for details.