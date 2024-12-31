class User:
    
      def __init__(self,first,last):
          self.first_name = first
          self.last_name = last
          self.session_cards = {}
          self.topic_id = 0
          self.prompt = 0
      
      def add_topic_id(self, topic):
         self.topic_id = topic

      def add_prompt(self, prompt):
          self.propmt = prompt
      
