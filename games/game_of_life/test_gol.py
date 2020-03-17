import unittest
import game

class Game_test(unittest.TestCase):
  def setUp(self):
  	self.bord = game.Bord(5,5)

  def test_setLfe(self):
  	self.bord.setlife((1,1), True)

  def test_getlife(self):
  	self.assertFalse(self.bord.getlife((2,2)))

  def test_countN(self):
  	self.assertEqual(self.bord.countN((0,0)), 0)


if __name__ == '__main__':
  unittest.main()
