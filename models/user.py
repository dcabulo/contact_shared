class User:
    def __init__(self, name: str, email: str, description: str, type_user: str, id_freshdesk=None):
        self.name = name
        self.email = email
        self.description = description
        self.type_user = type_user
        self.id = "" if id_freshdesk is None else id_freshdesk

    def to_dict(self):
        return {"name": self.name, "email": self.email, "description": self.description}

    def __str__(self):
        user = ''
        user += f'Type User: {self.type_user}\n'
        user += f'Name: {self.name}\n'
        user += f'Email: {self.email}\n'
        user += f'Description: {self.description}\n'
        user += f'Id: {self.id}\n'
        return user
