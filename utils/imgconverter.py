import argparse
import os
from PIL import Image
from pillow_heif import register_heif_opener

#Currently, only heic to png and jpg is supported
def getOpts():
  parser = argparse.ArgumentParser(description="A Command-Line utility that converts images between different formats")
  parser.add_argument("--from", type=str, choices=["png","heic","jpg","tiff","bmp","webp"],help="Choose a file format to convert from")
  parser.add_argument("--to", type=str, choices=["png","heic","jpg","tiff","bmp","webp"],help="Choose a file format to convert to")
  parser.add_argument("-d","--dir",type=str,help="directory to folder containing the images to be converted")
  parser.add_argument("-f","--files",type=str,nargs="+",help="image files to be converted. Enter '*' to convert all files in the directory")
  parser.add_argument("-o","--outdir"type-str,help="Directory to place converted files in")
  parser.add_argument("-v","--verbose",action="store_true",help="Enable verbose mode")
  args = parser.parse_args()
  args_dict = vars(args)
  return args_dict

def convertImage(
  fromFormat : str,
  toFormat : str,
  directory : str,
  outdir : str,
  files : List[str],
  verbose : boolean
):
  images = []
  if fromFormat == "heic":
    register_heif_opener()
  if len(files) == 1 and files[0] == "*":
    for filename in os.listdir(directory):
      if verbose:
        print("Converting: " + filename)
      im = Image.open(os.path.join(directory,filename)
      new_filename = os.path.splitext(filename)[0] + "." + toFormat
      new_filepath = os.path.join(outdir,new_filename)
      Image.save(new_filepath, format(toFormat))

if __name__ == "__main__":
  opts = getOpts()
  convertImage(fromFormat
    
    
    
