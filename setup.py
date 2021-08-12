from distutils.core import setup

setup(
    name="batch_jpeg_compressor",  # How you named your package folder (MyLib)
    packages=["batch_jpeg_compressor"],  # Chose the same as "name"
    version="0.1",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="This is a CLI tool to compress multiple images (JPEG or PNG) at once using python",  # Give a short description about your library
    author="thaiminhpv",  # Type in your name
    author_email="thaiminhpv@gmail.com",  # Type in your E-Mail
    url="https://github.com/thaiminhpv/batch-jpeg-compressor",  # Provide either the link to your github or to your website
    download_url="blahblahblah",  # I explain this later on
    keywords=[
        "compressor",
        "jpeg",
        "jpg",
        "image processing",
    ],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        "Pillow",
        "tqdm",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Image Processing :: Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
