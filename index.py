import json

def o2jsonl(o): return json.dumps(o)+"\n"

def dict2pk2(d, k1, k2): return d and k1 in d and k2 in d and {
  k1: d[k1],
  k2: d[k2],
}
