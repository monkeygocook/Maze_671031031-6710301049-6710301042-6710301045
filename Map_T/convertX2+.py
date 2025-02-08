def replace_x_with_plus(filename):
    try:
        # อ่านไฟล์
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # แทนที่ 'X' ด้วย '+'
        updated_content = content.replace("X", "+")

        # เขียนกลับไปที่ไฟล์เดิม
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"แทนที่ 'X' เป็น '+' เรียบร้อย! ไฟล์ถูกบันทึกที่ {filename}")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# เรียกใช้ฟังก์ชัน ใส่ชื่อไฟล์ของนายแทน "maze.txt"
replace_x_with_plus("Map/maze8.txt")
