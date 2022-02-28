#  Rename academic papers to author-year-title.pdf. 

import argparse
import bibtexparser

if __name__ == '__main__' :

    parser = argparse.ArgumentParser(description='Extract bib file to author, year, and title.')
    parser.add_argument('input', help='Input file (.bib)')
    args = parser.parse_args()

    filename = args.input

    with open(filename) as bibtex_file:
        bibtex_str = bibtex_file.read()
  
    bib_database = bibtexparser.loads(bibtex_str)

    authors = bib_database.entries[0]["author"]
    year = bib_database.entries[0]["year"]
    title = bib_database.entries[0]["title"]

    authors_list = authors.split(" and ")
    author = authors_list[0]

    print(author, "-", year, "-", title)
    
