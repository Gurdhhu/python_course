#!/usr/bin/python3.4
import argparse
import subprocess
from Bio import Entrez


Entrez.email = "ledum_laconicum@mail.ru"

parser = argparse.ArgumentParser(description="Finds GSE datasets "
                                             "in NCBI")
parser.add_argument("query",
                    type=str,
                    help="enter your query")
parser.add_argument("taxon",
                    type=str,
                    nargs="?",
                    help="enter the organism (if you want)")

args = parser.parse_args()
query = args.query
taxon = args.taxon

if taxon is None:
    formatted = query + " AND GSE[Entry Type]"
else:
    formatted = " ".join([query, "AND GSE[Entry Type] AND",
                          taxon, "[Organism]"])
handle = Entrez.esearch(db="gds", term=formatted)
record = Entrez.read(handle)
idlist = ", ".join(record["IdList"])
handle = Entrez.esummary(db="gds", id=idlist, retmode="xml")
record = Entrez.read(handle)
for i in record:
    print("\t".join([i["Accession"], i["taxon"], i["title"]]))
