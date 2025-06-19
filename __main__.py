'''
@description: Entry point for the filesync package.
'''

import filesync.cli as cli
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    cli.main()