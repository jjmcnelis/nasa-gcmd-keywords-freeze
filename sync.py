#!/usr/bin/env python3
from datetime import datetime as dt
from os.path import realpath, dirname
from urllib.request import urlretrieve
gcmd = "https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme"
sdir = dirname(realpath(__file__))
for kwd in [
    'MimeType',
    'chronounits',
    'horizontalresolutionrange',
    'instruments',
    'locations',
    'platforms',
    'projects',
    'providers',
    'rucontenttype',
    'sciencekeywords',
    'temporalresolutionrange',
    'verticalresolutionrange',
]:
    for fmt in ['json', 'xml', 'csv', 'rdf']:
        urlretrieve(f"{gcmd}/{kwd}?format={fmt}", f"{sdir}/{kwd}.{fmt}")
with open(f"{sdir}/README.md", "r") as f:
    lns = [l.strip() for l in f.readlines()]
lns[3] = f">*Last updated: **{dt.now().strftime('%Y-%m-%d %H:%M:%S')}***"
with open(f"{sdir}/README.md", "w") as f:
    f.write("\n".join(lns))