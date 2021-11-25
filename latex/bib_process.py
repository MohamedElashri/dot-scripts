#!/usr/bin/env python

import bibtexparser
import sys
import os

filepath = sys.argv[1]


# Reduce Author list that is greater than 10 to 3 authors only
def truncate_to_three_authors(authors_string):
    authors = authors_string.split('and')
    if len(authors) > 10:  # et.al.
        authors_truncated = 'and'.join(authors[:3]) + "and others"
        return authors_truncated
    else:
        return authors_string
# Define journal abbreviations
journal_abbreviations = {
    "Physical Review A": "Phys. Rev. A",
    "Physical Review A - Atomic, Molecular, and Optical Physics": "Phys. Rev. A",
    "Physical Review D": "Phys. Rev. D",
    "Physical Review D - Particles, Fields, Gravitation and Cosmology": "Phys. Rev. D",
    "J. Phys. B: At. Mol. Opt. Phys. ",
    "Physical Review Letters": "Phys. Rev. Lett. ",
    "Classical and Quantum Gravity": "Class. Quantum Grav. ",
    "Journal of Physics B: Atomic, Molecular and Optical Physics":
    "Reviews of Modern Physics": "Rev. Mod. Phys. ",
    "Nature Physics": "Nat. Phys. ",
    "Nuclear Instruments and Methods in Physics Research, Section A: Accelerators, Spectrometers, Detectors and Associated Equipment":
    "Reports on Progress in Physics": "Rep. Prog. Phys. ",
    "Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences": "Philos. T. R. Soc. A",
    "Advanced in Physics: X": "Adv. Phys. X",
}

# Select case for Abbreviate journal names
def abbreviate_journal_name(journal_name):
    journal_name = journal_name.strip()
    if journal_name in journal_abbreviations:
        return journal_abbreviations[journal_name]
    else:
        return journal_name

# Remove archiveprefix, arxivid, eprint keys and use first of the URLs listed
def remove_ids_and_fix_links(entry):
    if 'archiveprefix' in entry:
        del entry['archiveprefix']
    if 'arxivid' in entry:
        del entry['arxivid']
    if 'eprint' in entry:
        del entry['eprint']

    # only use first of the URLs listed
    if 'url' in entry:
        split_urls = entry['url'].split(' ')
        if len(split_urls) > 1:
            entry['url'] = split_urls[0]
    # If there is no URL, construct a DOI URL link
    if 'doi' in entry:
        if 'url' not in entry:
            doi = entry['doi']
            entry['url'] = f"https://doi.org/{doi}"
        del entry['doi']
# load the bibtex file
with open(filepath) as f:
    bib_database = bibtexparser.load(f)
      
    # each entry is a bibtex entry
    for entry in bib_database.entries:
        entry['author'] = truncate_to_three_authors(entry['author'])

        if 'journal' in entry:
            entry['journal'] = abbreviate_journal_name(entry['journal'])

        remove_ids_and_fix_links(entry)

        if 'abstract' in entry:
            del entry['abstract']
        if 'file' in entry:
            del entry['file']

    # save the bibtex file
    filepath, ext = os.path.splitext(filepath)
    filepath = f"{filepath}-processed{ext}"

    with open(filepath, 'w') as output_file:
        bibtexparser.dump(bib_database, output_file)
        print(f"Wrote to {filepath}")
