import unittest

def dict2pk2(d, k1, k2): return d and k1 in d and k2 in d and {
  k1: d[k1],
  k2: d[k2],
}

class Test1(unittest.TestCase):
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
