from utils.helpers import create_user_from_github, action_update_contact, action_get_username_github, \
    action_get_domain_freshdesk
from utils.questions import init_questions


def main():
    print("\n Updated and get Contacts App \n")
    while True:
        initial_question = init_questions()

        if initial_question == "Transfer from github":
            create_user_from_github()

        if initial_question == "Update contact":
            action_update_contact()

        if initial_question == "Get username Github":
            action_get_username_github()

        if initial_question == "Get Freshdesk domain":
            action_get_domain_freshdesk()
        if initial_question == "exit":
            break


if __name__ == "__main__":
    main()
