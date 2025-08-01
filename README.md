# benas_filesync

Automated README generated from docstrings.

# Setup Instructions:

## Option 1: Install from PyPI (recommended)

**Install the package using pip:**
```bash
pip install benas-filesync
```

**Run synchronization**
```bash
filesync --source ./path_source/ --backup ./path_backup/ --versioning ./path_versioning/
```


## Option  2: Install from source (development mode)
**Clone the repository:**
```bash
git clone https://github.com/BUntulis/filesync
cd filesync
```

**(Optional) Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Make the package executable (optional, for CLI usage)**
```bash
pip install -e .
```

**Run synchronization**
```bash
filesync --source ./path_source/ --backup ./path_backup/ --versioning ./path_versioning/
```

# Code Documentation:


# setup.py
@description: Setup script for the filesync package.







# benas_filesync\filesyncmanager.py
@author: Benas Untulis
@description:
- FileSyncManager class for managing file synchronization between source, backup, and versioning directories.



## Class: FileSyncManager
**Purpose:** 
- A class to manage file synchronization between a source directory, a backup directory, and a versioning directory.
This class provides methods to retrieve .txt files, compute file hashes, check if files should be synchronized,
and perform the synchronization process.

**Attributes:**
- ``source (str)``: Path to the source directory containing .txt files.
- ``backup (str)``: Path to the backup directory where files will be copied.
- ``versioning (str)``: Path to the versioning directory where old versions will be stored.
- ``dry_run (bool)``: If True, preview actions without making changes.
- ``modified_within (int)``: If specified, only sync files modified within the last N minutes.
- ``logger (logging.Logger)``: Logger instance for logging actions and errors.

**Example:**
```python
>>> manager = FileSyncManager('/path/to/source', '/path/to/backup', '/path/to/versioning', dry_run=True, modified_within=60)
>>> manager.sync()
```

Example Output:
- logging: Copying new file: example.txt
- logging: Versioning: example.txt → example_20231001T123456.txt
- logging: Skipped (unchanged): unchanged_file.txt

```python
>>> print(manager.get_txt_files())
```
Example Output:
- ['file1.txt', 'file2.txt', 'file3.txt']

```python
>>> print(manager.hash_file('/path/to/file.txt'))
```
Example Output:
- 'abc123def456...'

```python
>>> print(manager.should_sync('/path/to/source/file.txt', '/path/to/backup/file.txt'))
```
Example Output:
- ``True``  # If the files differ or backup does not exist
- ``False`` # If the files are identical



### Methods:


### __init__(): 
**Purpose:** 
- Initialize the FileSyncManager with source, backup, and versioning directories.

**Args:**
- ``source (str)``: Path to the source directory containing .txt files.
- ``backup (str)``: Path to the backup directory where files will be copied.
- ``versioning (str)``: Path to the versioning directory where old versions will be stored.
- ``dry_run (bool)``: If True, preview actions without making changes.
- ``modified_within (int)``: If specified, only sync files modified within the last N minutes.




### get_txt_files(): 
**Purpose:** 
- Retrieve all .txt files from the specified directory.

**Args:**
- ``self``: Instance of the FileSyncManager class.
    
    - **Used Parameters:**
        - The following parameters can be set when creating an instance of the FileSyncManager class:
        
        - ``source (str)``: The directory path to search for .txt files.

**Returns:**
- ``list``: A list of .txt filenames in the specified directory.

**Example:**
```python
>>> get_txt_files('/path/to/directory')
```
Example Output:
- ['file1.txt', 'file2.txt']

**Raises:**
 - ``FileNotFoundError``: If the specified path does not exist.
- ``ValueError``: If the specified path is not a directory.
- ``RuntimeError``: If there is an error reading the directory.




### hash_file(): 
**Purpose:** 
- Compute the SHA-256 hash of a file to determine if it has changed.

**Args:**
- ``self``: Instance of the FileSyncManager class.
- ``filepath (str)``: The path to the file to be hashed.

**Returns:**
 - ``str``: The SHA-256 hash of the file as a hexadecimal string.

