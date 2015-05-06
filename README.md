es-query-simple
===============

A tiny command line utility to query elasticsearch.

Installation
-------

```
git clone (this repo)
pip install elasticsearch
./queryes.py
```

Usage
-------

```
usage: ./queryes.py -h [es_host:port] <query>

options:
    -c [count]    number of results to return
    -i [index]  query a specific index
    -j,--json   output json instead of lines
    --help      print this.
    -l           list all indexes on host
```
