'''
@author: Benas Untulis
@description:
- Generates an automated README.md file for the project by extracting documentation from Python files.
'''

import os
import ast
from pathlib import Path
from jinja2 import Template

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "readme_template.md.j2"

def extract_doc_info(py_path: Path) -> dict:
    """
    Parses a Python file and extracts all doc-related content for documentation purposes.

    This is used to build an automated README by scanning each .py file for:
    - Module-level docstring
    - Classes and their methods (with docstrings)
    - Standalone functions (with docstrings)

    **Args:**
    - ``py_path`` (Path): Path to the Python file being processed.

    Returns a ``dict`` with:
    - ``file``: filename
    - ``path``: relative path
    - ``doc``: module docstring
    - ``classes``: list of classes with name, doc, methods
    - ``functions``: list of functions with name and doc
    """

    with open(py_path, encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=py_path.name)

    module_doc = ast.get_docstring(tree) or ""
    classes = []
    functions = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_doc = ast.get_docstring(node) or ""
            methods = []
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    methods.append({
                        "name": item.name,
                        "doc": (ast.get_docstring(item) or "").strip(),
                    })
            classes.append({
                "name": node.name,
                "doc": class_doc.strip(),
                "methods": methods,
            })
        elif isinstance(node, ast.FunctionDef):
            functions.append({
                "name": node.name,
                "doc": (ast.get_docstring(node) or "").strip(),
            })

    if not (module_doc or classes or functions):
        return None

    return {
        "file": py_path.name,
        "path": str(py_path.relative_to(BASE_DIR)),
        "doc": module_doc.strip(),
        "classes": classes,
        "functions": functions,
    }

def get_structure(path: str, prefix: str = "") -> str:
    """
    Builds a visual (text-based) tree of the project's folder structure.

    This is rendered into the README for a quick overview of the project layout.

    **Args:**
    - ``path`` (str): Starting directory path.
    - ``prefix`` (str): Indentation prefix for nested files/folders.

    **Returns:**
    - ``str``: Formatted directory tree as a string.
    """

    tree = ""
    for item in sorted(os.listdir(path)):
        if item.startswith(".") or item in ["venv", "__pycache__", ".git"]:
            continue
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            tree += f"{prefix}{item}/\n"
            tree += get_structure(full_path, prefix + "    ")
        else:
            tree += f"{prefix}{item}\n"
    return tree

def gather_all_docs() -> list[dict]:
    """
    Walks through the entire project directory and processes all .py files
    (excluding itself), collecting structured documentation info.

    Useful for compiling a full project API overview.

    **Returns:**
    - ``list[dict]``: List of documentation entries (one per valid Python file).
    """

    docs = []
    for root, _, files in os.walk(BASE_DIR):
        for fname in files:
            if fname.endswith(".py") and fname != Path(__file__).name:
                fpath = Path(root) / fname
                info = extract_doc_info(fpath)
                if info:
                    docs.append(info)
    return docs

def generate_readme() -> None:
    """
    Generates the README.md file using a Jinja2 template and dynamic project metadata.

    **This includes:**
    - Extracting installed apps from Django settings
    - Building file structure overview
    - Collecting all documented classes/functions

    **Returns:**
    - ``None``
    """

    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        template = Template(f.read())

    context = {
        "project_name": BASE_DIR.name,
        "description": "Automated README generated from docstrings.",
        "structure": get_structure(BASE_DIR),
        "modules": gather_all_docs(),
    }

    readme_content = template.render(context)

    with open(BASE_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README.md generated!")

if __name__ == "__main__":
    generate_readme()
