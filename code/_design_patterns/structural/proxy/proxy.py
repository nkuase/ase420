# Interface 
class ThirdPartyYouTubeLib(object):
  def list_videos(self): pass
  def get_video_info(self, id): pass
  def download_video(self, id): pass
    
# Real Lib    
class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
  def list_videos(self): print("list videos A, B, C")
  def get_video_info(self, id): print(f"get video info {id}")
  def download_video(self, id): print(f"download video {id}") 
  def operational(self): return True # <- Change the return value  
    
# Proxy that aggregates the Lib    
class CachedYouTubeClass(ThirdPartyYouTubeLib):
  def __init__(self, lib):
    self.lib = lib
  def list_videos(self): 
    if self.check_access(): self.lib.list_videos()
    else: print("Wait for signal ...")
  def get_video_info(self, id): pass
  def download_video(self, id): pass
  def check_access(self):
    if self.lib.operational(): return True
    return False
   
# Driver    
youtube_service = ThirdPartyYouTubeClass()
youtube_proxy = CachedYouTubeClass(youtube_service)
youtube_proxy.list_videos()