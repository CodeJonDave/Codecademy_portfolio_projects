import random
import json


class TarotCard:
    cards_total = 22
    suits = ["cups", "swords", "pentacles", "wands"]

    def __init__(self):
        self.id = None
        self.card_name = ""
        self.description = ""
        self.keywords = []
        self.upright_meaning = ""
        self.reversed_meaning = ""
        self.related_areas = []
        self.roman_numeral = ""
        self.time_meaning = {}

    def set_card_details(self, id, name, description, keywords, upright, reversed, related, roman, time_meaning):
        self.id = id
        self.card_name = name
        self.description = description
        self.keywords = keywords
        self.upright_meaning = upright
        self.reversed_meaning = reversed
        self.related_areas = related
        self.roman_numeral = roman
        self.time_meaning = time_meaning

    def display_card(self):
        # Method to display card details
        print(self.card_name)
        print(self.description)
        print(', '.join(self.keywords))
        print(', '.join(self.related_areas))
        print(self.roman_numeral)

    @staticmethod
    def draw_major_arcana():
        major_draw = TarotCard()
        with open('major_arcana.json', 'r', encoding='utf-8') as major_file:
            cards = json.load(major_file)
        card = cards.get(str(random.randint(1, TarotCard.cards_total)))
        if card:
            major_draw.set_card_details(card.get("id"), card.get("card_name"),
                                        card.get("description"), card.get(
                                            "keywords"),
                                        card.get("upright_meaning"), card.get(
                                            "reversed_meaning"),
                                        card.get("related_areas"), card.get(
                                            "roman_numeral"),
                                        card.get("time_meanings"))
        return major_draw

    @staticmethod
    def draw_minor_arcana():
        minor_draw = TarotCard()
        
        return minor_draw