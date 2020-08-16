import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="froud-python",
    version="0.1.0",
    author="Maxime ANDRÉ",
    author_email="maxime.andre1986@gmail.com",
    description="A Python library inspired by Flow-Based Programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/max22-/froud-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)