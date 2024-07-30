from App.models.profile import Profile

def run():
    profiles = [
        {'id': 1, 'lastname': "Admin"},
    ]
    
    for record in profiles:
        record_id = record['id']
        new_lastname = record['lastname']
        
        profile_record, created = Profile.objects.update_or_create(
            id=record_id,
            defaults={'lastname': new_lastname})
        
        if created:
            print(f"Created new password record with ID: {record_id}")
        else:
            print(f"Updated existing password record with ID: {record_id}")

if __name__ == "__main__":
    run()
