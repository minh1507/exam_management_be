from App.models.password import Password

def run():
    passwords = [
        {'id': 1, 'hash': "pbkdf2_sha256$720000$29WULEfRzk2SadGQ1VzINq$m28307BdwAlNOl8MnLs2Wx4kv46GQMDGmcjuz0K87rY="},
    ]
    
    for record in passwords:
        record_id = record['id']
        new_hash = record['hash']
        
        password_record, created = Password.objects.update_or_create(
            id=record_id,
            defaults={'hash': new_hash})
        
        if created:
            print(f"Created new password record with ID: {record_id}")
        else:
            print(f"Updated existing password record with ID: {record_id}")

if __name__ == "__main__":
    run()
