# ==============================================================================
# quiz2_homework_style.py
# โค้ดแนวข้อสอบ QUIZ 2 สไตล์เดียวกับการบ้าน Grader (EX_24, EX_25)
# ลักษณะเฉพาะ: รับค่าบรรทัดเดียว, ไม่มี def ชั้นนอก, แสดงผล 2 บรรทัด (ค่ากลาง + คำตอบ)
# ==============================================================================


# ==============================================================================
# ข้อที่ 1: [HASH] Weighted ASCII Hash (สไตล์การบ้านคำนวณข้อความ)
# ==============================================================================
# [คำอธิบาย]
# บรรทัด 1: แสดงผลคูณ ord(c) * ตำแหน่ง ของแต่ละตัว คั่นด้วยเว้นวรรค
# บรรทัด 2: แสดงตำแหน่ง slot ในตาราง (% table_size)
# 
# Sample Input:  cat 11
# Sample Output: 99 194 348
#                3
# ==============================================================================
def run_q1_hash_homework():
    text, size_str = input().split()
    table_size = int(size_str)

    terms = []
    total_sum = 0

    # วนลูปคำนวณ ord(c) คูณตำแหน่ง (เริ่มที่ 1)
    for i in range(len(text)):
        val = ord(text[i]) * (i + 1)
        terms.append(str(val))
        total_sum += val

    slot = total_sum % table_size

    # แสดงผล 2 บรรทัดสไตล์การบ้าน
    print(" ".join(terms))
    print(slot)


# ==============================================================================
# ข้อที่ 2: [HEAP] delMin & percDown (สไตล์การบ้านตามโน้ต # Quiz Heap)
# ==============================================================================
# [คำอธิบาย]
# บรรทัด 1: แสดงค่าต่ำสุดที่ถูกดึงออกจาก Root
# บรรทัด 2: แสดงสภาพ Min Heap ที่เหลือทั้งหมดหลังจัดเรียงสมบูรณ์
# 
# Sample Input:  5 9 11 14 18 19 21 33 17 27
# Sample Output: 5
#                9 14 11 17 18 19 21 33 27
# ==============================================================================
def run_q2_heap_homework():
    heap = [0] + list(map(int, input().split()))  # dummy 0 ให้ root เริ่มที่ 1
    size = len(heap) - 1

    if size > 0:
        min_val = heap[1]
        heap[1] = heap[size]
        heap.pop()
        size -= 1

        # ลูปเลื่อนลง (percDown) ตามสไลด์
        i = 1
        while (i * 2) <= size:
            # เลือกลูกตัวที่น้อยกว่า (minChild)
            if i * 2 + 1 > size:
                mc = i * 2
            elif heap[i * 2] < heap[i * 2 + 1]:
                mc = i * 2
            else:
                mc = i * 2 + 1

            # ถ้าแม่มากกว่าลูก ให้สลับที่กัน
            if heap[i] > heap[mc]:
                heap[i], heap[mc] = heap[mc], heap[i]
                i = mc
            else:
                break

        # แสดงผล 2 บรรทัดสไตล์การบ้าน
        print(min_val)
        print(" ".join(map(str, heap[1:])))


# ==============================================================================
# ข้อที่ 3: [COLLISION] Linear Probing Step/Collision Count (สไตล์การบ้านตาราง)
# ==============================================================================
# [คำอธิบาย]
# บรรทัด 1: แสดงจำนวนครั้งที่เกิดการชน (Collisions) ทั้งหมด
# บรรทัด 2: แสดงสภาพตารางแฮชทั้งหมด คั่นด้วยเว้นวรรค
# 
# Sample Input:  77 44 55 20 26 93 17 31 54 11
# Sample Output: 3
#                77 44 55 20 26 93 17 None None 31 54
# ==============================================================================
def run_q3_collision_homework():
    data = list(map(int, input().split()))
    items = data[:-1]
    table_size = data[-1]

    table = [None] * table_size
    total_collisions = 0

    for item in items:
        pos = item % table_size
        while table[pos] is not None:
            total_collisions += 1
            pos = (pos + 1) % table_size
        table[pos] = item

    # แสดงผล 2 บรรทัดสไตล์การบ้าน
    print(total_collisions)
    print(" ".join(map(str, table)))


# ==============================================================================
# จุดเลือกรันในห้องสอบ (ปลด # หน้าข้อที่ตรงกับโจทย์ แล้วกด Run ใน VS Code)
# ==============================================================================
if __name__ == '__main__':
    # run_q1_hash_homework()
    # run_q2_heap_homework()
    # run_q3_collision_homework()
    pass