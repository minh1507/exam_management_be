from .string import *
class MessageUtil:
    def __init__(self):
        self.messages = []
    def push(self, content, key):
        self.messages.append(StringUtil.messages(key, content))
    def get(self):
        return list(set(self.messages))