#!/usr/bin/env python

from elasticsearch import Elasticsearch
import getopt
import sys


def query_es(host, query, index, count, json_output):

    es = Elasticsearch([host])
    data = es.search(q=query, size=count, index=index)
    if json_output:
        import json
        print json.dumps(data)
    else:
        for item in data["hits"]["hits"]:
            string = [str(v) for v in item["_source"].values()]
            output = " ".join(string)
            print "{} {} {}".format(item["_source"]["@timestamp"], item["_type"], output)

def get_index_list(host):
    es = Elasticsearch([host])
    print "\n".join(es.indices.get_aliases().keys())

def usage():
    print """Es-query-simple by Ryan Huber
usage: {name} -h [es_host:port] <query>

options:
    -c [count]    number of results to return
    -i [index]  query a specific index
    -j,--json   output json instead of lines
    --help      print this.
    -l           list all indexes on host

 """.format(name=sys.argv[0])

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:ji:h:l", ["count=", "json", "index=", "host=", "list", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    host = "localhost:9200"
    query = args
    index="_all"
    count=10
    json_output = False

    for o, a in opts:
        if o in ("--help"):
            usage()
            sys.exit(1)
        if o in ("-h", "--host"):
            host = a
        if o in ("-c", "--count"):
            count = a
        if o in ("-j", "--json"):
            json_output = True
        if o in ("-i", "--index"):
            index = a
        if o in ("-l", "--index"):
            get_index_list(host)
            sys.exit(0)

    query_es(host, query, index, count, json_output)

