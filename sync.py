#!/usr/bin/env python3
from datetime import datetime as dt
from os.path import realpath, dirname
from urllib.request import urlretrieve
gcmd = "https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme"
sdir = dirname(realpath(__file__))
time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
dt.now().strftime('%Y-%m-%d %H:%M:%S')
fmts = {o: [f"### {o}\n"] for o in ['json', 'xml', 'csv', 'rdf',]}
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
    for fmt in list(fmts.keys()):
        urlretrieve(f"{gcmd}/{kwd}?format={fmt}", f"{fmt}/{kwd}.{fmt}")
        fmts[fmt].append(f"- *[`{fmt}/{kwd}.{fmt}`]({fmt}/{kwd}.{fmt})*")
files = "\n".join(["\n".join(fmts[o])+"\n" for o in list(fmts.keys())])
with open(f"README.md", "w") as f:
    f.write(f"""# GCMD Keyword Freeze

*This readme regenerates with each `sync.py` run. Last updated on **{time}.***

## Keyword links

* Earthdata wiki reference: https://wiki.earthdata.nasa.gov/display/CMR/GCMD+Keyword+Access
* Keyword list dumps in `rdf`, `xml`, `json`, `csv` formats: https://gcmd.earthdata.nasa.gov/static/kms/
* Script syncs dumps to respective folders, updates this readme: [`sync.py`](sync.py)

```shell
./sync.py
```

You could also use the web service if you needed to hit keywords lists routinely for any reason. It's the second of the two links on the Earthdata wiki page linked above.

## Keyword dumps

{files}

""")