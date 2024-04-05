import os
import fnmatch
from datetime import datetime

from typing import List


def find_audio_files( directory: str, extensions: List[str] ) -> List[str]:
  """
  List all files in the specified directory and its subdirectories that have the given extensions.
  """
  audio_files = []
  for root, dirs, files in os.walk( directory ):
    for extension in extensions:
      for filename in fnmatch.filter( files, f'*.{extension}' ):
        audio_files.append( os.path.join( root, filename ) )
  return audio_files


if __name__ == "__main__":
  output_filename = "music-" + datetime.now().isoformat() + ".txt"
  output_filename = output_filename.replace( ":", "." )
  # Use the current working directory as the starting point, or replace it with the desired directory path.
  current_directory = os.getcwd()
  # A list of all audio file extensions to look for.
  extension_list = ["flac", "m4a", "mp3", "wav", "aac", "ogg"]
  results_string = ""
  for audio_file in find_audio_files( current_directory, extension_list ):
    print( audio_file )
    results_string += audio_file + "\n"
  with open( output_filename, 'w', encoding = 'utf-8', newline = '\n' ) as key_file:
    write_bytes = key_file.write( results_string )
