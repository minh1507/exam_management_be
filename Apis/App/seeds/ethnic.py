from App.models.ethnic import Ethnic

def run():
    records = [
    {'id': 1, 'name': 'Kinh', 'code': 'KINH'},
    {'id': 2, 'name': 'Tày', 'code': 'TAY'},
    {'id': 3, 'name': 'Thái', 'code': 'THAI'},
    {'id': 4, 'name': 'Mường', 'code': 'MUONG'},
    {'id': 5, 'name': 'H’mong', 'code': 'HMONG'},
    {'id': 6, 'name': 'Dao', 'code': 'DAO'},
    {'id': 7, 'name': 'Kơ Ho', 'code': 'KO_HO'},
    {'id': 8, 'name': 'Nùng', 'code': 'NUNG'},
    {'id': 9, 'name': 'Ê Đê', 'code': 'E_DE'},
    {'id': 10, 'name': 'Ba Na', 'code': 'BA_NA'},
    {'id': 11, 'name': 'Xơ Đăng', 'code': 'XO_DANG'},
    {'id': 12, 'name': 'H’Rê', 'code': 'H_RE'},
    {'id': 13, 'name': 'Chăm', 'code': 'CHAM'},
    {'id': 14, 'name': 'Jarai', 'code': 'JARAI'},
    {'id': 15, 'name': 'S’tieng', 'code': 'STIENG'},
    {'id': 16, 'name': 'Tà Ôi', 'code': 'TA_OI'},
    {'id': 17, 'name': 'Co', 'code': 'CO'},
    {'id': 18, 'name': 'Giáy', 'code': 'GIAY'},
    {'id': 19, 'name': 'Cơ Tu', 'code': 'CO_TU'},
    {'id': 20, 'name': 'Raglai', 'code': 'RAGLAI'},
    {'id': 21, 'name': 'M’nông', 'code': 'M_NONG'},
    {'id': 22, 'name': 'Xinh Mun', 'code': 'XINH_MUN'},
    {'id': 23, 'name': 'Hà Nhì', 'code': 'HA_NHI'},
    {'id': 24, 'name': 'Khmer', 'code': 'KHMER'},
    {'id': 25, 'name': 'Hà La', 'code': 'HA_LA'},
    {'id': 26, 'name': 'Bố Y', 'code': 'BO_Y'},
    {'id': 27, 'name': 'Lào', 'code': 'LAO'},
    {'id': 28, 'name': 'Chứt', 'code': 'CHUT'},
    {'id': 29, 'name': 'Lự', 'code': 'LU'},
    {'id': 30, 'name': 'Mảng', 'code': 'MANG'},
    {'id': 31, 'name': 'Sách', 'code': 'SACH'},
    {'id': 32, 'name': 'Thổ', 'code': 'THO'},
    {'id': 33, 'name': 'Hồ', 'code': 'HO'},
    {'id': 34, 'name': 'Bana', 'code': 'BANA'},
    {'id': 35, 'name': 'Ngái', 'code': 'NGAI'},
    {'id': 36, 'name': 'Phu La', 'code': 'PHU_LA'},
    {'id': 37, 'name': 'Si La', 'code': 'SI_LA'},  
    {'id': 38, 'name': 'Lô Lô', 'code': 'LO_LO'},
    {'id': 39, 'name': 'Chơ Ro', 'code': 'CHO_RO'},
    {'id': 40, 'name': 'Kháng', 'code': 'KHANG'},
    {'id': 41, 'name': 'Dê', 'code': 'DE'},
    {'id': 42, 'name': 'Lục', 'code': 'LUC'},
    {'id': 43, 'name': 'Yao', 'code': 'YAO'},
    {'id': 44, 'name': 'Cao Lan', 'code': 'CAO_LAN'},
    {'id': 45, 'name': 'Rơ Măm', 'code': 'RO_MAM'}
    ]
    
    for record in records:
        record_id = record['id']
        new_name = record['name']
        new_code = record['code']

        ethnic_record, created = Ethnic.objects.update_or_create(
            id=record_id,
            defaults={'name': new_name, 'code': new_code}
        )
        
        if created:
            print(f"Created new record with ID: {record_id}")
        else:
            print(f"Updated existing record with ID: {record_id}")

if __name__ == "__main__":
    run()
