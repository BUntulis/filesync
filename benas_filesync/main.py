'''
@description: Entry point for the filesync package.
'''
from .utils.logging_utils import setup_logging, logging
from .filesyncmanager import FileSyncManager
from .utils.cli_utils import parse_args
import os


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
