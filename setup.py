from pathlib import Path

from setuptools import find_packages, setup


about: dict = {}
init_path = Path(__file__).parent / "smashup" / "__init__.py"
exec(init_path.read_text(encoding="utf-8"), about)


setup(
    name="smashup-cli",
    version=about["__version__"],
    description="Smash Up faction randomizer with TUI configuration.",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "click",
        "prompt_toolkit",
        "rich",
        "tomli; python_version < '3.11'",
    ],
    entry_points={"console_scripts": ["smashup=smashup.cli:main"]},
)
