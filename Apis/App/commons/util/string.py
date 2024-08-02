import uuid
import re
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

class StringUtil:
    def is_valid_uuid(val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False
    def validate_password(password):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return bool(re.match(pattern, password))
    def hash_password_with_key(password):
        combined_password = f"{password}{settings.PASSWORD_HASH_KEY}"
        hashed_password = make_password(combined_password)
        return hashed_password
    def compare_passwords(stored_hashed_password, input_password):
        combined_input_password = f"{input_password}{settings.PASSWORD_HASH_KEY}"
        return check_password(combined_input_password, stored_hashed_password)
    def extract_uuid(uuid_str):
        match = re.search(r"UUID\('([0-9a-fA-F-]+)'\)", uuid_str)
        if match:
            return match.group(1)
        return None
    def messages(key,content):
        return content + '.' + key
    def get_uuid_filename(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return filename