**Example:**
```python
>>> hash_file('/path/to/file.txt')
```
Example Output:
- '3a1f4b2c5d6e7f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2u3v4w5x6y7z8a9b0c1d2'

**Raises:**
- ``FileNotFoundError``: If the specified file does not exist.
- ``ValueError``: If the specified path is not a file.
- ``RuntimeError``: If there is an error reading the file.




### should_sync(): 
**Purpose:** 
- Determine if a file should be synchronized between source and backup locations.

**Args:**
- ``self``: Instance of the FileSyncManager class.
- ``source_path (str)``: The path to the source file.
- ``backup_path (str)``: The path to the backup file.

**Returns:**
- ``bool``: True if the file should be synchronized, False otherwise.

**Example:**
```python
>>> should_sync('/path/to/source/file.txt', '/path/to/backup/file.txt')
```
Example Output:
- ``True``  # If the files differ or backup does not exist
- ``False`` # If the files are identical
        
**Raises:**
    - ``FileNotFoundError``: If the source file does not exist.
    - ``ValueError``: If the source or backup path is not a file.
    - ``RuntimeError``: If there is an error comparing the files.




### sync(): 
**Purpose:** 
 - Synchronize .txt files from the source directory to the backup directory and manage versioning.

 **Args:**
 - ``self``: Instance of the FileSyncManager class.

     - **Used Parameters:**
         - The following parameters can be set when creating an instance of the FileSyncManager class:

         - ``source (str)``: Path to the source directory containing .txt files.
         - ``backup (str)``: Path to the backup directory where files will be copied.
         - ``versioning (str)``: Path to the versioning directory where old versions will be stored.
         - ``dry_run (bool)``: If True, preview actions without making changes.
         - ``modified_within (int)``: If specified, only sync files modified within the last N minutes.

**Returns:**
 - ``None``

 **Example:**
 ```python
 >>> sync_files('/path/to/source', '/path/to/backup', '/path/to/versioning', dry_run=True, modified_within=60)
 ```
 Example Output:
 - ``logging``: Copying new file: example.txt
 - ``logging``: Versioning: example.txt → example_20231001T123456.txt
 - ``logging``: Skipped (unchanged): unchanged_file.txt

 **Raises:**
 - ``RuntimeError``: If there are issues with file operations (e.g., copying, moving, hashing).
 - ``PermissionError``: If there are insufficient permissions to read/write files.
 - ``FileNotFoundError``: If the source directory does not exist.
 - ``ValueError``: If the source or backup path is not a directory.
 - ``OSError``: If there are issues with file operations (e.g., permission denied, disk full).











# benas_filesync\main.py
@description: Entry point for the filesync package.





## Functions:


### main(): 
**Purpose:** 
- Main function to execute the file synchronization script.
This function parses command-line arguments, sets up logging, and calls the `sync_files` function
with the provided arguments. It handles exceptions and logs errors if the script fails.

**Raises:**
- ``SystemExit``: If the script encounters an error during execution.
- ``ValueError``: If the provided paths are not valid directories.
- ``RuntimeError``: If there are issues with file operations (e.g., copying, moving, hashing).
- ``PermissionError``: If there are insufficient permissions to read/write files.







# benas_filesync\__init__.py
@description: This module is main entry point for the filesync package.







# benas_filesync\utils\cli_utils.py
@author: Benas Untulis
@description:
- Command-line interface for the file synchronization script.





## Functions:


### parse_args(): 
**Purpose:**
- Parse command-line arguments for the file synchronization script.

**Returns:**
- ``argparse.Namespace``: The parsed command-line arguments.

**Example:**
```python
>>> args = parse_args()
>>> print(args.source)
```
Example Output:
- /path/to/source

```python
>>> print(args.backup)
```
Example Output:            
- /path/to/backup

```python
>>> print(args.versioning)
```
Example Output:
- /path/to/versioning

**Raises:**
- ``SystemExit``: If the required arguments are not provided or if the arguments are invalid







# benas_filesync\utils\logging_utils.py






