es-query-simple
===============

A tiny command line utility to query elasticsearch. "Because `curl` isn't a cli."

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
    -h [host:port]  host and port. defaults to localhost:9200
    -c [count]      number of results to return
    -i [index]      query a specific index
    -j,--json       output json instead of lines
    --help          print this.
    -l              list all indexes on host
```

Examples
--------

Get 100 apache events from the logstash-2020.04.11 index

`./queryes.py -h "mybigserver:9200" -i "logstash-2020.4.11" -c 100 "type:apache AND clientip:4.2.2.1"`

Same, but print json instead

`./queryes.py -h "mybigserver:9200" -i "logstash-2020.4.11" -c 100 --json "type:apache AND clientip:4.2.2.1"`

Return a list of all indexes in a cluster

`./queryes.py -h "mybigserver:9200" -l`

