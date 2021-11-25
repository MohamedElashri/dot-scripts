## Goal

Given a bib file the script do the following:
1. Reduce author lists to 10 authors
2. Abbreviate journal names
3. Remove unneeded IDs and replace with doi links
4. Remove unneeded tags (file, abstract)


## Dependencies 

This script requires `bibtexparser`

```
pip install bibtexparser
```

## Usage

```
./process-bibliography.py <filename>.bib
```
