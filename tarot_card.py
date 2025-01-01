class TarotCard:
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
