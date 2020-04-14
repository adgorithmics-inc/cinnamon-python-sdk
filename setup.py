import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cinnamon-sdk",
    version="0.0.1",
    author="Adgorithmics, Inc",
    description="Adgorithmics Cinnamon API SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.adgo.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
