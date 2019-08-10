import os
import sys
import json
from itertools import imap

from index import o2jsonl, dict2pk2

def main():
  d = {
    "k1": 3776,
    "k2": 2.99792458,
    "v1": 634,
  }
  jsonl = imap(o2jsonl, [
    d,
    dict2pk2(d, "k1", "k2"),
  ])
  sys.stdout.writelines(jsonl)
  pass

main()
