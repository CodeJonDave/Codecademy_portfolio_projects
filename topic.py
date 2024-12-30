import json

class Topic:
    def __init__(self,id,topic,description):
        self.id = id
        self.topic = topic
        self.description = description

    def get_all_topics():
        topics_list = ""
        
        with open("topics.json","r", encoding="utf-8") as topics_file:
            topics = json.load(topics_file)
        for topic_id, topic_data in topics.items():
            topics_list += topic_id+". "
            topics_list += topic_data.get("topic") + "\n"
            pass
        return topics_list

    def get_prompt():
        pass