## Functions:


### setup_logging(): 
**Purpose:** 
- Configures logging for the script based on the specified log type and file.

**Parameters:**
- `log_type` (str): Specifies the type of logging to use. Options are 'none', 'console', 'file', or 'both'.
- `log_file` (str): The file path where logs will be written if `log_type` is 'file' or 'both'.

**Raises:**
- `ValueError`: If `log_type` is not one of the expected values
- `OSError`: If file handler creation fails (e.g., due to permission issues or invalid path)







# build\lib\benas_filesync\cli.py
@author: Benas Untulis
@description:
- Command-line interface for the file synchronization script.





## Functions:


### parse_args(): 
**Purpose:**
- Parse command-line arguments for the file synchronization script.

**Returns:**
- ``argparse.Namespace``: The parsed command-line arguments.

**Example:**
```python
>>> args = parse_args()
>>> print(args.source)
```
Example Output:
- /path/to/source

```python
>>> print(args.backup)
```
Example Output:            
- /path/to/backup

```python
>>> print(args.versioning)
```
Example Output:
- /path/to/versioning

**Raises:**
- ``SystemExit``: If the required arguments are not provided or if the arguments are invalid







# build\lib\benas_filesync\main.py
@description: Entry point for the filesync package.





## Functions:


### setup_logging(): 





### main(): 
**Purpose:** 
- Main function to execute the file synchronization script.
This function parses command-line arguments, sets up logging, and calls the `sync_files` function
with the provided arguments. It handles exceptions and logs errors if the script fails.

**Raises:**
- ``SystemExit``: If the script encounters an error during execution.
- ``ValueError``: If the provided paths are not valid directories.
- ``RuntimeError``: If there are issues with file operations (e.g., copying, moving, hashing).
- ``PermissionError``: If there are insufficient permissions to read/write files.







# build\lib\benas_filesync\manager.py
@author: Benas Untulis
@description:
- FileSyncManager class for managing file synchronization between source, backup, and versioning directories.



## Class: FileSyncManager
**Purpose:** 
- A class to manage file synchronization between a source directory, a backup directory, and a versioning directory.
This class provides methods to retrieve .txt files, compute file hashes, check if files should be synchronized,
and perform the synchronization process.

**Attributes:**
- ``source (str)``: Path to the source directory containing .txt files.
- ``backup (str)``: Path to the backup directory where files will be copied.
- ``versioning (str)``: Path to the versioning directory where old versions will be stored.
- ``dry_run (bool)``: If True, preview actions without making changes.
- ``modified_within (int)``: If specified, only sync files modified within the last N minutes.
- ``logger (logging.Logger)``: Logger instance for logging actions and errors.

**Example:**
```python
>>> manager = FileSyncManager('/path/to/source', '/path/to/backup', '/path/to/versioning', dry_run=True, modified_within=60)
>>> manager.sync()
```

Example Output:
- logging: Copying new file: example.txt
- logging: Versioning: example.txt → example_20231001T123456.txt
- logging: Skipped (unchanged): unchanged_file.txt

```python
>>> print(manager.get_txt_files())
```
Example Output:
- ['file1.txt', 'file2.txt', 'file3.txt']

```python
>>> print(manager.hash_file('/path/to/file.txt'))
```
Example Output:
- 'abc123def456...'

```python
>>> print(manager.should_sync('/path/to/source/file.txt', '/path/to/backup/file.txt'))
```
Example Output:
- ``True``  # If the files differ or backup does not exist
- ``False`` # If the files are identical



### Methods:


### __init__(): 
**Purpose:** 
- Initialize the FileSyncManager with source, backup, and versioning directories.

**Args:**
- ``source (str)``: Path to the source directory containing .txt files.
- ``backup (str)``: Path to the backup directory where files will be copied.
- ``versioning (str)``: Path to the versioning directory where old versions will be stored.
- ``dry_run (bool)``: If True, preview actions without making changes.
- ``modified_within (int)``: If specified, only sync files modified within the last N minutes.




