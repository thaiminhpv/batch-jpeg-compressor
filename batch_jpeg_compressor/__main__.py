import sys
from pathlib import Path
from .batch_jpeg_compressor import compress_images

begin_directory = Path.absolute(Path(sys.argv[1]))
target_directory = Path.absolute(Path(sys.argv[2]))

compress_images(
    begin_directory=begin_directory, target_directory=target_directory, quality=30
)

print("done!")
