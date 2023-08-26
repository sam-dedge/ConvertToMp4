# Converting video files to .mp4 locally (Windows)
### File Formats supported
- .flv
- .avi
- .mov

### Create Python Virtual Environemnt
```sh
> python -m venv convertEnv
> convertEnv\Scripts\activate
> pip install -r requirements.txt
```

Do not install requirements.txt as it suprisingly showed lots of packages with " > pip freeze ".
Install the missing packages after 1st run.


## Run Commands for conversion
### Flags
- --dir : Specify a directory
- --file : Specify filepath including filename and extension
- --ogdel : (Optional) True/False. True if you want to delete the original video files

### Run to convert all files from a directory
```sh
> python convert_to_mp4.py --dir "path/to/dir"
```

### Run to convert a file
```sh
> python convert_to_mp4.py --file "path/to/dir/file.ext" --ogdel True
```

---

Please contact to contribute or to request support for more file formats.