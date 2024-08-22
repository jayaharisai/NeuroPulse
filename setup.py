from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # list your dependencies here
    ],
    author="Jayaharisai Tothala",
    author_email="jayaharisai1212@gmail.com",
    description="A short description of the package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jayaharisai/NeuroPulse.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)