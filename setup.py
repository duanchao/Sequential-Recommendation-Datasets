import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="srdatasets",
    version="0.0.1",
    author="Cheng Guo",
    author_email="guocheng672@gmail.com",
    description="A collection of research ready datasets for sequential recommendation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guocheng2018/sequential-recommendation-datasets",
    packages=["srdatasets"],
    python_requires=">=3.5",
    install_requires=["pandas>=0.25.0", "tqdm>=4.32.2", "tabulate>=0.8.5"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)