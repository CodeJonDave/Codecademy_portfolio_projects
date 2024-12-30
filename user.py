class User:
    def __init__(self,first,last):
          self.first_name = first
          self.last_name = last
          self.user_cards = {}
    def add_topic_id(self, id):
         self.topic_id = int(id)