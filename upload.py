from dotenv import load_dotenv
import subprocess

load_dotenv()

subprocess.run(["twine", "upload", "dist/*"])
