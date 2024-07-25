import uuid

class StringUtil:
    def is_valid_uuid(val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False