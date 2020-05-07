import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cinnamon_sdk",
    version="0.0.1",
    author="Rob McAuley",
    author_email="rmcauley@adgorithmics.com",
    description="SDK for using the Cinnamon GraphQL API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adgorithmics-inc/cinnamon-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
