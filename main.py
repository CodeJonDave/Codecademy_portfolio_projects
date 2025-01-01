from title import title as TITLE
from topic import Topic
from user import User


def main():
    print(TITLE)
    while (True):
        username = input(
            "Welcome! please What is your fist and last name.").strip()
        if " " in username and len(username.split()) == 2:
            break
        print("Improper format: first and last name please: ")
    first_name, last_name = username.split(" ", 1)
    user = User(first_name, last_name)

    print(
        f"We are ready for you {user.first_name.title()}.\nPlease take a moment and think about what you would like ask the fates today.\n")

    while (True):
        print(Topic.get_all_topics())
        topic = input("Please enter the number for you selection: ").strip()
        if topic.isdigit() and int(topic) in range(1, 6):
            user.add_topic_id(topic)
            break
        print("Improper selection please enter a number 1-5")
    print(f"{Topic.get_topic_name(user.topic_id)} can grant you insights such as {Topic.get_topic_description(user.topic_id)}")
    print("Please think about which question you want insight into.\n")

    while (True):
        print(Topic.get_prompts(user.topic_id))
        prompt = input("Please enter the number for you selection: ")
        if prompt.isdigit() and 1 <= int(prompt) <= 3:
            user.add_prompt(prompt)
            break
        print("Improper slecetion please enter a number 1-3")


if __name__ == "__main__":
    main()
