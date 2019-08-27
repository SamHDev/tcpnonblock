import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tcpnonblock",
    version="0.1.0",
    author="SamHDev",
    author_email="sam02h.huddart@gmail.com",
    description="A Simple Implementation of Non-Blocking TCP Socket Server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamHDev/tcpnonblock",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)
