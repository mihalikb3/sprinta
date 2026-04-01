import sys
from pathlib import Path

# Add the src directory to sys.path to resolve the sprinta package
src_path = str(Path(__file__).parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from sprinta.cli import app

if __name__ == "__main__":
    app()
