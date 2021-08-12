import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="batch_jpeg_compressor",
    scripts=["batch_jpeg_compressor"],
    version="0.1",
    license="MIT",
    description="This is a CLI tool to compress multiple images (JPEG or PNG) at once using python",
    author="thaiminhpv",
    author_email="thaiminhpv@gmail.com",
    url="https://github.com/thaiminhpv/batch-jpeg-compressor",
    download_url="https://github.com/thaiminhpv/batch-jpeg-compressor/archive/refs/tags/v0.1.tar.gz",
    keywords=[
        "compressor",
        "jpeg",
        "jpg",
        "image processing",
    ],
    install_requires=[
        "Pillow",
        "tqdm",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Image Processing :: Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
