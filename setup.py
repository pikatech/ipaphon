import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ipaphon",
    version="0.0.1",
    author="Pikatech",
    author_email="pikatech@mail.de",
    description="A skeleton Flask app demonstrating how to process uploaded files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pikatech/ipaphon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Framework :: Flask",
    ],
    python_requires='>=3.6',
)
