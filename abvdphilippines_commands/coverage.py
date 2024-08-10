"""
Write nexus file.
"""
from pathlib import Path
from collections import defaultdict, Counter
from nexusmaker import load_cldf

root = Path(__file__).parent.parent


def run(args):
    mdfile = root / 'cldf' / "cldf-metadata.json"
    records = list(load_cldf(mdfile, table='FormTable'))
    
    parameters = set()
    lexemes = Counter()
    pbl = defaultdict(set)
    cognates = defaultdict(set)
    for r in records:
        parameters.add(r.Parameter_ID)
        pbl[r.get_taxon()].add(r.Parameter_ID)
        lexemes[r.get_taxon()] += 1
        if r.Cognacy:
            cognates[r.get_taxon()].add(r.Parameter_ID)

    np = len(parameters)
    print("\t".join(["Taxon", "Lexemes", "Parameters", "Missing", "Cognates", "PropLexemesWithCognates", "PropParametersWithCognates"]))
    for taxon in sorted(lexemes):
        nc = len(cognates[taxon])
        print("\t".join([
            taxon,
            "%d" % lexemes[taxon],
            "%d" % len(pbl[taxon]),
            "%d" % (np - len(pbl[taxon])),
            "%d" % nc,
            "%0.3f" % (nc / lexemes[taxon]),
            "%0.3f" % (nc / np)
        ]))