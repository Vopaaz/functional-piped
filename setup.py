from setuptools import setup, find_packages

with open(r"README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="functional-piped",
    version="0.0.1",
    author="Vopaaz",
    author_email="liyifan945@gmail.com",
    url="https://github.com/Vopaaz/functional-piped",
    description="Write iterator.map(func) instead of map(func, iterator)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)
