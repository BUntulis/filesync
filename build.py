from dotenv import load_dotenv
import importlib.metadata
import subprocess
import sys
import os

load_dotenv()

subprocess.run([sys.executable, "setup.py", "sdist", "bdist_wheel"], check=True)


PACKAGE_NAME = "benas_filesync" 
version = importlib.metadata.version(PACKAGE_NAME)

whl_name = f"{PACKAGE_NAME.replace('-', '_')}-{version}-py3-none-any.whl"
whl_path = os.path.join("dist", whl_name, )

subprocess.run(["pip", "install", "--force-reinstall", whl_path])