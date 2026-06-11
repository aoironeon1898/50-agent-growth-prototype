"""setup.py - Package configuration"""

from setuptools import setup, find_packages

setup(
    name="recursive-growth-agent",
    version="0.1.0",
    description="Controlled recursive-growth agent prototype",
    author="Copilot",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": ["pytest>=6.0"],
    },
    entry_points={
        "console_scripts": [
            "growth-agent=main:main",
        ],
    },
)
