import logging

def setup_logging(log_type, log_file) -> None:
    '''
    **Purpose:** 
    - Configures logging for the script based on the specified log type and file.

    **Parameters:**
    - `log_type` (str): Specifies the type of logging to use. Options are 'none', 'console', 'file', or 'both'.
    - `log_file` (str): The file path where logs will be written if `log_type` is 'file' or 'both'.

    **Raises:**
    - `ValueError`: If `log_type` is not one of the expected values
    - `OSError`: If file handler creation fails (e.g., due to permission issues or invalid path)
    '''
    if log_type == 'none':
        logging.disable(logging.CRITICAL)
        return

    if log_type not in ('console', 'file', 'both'):
        raise ValueError(f"Invalid log_type: {log_type}. Must be one of 'none', 'console', 'file', 'both'.")

    handlers = []
    try:
        if log_type in ('console', 'both'):
            handlers.append(logging.StreamHandler())
        if log_type in ('file', 'both'):
            handlers.append(logging.FileHandler(log_file, encoding='utf-8'))

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            handlers=handlers
        )
    except Exception as e:
        raise RuntimeError(f"Failed to set up logging: {e}")