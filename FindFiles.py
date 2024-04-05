import os
import fnmatch
from datetime import datetime

from typing import List


def find_audio_files( directory: str, extensions: List[str] ) -> List[str]:
  """
  List all files in the specified directory and its subdirectories that have the given extensions.
  @param directory: The directory to search for audio files.
  @param extensions: The extensions to search for.
  @return: A list of audio files.
  """
  audio_files = []
  for root, dirs, files in os.walk( directory ):
    for extension in extensions:
      for filename in fnmatch.filter( files, f'*.{extension}' ):
        audio_files.append( os.path.join( root, filename ) )
  return audio_files


if __name__ == "__main__":
  program_name = "FindFiles"
  current_time = datetime.now().strftime( "%Y-%m-%dT%H.%M.%S" )
  print( f"{program_name} starting at {current_time}" )
  output_filename = "music-" + current_time + ".txt"

  # Use the current working directory as the starting point, or replace it with the desired directory path.
  current_directory = os.getcwd()

  # A list of all audio file extensions to look for.
  extension_list = ["flac", "m4a", "mp3", "wav", "aac", "ogg"]
  results_string = ""

  # Call find_audio_files and parse the returned list.
  for audio_file in find_audio_files( current_directory, extension_list ):
    results_string += audio_file + "\n"

  if len( results_string ) > 0:
    # Save the results to a file.
    with open( output_filename, 'w', encoding = 'utf-8', newline = '\n' ) as key_file:
      write_bytes = key_file.write( results_string )
      print( f"Wrote {write_bytes} bytes to {output_filename}" )
  else:
    print( f"No audio files found at {current_directory}" )