### get_txt_files(): 
**Purpose:** 
- Retrieve all .txt files from the specified directory.

**Args:**
- ``self``: Instance of the FileSyncManager class.
    
    - **Used Parameters:**
        - The following parameters can be set when creating an instance of the FileSyncManager class:
        
        - ``source (str)``: The directory path to search for .txt files.

**Returns:**
- ``list``: A list of .txt filenames in the specified directory.

**Example:**
```python
>>> get_txt_files('/path/to/directory')
```
Example Output:
- ['file1.txt', 'file2.txt']

**Raises:**
 - ``FileNotFoundError``: If the specified path does not exist.
- ``ValueError``: If the specified path is not a directory.
- ``RuntimeError``: If there is an error reading the directory.




### hash_file(): 
**Purpose:** 
- Compute the SHA-256 hash of a file to determine if it has changed.

**Args:**
- ``self``: Instance of the FileSyncManager class.
- ``filepath (str)``: The path to the file to be hashed.

**Returns:**
 - ``str``: The SHA-256 hash of the file as a hexadecimal string.

**Example:**
```python
>>> hash_file('/path/to/file.txt')
```
Example Output:
- '3a1f4b2c5d6e7f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2u3v4w5x6y7z8a9b0c1d2'

**Raises:**
- ``FileNotFoundError``: If the specified file does not exist.
- ``ValueError``: If the specified path is not a file.
- ``RuntimeError``: If there is an error reading the file.




### should_sync(): 
**Purpose:** 
- Determine if a file should be synchronized between source and backup locations.

**Args:**
- ``self``: Instance of the FileSyncManager class.
- ``source_path (str)``: The path to the source file.
- ``backup_path (str)``: The path to the backup file.

**Returns:**
- ``bool``: True if the file should be synchronized, False otherwise.

**Example:**
```python
>>> should_sync('/path/to/source/file.txt', '/path/to/backup/file.txt')
```
Example Output:
- ``True``  # If the files differ or backup does not exist
- ``False`` # If the files are identical
        
**Raises:**
    - ``FileNotFoundError``: If the source file does not exist.
    - ``ValueError``: If the source or backup path is not a file.
    - ``RuntimeError``: If there is an error comparing the files.




### sync(): 
**Purpose:** 
 - Synchronize .txt files from the source directory to the backup directory and manage versioning.

 **Args:**
 - ``self``: Instance of the FileSyncManager class.

     - **Used Parameters:**
         - The following parameters can be set when creating an instance of the FileSyncManager class:

         - ``source (str)``: Path to the source directory containing .txt files.
         - ``backup (str)``: Path to the backup directory where files will be copied.
         - ``versioning (str)``: Path to the versioning directory where old versions will be stored.
         - ``dry_run (bool)``: If True, preview actions without making changes.
         - ``modified_within (int)``: If specified, only sync files modified within the last N minutes.

**Returns:**
 - ``None``

 **Example:**
 ```python
 >>> sync_files('/path/to/source', '/path/to/backup', '/path/to/versioning', dry_run=True, modified_within=60)
 ```
 Example Output:
 - ``logging``: Copying new file: example.txt
 - ``logging``: Versioning: example.txt → example_20231001T123456.txt
 - ``logging``: Skipped (unchanged): unchanged_file.txt

 **Raises:**
 - ``RuntimeError``: If there are issues with file operations (e.g., copying, moving, hashing).
 - ``PermissionError``: If there are insufficient permissions to read/write files.
 - ``FileNotFoundError``: If the source directory does not exist.
 - ``ValueError``: If the source or backup path is not a directory.
 - ``OSError``: If there are issues with file operations (e.g., permission denied, disk full).











# build\lib\benas_filesync\__init__.py
@description: This module is main entry point for the filesync package.







# build\lib\tests\test_manager.py
@author: Benas Untulis
@description:
- Unit tests for the FileSyncManager class, covering various scenarios such as copying new files,
    skipping unchanged files, versioning on changes, and filtering by modification time.



## Class: TestFileSyncManager
Test suite for ``FileSyncManager`` class.



