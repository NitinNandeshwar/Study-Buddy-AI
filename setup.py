from setuptools import setup,find_packages
from pathlib import Path

# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()

this_dir = Path(__file__).parent
requirements = (this_dir / "requirements.txt").read_text().splitlines()

setup(
    name="LLMOPS-Study-Buddy-AI",
    version="0.1",
    author="Nitin Nandeshwar",
    packages=find_packages(),
    install_requires = requirements,
)