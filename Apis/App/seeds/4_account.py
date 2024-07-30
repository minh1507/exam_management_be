from App.models.user import User
from App.models.password import Password
from App.models.role import Role
from App.models.profile import Profile

def run():
    accounts = [
        {'id': 1, 'username': 'admin', "role": "00000000000000000000000000000001", "password": "00000000000000000000000000000001", "profile": "00000000000000000000000000000001"},
    ]
    
    for record in accounts:
        record_id = record['id']
        new_username = record['username']
        password_id = record['password']  
        role_id = record['role']
        profile_id = record['profile']

        password_instance = Password.objects.get(id=password_id)
        role_instance = Role.objects.get(id=role_id)
        profile_instance = Profile.objects.get(id=profile_id)

        profile_record, created = User.objects.update_or_create(
            id=record_id,
            defaults={'username': new_username, 'password': password_instance, 'role': role_instance, 'profile': profile_instance}
        )
        
        if created:
            print(f"Created new user record with ID: {record_id}")
        else:
            print(f"Updated existing user record with ID: {record_id}")

if __name__ == "__main__":
    run()
