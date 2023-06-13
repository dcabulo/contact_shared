from PyInquirer import prompt
from typing import List

from models.user import User


def init_questions():
    actions = {
        'type': 'list',
        'name': 'action',
        'message': 'Which action you wanna do today?',
        'choices': ['Transfer from github', 'Update contact', 'Get username Github', 'Get Freshdesk domain', "exit"]
    }
    answers = prompt(actions)
    return answers["action"]


def which_contact_update(users: List[User]):
    questions = {
        'type': 'list',
        'name': 'get_contact',
        'message': 'Which contact you wanna update?',
        'choices': map(lambda v: f"{v.id}-{v.name}", users)
    }
    answers = prompt(questions)
    user_to_update = list(filter(lambda x: str(x.id) == answers.get("get_contact").split("-")[0], users))
    return user_to_update[0]


def update_information(user: User):
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Update the contact name',
            'default': user.name,
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Update the description',
            'default': user.description,
        }
    ]
    answers = prompt(questions)
    user.name = answers.get("name")
    user.description = answers.get("description")
    return user
