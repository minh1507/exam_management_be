class MessageUtil:
    def __init__(self):
        self.messages = []
    def push(self, content, key):
        self.messages.append(content + '.' + key)
    def get(self):
        return list(set(self.messages))