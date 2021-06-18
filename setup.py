import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MacTmp",
    version="0.0.9",
    author="Kethan",
    author_email="kethan@vegunta.com",
    description="A package used to get temperatures on Mac OS Machines. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.3',
)
