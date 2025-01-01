import json


class Topic:

    @staticmethod
    def get_all_topics():
        topics_list = ""
        with open("topics.json", "r", encoding="utf-8") as topics_file:
            topics = json.load(topics_file)
            for topic in topics.keys():
                topic_data = topics.get(topic)
                topic_name = topic_data.get("topic")
                topics_list += f"{topic}. {topic_name}\n"
        return topics_list

    @staticmethod
    def get_prompts(topic_id):
        count = 1
        prompts = ""
        with open('topics.json', 'r', encoding='utf-8') as topics_file:
            topics = json.load(topics_file)
        questions = topics.get(topic_id).get("common_questions")
        for question in questions:
            prompts += f"{count}. {question}\n"
            count += 1
        return prompts

    @staticmethod
    def get_topic_name(topic_id):
        with open("topics.json", "r", encoding="utf-8") as topics_file:
            topics = json.load(topics_file)
        topic = topics.get(topic_id).get("topic")
        return topic

    @staticmethod
    def get_topic_description(topic_id):
        with open("topics.json", 'r', encoding='utf-8') as topics_file:
            topics = json.load(topics_file)
        topic_desc = topics.get(topic_id).get("description")
        return topic_desc
