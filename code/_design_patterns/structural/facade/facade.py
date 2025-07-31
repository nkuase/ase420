class VideoFile(object): 
  def __init__(self, file):
    self.file = file  
class OggCompressionCodec(object): 
  def __init__(self, file):
    self.file = file
  def convert(self):
    print(f"Converting to Ogg")
class MPEG4CompressionCodec(object): 
  def __init__(self, file):
    self.file = file
  def convert(self):
    print(f"Converting to Mp4")

## Facade
class VideoConverterFacade(object):
  def convert(self, filename, format):
    file = VideoFile(filename)
    if format == "mp4":
      destinationCodec = MPEG4CompressionCodec(file)
    else:
      destinationCodec = OggCompressionCodec(file)
    destinationCodec.convert()

# Driver
file = VideoFile("abc")
converter = VideoConverterFacade()
converter.convert(file, "mp4")