class MessageUtil:
    def __init__(self):
        self.messages = []
    def push(self, content, key):
        print(content, key)
        self.messages.append(content + '.' + key)
    def get(self):
        return self.messages