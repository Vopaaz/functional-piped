from setuptools import setup, find_packages

with open(r"README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open(r"requirements.txt", "r", encoding="utf-8") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="dot-map",
    version="0.0.1",
    author="Vopaaz",
    author_email="liyifan945@gmail.com",
    url="https://github.com/Vopaaz/dot-map",
    description="Write iterator.map(func) instead of map(func, iterator)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)
