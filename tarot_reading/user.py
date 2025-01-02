class User:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.session_cards = []
        self.topic_id = None
        self.question = None

    def add_topic_id(self, topic):
        self.topic_id = topic

    def add_prompt(self, question):
        self.question = question

    def not_card_in_session_cards(self, card):
        for set in self.session_cards:
            for cards in set.values():
                for session_card in cards:
                    if session_card.id == card.id:
                        return False
        return True
