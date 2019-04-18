import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pzdata",
    version="0.0.1",
    author="Luke Hargreaves",
    author_email="lukeharg@amazon.com",
    description="Personalize demo data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lukeharg/pzdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)
