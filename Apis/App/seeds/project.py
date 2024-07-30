from App.models.project import Project

def run():
    projects = [
        {'id': 1, 'name': 'python', "code": "PY"}
    ]
    
    for record in projects:
        record_id = record['id']
        name = record['name']
        code = record['code']  

        project_instance = Project.objects.get(id=record_id)

        project_record, created = Project.objects.update_or_create(
            id=record_id,
            defaults={'name': name, 'code': code}
        )
        
        if created:
            print(f"Created new project record with ID: {record_id}")
        else:
            print(f"Updated existing project record with ID: {record_id}")

if __name__ == "__main__":
    run()
