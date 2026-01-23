from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="app-string",
    version="1.2.0",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    description="Create a long string with all file paths and contents from an application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danilocgsilva/app_string",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "app-string=app_string.cli:main",
        ],
    },
)