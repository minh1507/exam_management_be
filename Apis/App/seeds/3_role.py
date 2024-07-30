from App.models.role import Role

def run():
    records = [
        {'id': 1, 'name': 'Admin', "code": "ADMIN"},
        {'id': 2, 'name': 'Exam entrants', "code": "EXAM_ENTRANTS"},
        {'id': 3, 'name': 'Exam corrector', "code": "EXAM_CORECTOR"},
        {'id': 4, 'name': 'Exam presenter', "code": "EXAM_PRESENTER"},
        {'id': 5, 'name': 'Exam time setter', "code": "EXAM_TIME_SETTER"},
        {'id': 6, 'name': 'Contestants', "code": "CONTESTANTS"},
    ]
    
    for record in records:
        record_id = record['id']
        new_name = record['name']
        new_code = record['code']
        
        role_record, created = Role.objects.update_or_create(
            id=record_id,
            defaults={'name': new_name, 'code': new_code}
        )
        
        if created:
            print(f"Created new record with ID: {record_id}")
        else:
            print(f"Updated existing record with ID: {record_id}")

if __name__ == "__main__":
    run()
