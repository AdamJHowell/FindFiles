import os
import fnmatch
from datetime import datetime
from pathlib import Path

from typing import List

"""
Data structure:
  absolute_path_to_file: str  # This will be the absolute path with the filename.
  file_path: List[pathlib.PurePath, pathlib.PurePosixPath, pathlib.PureWindowsPath, pathlib.Path, pathlib.PosixPath, pathlib.WindowsPath]
  file_name: str
  file_extension: str
os.walk() returns a 3-tuple:
  dirpath is a string, the path to the directory.  
  dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..').
  filenames is a list of the names of the non-directory files in dirpath.
"""


def find_files_by_extension( directory: str, extensions: List[str] ) -> List[str]:
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


def find_all_files( root_dir: str ) -> List[str]:
  """
  List all files in the specified directory.
  """
  all_files = []
  for dirpath, dirnames, filenames in os.walk( root_dir ):
    print( f"dirpath type: {type( dirpath )}" )
    print( f"dirnames type: {type( dirnames )}" )
    print( f"filenames type: {type( filenames )}" )
    # Convert the dirpath to a Path object
    pathlib_dirpath = Path( dirpath )
    all_files.extend( filenames )

    # Optionally convert dirnames and filenames to Path objects
    dirnames = [pathlib_dirpath / dirname for dirname in dirnames]
    filenames = [pathlib_dirpath / filename for filename in filenames]

    # Now you can use the Path object and its methods
    print( f"Directory: {dirpath}" )
    print( f"  Subdirectories: {dirnames}" )
    for dirname in dirnames:
      print( f"    dirname type: {type( dirname )}" )
      print( f"    dirname: {dirname}" )
    print( f"  Files: {filenames}" )
    for filename in filenames:
      print( f"    filename: {type( filename )}" )
      print( f"    filename: {filename}" )
    print()
  return all_files


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

  find_all_files( current_directory )
  raise SystemExit( 0 )

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
