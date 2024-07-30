from App.models.password import Password

def run():
    records = [
        {'id': 1, 'hash': '123'},
        {'id': 2, 'hash': '456'},
        {'id': 3, 'hash': '789'},
    ]
    
    for record in records:
        record_id = record['id']
        new_hash = record['hash']
        
        password_record, created = Password.objects.update_or_create(
            id=record_id,
            defaults={'hash': new_hash}
        )
        
        if created:
            print(f"Created new record with ID: {record_id}")
        else:
            print(f"Updated existing record with ID: {record_id}")

if __name__ == "__main__":
    run()