### Methods:


### setUp(): 
**Purpose:**
- Setup temporary directories for source, backup, and versioning before each test.

**Functionality:**
- Creates temporary directories and initializes a FileSyncManager instance with dry_run=False.




### tearDown(): 
**Purpose:** 
- Cleanup temporary directories after each test.

**Functionality:**
- Removes all temporary directories created in setUp.




### create_file(): 
**Purpose:** 
- Helper method to create a file with specified content.

**Args:**
- ``dir_path (str)``: Directory path to create the file in.
- ``filename (str)``: Name of the file to create.
- ``content (str)``: Text content to write into the file.

**Returns:**
- ``str``: Full path to the created file.




### test_copy_new_file(): 
**Purpose:** 
- Test that a new file in source is copied to backup if it doesn't exist there.

**Functionality steps:**
- Create a new file in the source directory.
- Run sync.
- Assert the file exists in backup.




### test_skip_unchanged_file(): 
**Purpose:** 
- Test that unchanged files are skipped (not copied or versioned).

**Functionality steps:**
- Create identical files in source and backup.
- Run sync.
- Assert file remains in backup.
- Assert versioning directory is empty.




### test_versioning_on_change(): 
**Purpose:** 
- Test that when a file is changed, the old backup is moved to versioning and source is copied to backup.

**Functionality steps:**
- Create a file in source with new content.
- Create a file in backup with old content.
- Run sync.
- Assert backup file updated with new content.
- Assert versioning contains the old version with timestamp.




### test_modified_within_filter(): 
**Purpose:** 
- Test that files modified outside the 'modified_within' window are skipped.

**Functionality steps:**
- Create a file in source with an old modification time.
- Set modified_within to less than the file's age.
- Run sync.
- Assert file is not copied to backup.











# build\lib\tests\__init__.py
@description: This module is used to run all tests in the filesync package.







# tests\test_manager.py
@author: Benas Untulis
@description:
- Unit tests for the FileSyncManager class, covering various scenarios such as copying new files,
    skipping unchanged files, versioning on changes, and filtering by modification time.



## Class: TestFileSyncManager
Test suite for ``FileSyncManager`` class.



### Methods:


### setUp(): 
**Purpose:**
- Setup temporary directories for source, backup, and versioning before each test.

**Functionality:**
- Creates temporary directories and initializes a FileSyncManager instance with dry_run=False.




### tearDown(): 
**Purpose:** 
- Cleanup temporary directories after each test.

**Functionality:**
- Removes all temporary directories created in setUp.




### create_file(): 
**Purpose:** 
- Helper method to create a file with specified content.

**Args:**
- ``dir_path (str)``: Directory path to create the file in.
- ``filename (str)``: Name of the file to create.
- ``content (str)``: Text content to write into the file.

**Returns:**
- ``str``: Full path to the created file.




### test_copy_new_file(): 
**Purpose:** 
- Test that a new file in source is copied to backup if it doesn't exist there.

**Functionality steps:**
- Create a new file in the source directory.
- Run sync.
- Assert the file exists in backup.




### test_skip_unchanged_file(): 
**Purpose:** 
- Test that unchanged files are skipped (not copied or versioned).

**Functionality steps:**
- Create identical files in source and backup.
- Run sync.
- Assert file remains in backup.
- Assert versioning directory is empty.




### test_versioning_on_change(): 
**Purpose:** 
- Test that when a file is changed, the old backup is moved to versioning and source is copied to backup.

**Functionality steps:**
- Create a file in source with new content.
- Create a file in backup with old content.
- Run sync.
- Assert backup file updated with new content.
- Assert versioning contains the old version with timestamp.




### test_modified_within_filter(): 
**Purpose:** 
- Test that files modified outside the 'modified_within' window are skipped.

**Functionality steps:**
- Create a file in source with an old modification time.
- Set modified_within to less than the file's age.
- Run sync.
- Assert file is not copied to backup.











# tests\__init__.py
@description: This module is used to run all tests in the filesync package.





