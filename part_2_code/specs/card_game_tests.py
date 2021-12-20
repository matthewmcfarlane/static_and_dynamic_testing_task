import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 7)
        self.card2 = Card("Spades", 1)
        self.cards = [self.card1, self.card2]
        self.cardgame = CardGame()

    def test_check_for_ace(self):
        result = self.cardgame.check_for_ace(self.card2)
        expected = True
        self.assertEqual(expected, result)

    def test_highest_card(self):
        result = self.cardgame.highest_card(self.card1, self.card2)
        expected = self.card1
        self.assertEqual(expected, result)
    
    def test_cards_total(self):
        result = self.cardgame.cards_total(self.cards)
        expected_total = self.card1.value + self.card2.value
        expected_result = "You have a total of " + str(expected_total)
        self.assertEqual(expected_result, result)
        



        