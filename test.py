import unittest
import json

from index import o2jsonl, dict2pk2

class Test1(unittest.TestCase):
  def test_o2jsonl(self):
    o = {
      "k1s": "hw",
      "k2i": 299792458,
      "k3f": 3.776,
    }
    jline = o2jsonl(o)
    jlf = jline[-1]
    self.assertEqual(jlf, "\n")
    o2 = json.loads(jline.strip())
    o3 = o2 and "k1s" in o2 and "k2i" in o2 and "k3f" in o2 and o2
    self.assertEqual(o3 and o3["k1s"], o["k1s"])
    self.assertEqual(o3 and o3["k2i"], o["k2i"])
    self.assertEqual(o3 and o3["k3f"], o["k3f"])

  def test_dict2pk2(self):
    sd = {
      "a": "nts",
      "b": 299792458,
      "c": 3776,
    }
    pk2 = dict2pk2(sd, "a", "b")
    k1v = pk2 and "a" in pk2 and pk2["a"]
    k2v = pk2 and "b" in pk2 and pk2["b"]
    self.assertEqual(k1v, "nts")
    self.assertEqual(k2v, 299792458)

unittest.main()
