from mpinfo import utils
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.mp = utils.get_mp_from_postcode("NG26BE")

    def test_basicdetails(self):
        self.assertEqual(self.mp.name, "Rt Hon Kenneth Clarke QC")
        self.assertEqual(self.mp.party, "Conservative")

    def test_parliamentarydetails(self):
        self.assertEqual(self.mp.parliamentary_email, "clarkek@parliament.uk")
        self.assertEqual(self.mp.parliamentary_addr, "House of Commons, London, SW1A 0AA")
        self.assertEqual(self.mp.parliamentary_tel, "020 7219 4528")
        self.assertEqual(self.mp.parliamentary_fax, "020 7219 4841")

    def test_constituencydetails(self):
        self.assertEqual(self.mp.constituency_email, None)
        self.assertEqual(self.mp.constituency_addr, 'Rushcliffe House, 17/19 Rectory Road, West Bridgford, Nottingham, NG2 6BE')
        self.assertEqual(self.mp.constituency_tel, "0115-981 7224")
        self.assertEqual(self.mp.constituency_fax, "0115-981 7273")

if __name__ == '__main__':
    unittest.main()
