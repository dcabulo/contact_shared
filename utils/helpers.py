import json

import requests
from utils.constants import GITHUB_URL, GITHUB_TOKEN, FRESHDESK_URL, FRESHDESK_ACCOUNT, FRESHDESK_TOKEN, \
    FRESHDESK_URL_ADD_CONTACT
from models.user import User
from utils.questions import which_contact_update, update_information


def get_github_user_info():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.get(GITHUB_URL, headers=headers)
    response.raise_for_status()
    return response.json()


def get_freshdesk_user_info(**kwargs):
    type_account = kwargs.get("type_account")
    if type_account is None:
        raise
    if type_account == "account":
        response = requests.get(FRESHDESK_URL + FRESHDESK_ACCOUNT, auth=(FRESHDESK_TOKEN, "x"))
        response.raise_for_status()
        return response.json()
    if type_account == "contact":
        response = requests.get(FRESHDESK_URL + FRESHDESK_URL_ADD_CONTACT, auth=(FRESHDESK_TOKEN, "x"))
        response.raise_for_status()
        return response.json()


def create_user(data: dict, user_type: str):
    if user_type == "github":
        return User(name=data.get("name"), email=data.get("email"), description=data.get("bio"), type_user="github")
    if user_type == "freshdesk":
        return User(name=data.get("name"), email=data.get("email"), description=data.get("description"),
                    type_user="freshdesk", id_freshdesk=data.get("id"))


def create_contact(user: User):
    headers = {"Content-Type": "application/json"}
    password = "x"
    response = requests.post(FRESHDESK_URL + FRESHDESK_URL_ADD_CONTACT, auth=(FRESHDESK_TOKEN, password),
                             data=json.dumps(user.to_dict()), headers=headers)
    response.raise_for_status()
    return response.json()


def get_contact(id_user: int):
    headers = {"Content-Type": "application/json"}
    response = requests.get(FRESHDESK_URL + FRESHDESK_URL_ADD_CONTACT + f"{id_user}", auth=(FRESHDESK_TOKEN, "x"),
                            headers=headers)
    response.raise_for_status()
    return response.json()


def update_contact(id_user: int, user: User):
    headers = {"Content-Type": "application/json"}
    response = requests.put(FRESHDESK_URL + FRESHDESK_URL_ADD_CONTACT + f"/{id_user}", auth=(FRESHDESK_TOKEN, "x"),
                            data=json.dumps(user.to_dict()), headers=headers)
    response.raise_for_status()
    return response.json()


def create_user_from_github():
    github_user_info = get_github_user_info()
    user_to_add_fresh = create_user(github_user_info, "github")
    fresh_desk_user = create_contact(user_to_add_fresh)
    print(f"Contact added successfully-> id:{fresh_desk_user.json()['id']}")


def action_update_contact():
    users = [create_user(item, user_type="freshdesk") for item in get_freshdesk_user_info(type_account="contact")]
    user_to_update = which_contact_update(users)
    user_updated = update_information(user_to_update)
    update_contact(user_updated.id, user_to_update)
    print("Contact updated successfully")


def action_get_username_github():
    github_user_info = get_github_user_info()
    print(f"Your username is-> {github_user_info.get('login')}")


def action_get_domain_freshdesk():
    freshdesk_info = get_freshdesk_user_info(type_account="account")
    print(f"Your freshdesk domain is -> {freshdesk_info.get('account_domain')}")
