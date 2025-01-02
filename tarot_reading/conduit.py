from tarot_card import TarotCard
from user import User


class Conduit:
    @staticmethod
    def draw_set(user, time, num_major=1, num_minor=2):

        card_set = {}
        selections = []

        def draw_unique_card(draw_func):
            """Helper to draw a unique card."""
            for _ in range(50):  # Attempt up to 50 times to find a unique card
                card = draw_func()
                if card not in selections and user.not_card_in_session_cards(card):
                    return card
            raise ValueError("Failed to draw a unique card after 50 attempts.")

        # Draw major arcana cards
        for _ in range(num_major):
            selections.append(draw_unique_card(TarotCard.draw_major_arcana))

        # Draw minor arcana cards
        for _ in range(num_minor):
            selections.append(draw_unique_card(TarotCard.draw_minor_arcana))

        card_set[time] = selections
        return card_set
