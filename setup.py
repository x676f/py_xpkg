# coding:utf-8
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="xpkg",
    version="0.1.0",
    author="x676f@github",
    author_email="66930525+x676f@users.noreply.github.com",
    description="Packages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x676f/py_xpkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
