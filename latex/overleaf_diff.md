## Info

This script will grab two zips from Overleaf and diff the main.tex files in them

## Usage: 
- Go to the "History" tab in Overleaf
- Select each version then click "Download project at this version"
- Go to the directory that both files dowloaded to and run this script there
```bash
./overleaf_diff.sh
```
- The version numbers are automatically compared and zip files get deleted
