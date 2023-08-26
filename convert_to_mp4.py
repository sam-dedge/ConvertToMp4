import subprocess
import os
from pathlib import Path
import argparse

def convert_to_mp4(src=None, filepath=None, ogdel=False):
    
    if src != None:
        #print(src, ogdel)
        dst = src + '/result/'
        Path(dst).mkdir(parents=True, exist_ok=True)

        for root, _, filenames in os.walk(src):
            
            if root != src:
                print('Only Given directory is checked. Breaking.')
                break
            
            for filename in filenames:
                #print('[INFO] 1',filename)
                try:
                    _format = ''
                    if ".flv" in filename.lower():
                        _format=".flv"
                    if ".avi" in filename.lower():
                        _format=".avi"
                    if ".mov" in filename.lower():
                        _format=".mov"

                    if _format not in ['.flv', '.avi', '.mov']:
                        print('File Format not supported.')
                        break

                    inputfile = root + '/' + filename
                    filename = filename.lower().replace(_format, ".mp4")
                    filename = filename.replace('.en', '')
                    outputfile = dst + filename.lower()
                    print('[INFO] 2', inputfile, outputfile)
                    subprocess.call(['ffmpeg', '-i', inputfile, outputfile])
                    print(f'Conversion complete. Check File at {outputfile}. Del Flag = {ogdel}')
                    
                    if ogdel:
                        print("File Delete Flag set. Deleting File.")
                        os.remove(inputfile)
                        print('File Delete Complete.')

                except:
                    print("Directory exception occurred. Program Terminated.")
    elif filepath != None:
        try:
            if os.path.exists(filepath):
                dst = filepath[:-len(os.path.basename(filepath))]
                #print(dst)
                #Path(dst).mkdir(parents=True, exist_ok=True)
                filename = os.path.basename(filepath)
                
                _format = ''
                if ".flv" in filename.lower():
                    _format=".flv"
                if ".avi" in filename.lower():
                    _format=".avi"
                if ".mov" in filename.lower():
                    _format=".mov"

                if _format not in ['.flv', '.avi', '.mov']:
                    print('File Format not supported.')
                    return
                
                filename = filename.lower().replace(_format, ".mp4")
                filename = filename.replace('.en', '')
                outputfile = dst + 'Res_' + filename.lower()
                print('[INFO] 2', filepath, outputfile)
                subprocess.call(['ffmpeg', '-i', filepath, outputfile])
                print(f'Conversion complete. Check File at {outputfile}. Del Flag = {ogdel}')
                
                if ogdel:
                    print("File Delete Flag set. Deleting File.")
                    os.remove(filepath)
                    print('File Delete Complete.')
        except:
            print('FilePath Exception Occured. Program Terminated')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir')
    parser.add_argument('--file')
    parser.add_argument('--ogdel')
    args = parser.parse_args()

    if args.dir == None and args.file == None:
        print("Provide a directory or a file to convert.")
        print("Use:")
        print("\t --dir flag for Directory.")
        print("\t --file flag for File.")
    elif args.dir != None and args.file != None:
        print("Both flags provided. Please provide either --dir or --file flag.")
    elif args.dir != None:
        convert_to_mp4(src=args.dir, ogdel=args.ogdel)
    elif args.file != None:
        convert_to_mp4(filepath=args.file, ogdel=args.ogdel)