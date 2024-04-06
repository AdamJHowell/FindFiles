import fnmatch
import os
from datetime import datetime
from pathlib import Path
from typing import List

"""
Data structure:
  absolute_path_to_file: str  # This will be the absolute path with the filename.
  relative_path_to_file: str  # This will be the absolute_path_to_file with the base directory removed.
  artist_dir: str  # This will be the folder designating the artist.
  album_dir: str  # This will be the folder designating the album.
  file_path: List[pathlib.PurePath, pathlib.PurePosixPath, pathlib.PureWindowsPath, pathlib.Path, pathlib.PosixPath, pathlib.WindowsPath]
  file_name: str  # This will be the file name with the extension.
  file_extension: str  # This is just the file extension, intended for sorting.
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
  all_files: List[str] = []
  dirpath: str
  dirnames: List[str]
  filenames: List[str]
  for dirpath, dirnames, filenames in os.walk( root_dir ):
    # dirpath is a string.
    # dirnames and filenames are lists of strings.

    # Convert dirpath to Path object.
    pathlib_dirpath = Path( dirpath )
    all_files.extend( filenames )
    # Convert dirnames and filenames to Path containers.
    pathlib_dirnames: List[Path]
    pathlib_dirnames = [pathlib_dirpath / dirname for dirname in dirnames]
    pathlib_filenames: List[Path]
    pathlib_filenames = [pathlib_dirpath / filename for filename in filenames]

    # Process the Path objects.
    print( f"Directory: {dirpath}" )
    if len( pathlib_dirnames ) > 0:
      print( f"  {len( pathlib_dirnames )} Subdirectories: {pathlib_dirnames}" )
      for i, dirname in enumerate( pathlib_dirnames, start = 1 ):
        # dirname is a pathlib.Path object.
        print( f"    Directory {i} name: {dirname}" )
    print( f"  {len( pathlib_filenames )} files: {pathlib_filenames}" )
    for i, filename in enumerate( pathlib_filenames, start = 1 ):
      # filename is a string.
      print( f"    File {i} name: {filename}" )
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
