'''
@author: Benas Untulis
@description:
- Command-line interface for the file synchronization script.
'''

import argparse
import logging
import os
from filesync.manager import FileSyncManager

def parse_args():
    '''
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
    '''

    parser = argparse.ArgumentParser(description="Synchronize .txt files with backup and versioning.")
    parser.add_argument('--source', required=True, help='Path to the source folder (Folder A)')
    parser.add_argument('--backup', required=True, help='Path to the backup folder (Folder B)')
    parser.add_argument('--versioning', required=True, help='Path to the versioning folder (Folder C)')
    parser.add_argument('--dry-run', action='store_true', help='Preview actions without making changes')
    parser.add_argument('--modified-within', type=int, help='Only sync files modified in the last N minutes')
    parser.add_argument(
        '--log-type',
        choices=['none', 'console', 'file', 'both'],
        default='console',
        help='Logging output: none (no logging), console, file, or both'
    )
    parser.add_argument(
        '--log-file',
        default='file_sync.log',
        help='Path to the log file (used if --log-type is file or both). Default: file_sync.log'
    )
    return parser.parse_args()

def setup_logging(log_type, log_file):
    if log_type == 'none':
        logging.disable(logging.CRITICAL)
        return

    handlers = []
    if log_type in ('console', 'both'):
        handlers.append(logging.StreamHandler())
    if log_type in ('file', 'both'):
        handlers.append(logging.FileHandler(log_file, encoding='utf-8'))

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=handlers
    )

def main():
    '''
    **Purpose:** 
    - Main function to execute the file synchronization script.
    This function parses command-line arguments, sets up logging, and calls the `sync_files` function
    with the provided arguments. It handles exceptions and logs errors if the script fails.
    
    **Raises:**
    - ``SystemExit``: If the script encounters an error during execution.
    - ``ValueError``: If the provided paths are not valid directories.
    - ``RuntimeError``: If there are issues with file operations (e.g., copying, moving, hashing).
    - ``PermissionError``: If there are insufficient permissions to read/write files.
    '''

    args = parse_args()

    setup_logging(args.log_type, args.log_file)

    try:
        if not all(os.path.isdir(p) for p in [args.source, args.backup, args.versioning]):
            raise ValueError("One or more provided paths are not valid directories.")

        syncer = FileSyncManager(
            source=args.source,
            backup=args.backup,
            versioning=args.versioning,
            dry_run=args.dry_run,
            modified_within=args.modified_within
        )
        syncer.sync()

    except Exception as e:
        logging.error(f"Script execution failed: {e}")
        exit(1)

if __name__ == "__main__":
    main()
