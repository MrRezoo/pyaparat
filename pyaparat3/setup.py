import setuptools

with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyaparat3", # Replace with your own username
    version="0.0.1",
    author="Mr.Rezoo",
    author_email="rezam578@gmail.com",
    description="download aparat videos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrRezoo/pyaparat.git",
    install_requires=[
        'requests', 'beautifulsoup4'
    ],
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)