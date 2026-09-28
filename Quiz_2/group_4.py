# ==============================================================================
# ชุดข้อสอบเก็งเต็ง 4: QUIZ DATA STRUCTURE (Hash, Heap, Tree นิดนึง)
# สไตล์ Grader: รับค่าบรรทัดเดียวผ่าน input().split(), โค้ดสั้น, ไม่ใช้ f-string
# ==============================================================================


# ==============================================================================
# ข้อที่ 1: หมวด HASH (เต็ง 4 - Search Linear Probing และนับจำนวนครั้งที่เปรียบเทียบ)
# อ้างอิงสไลด์: 09,12-Binary Tree and Traversal.pdf หน้า 13
# ==============================================================================
# [คำอธิบายโจทย์]
# รับ input บรรทัดเดียว: สภาพตารางแฮชทั้งหมด และ "ตัวสุดท้ายคือเลขที่ต้องการค้นหา"
# ค้นหาตามลำดับ Linear Probing โดยเริ่มที่ (target % table_size)
# หากเจอ None ให้หยุดค้นหาทันทีตามหลักการในสไลด์
# บรรทัดที่ 1: แสดงว่าเจอหรือไม่ (True หรือ False)
# บรรทัดที่ 2: แสดงจำนวนช่อง/จำนวนครั้งที่ทำการเปรียบเทียบ
#
# [ตัวอย่าง Input]
# 77 44 55 20 26 93 17 None None 31 54 20
# (ตารางแฮชขนาด 11, ตัวสุดท้ายคือเลข 20 ที่ต้องการหา)
#
# [ตัวอย่าง Output]
# True
# 5
# (20 เริ่มเช็กที่ช่อง 9 -> 10 -> 0 -> 1 -> 2 รวมตรวจ 5 ช่องแล้วพบเลข 20)
# ==============================================================================
def q1_hash_search_linear():
    raw_input = input().split()
    raw_table = raw_input[:-1]
    target = int(raw_input[-1])

    table = []
    for x in raw_table:
        if x == "None":
            table.append(None)
        else:
            table.append(int(x))

    table_size = len(table)
    start_pos = target % table_size

    pos = start_pos
    found = False
    count = 0

    while table[pos] is not None:
        count = count + 1
        if table[pos] == target:
            found = True
            break
        pos = (pos + 1) % table_size
        if pos == start_pos:
            break

    print(found)
    print(count)


# ==============================================================================
# ข้อที่ 2: หมวด HEAP (เต็ง 4 - ตรวจสอบความถูกต้องของ Min Heap: is_min_heap)
# อ้างอิงสไลด์: 09-Tree.pdf หน้า 2-3
# ==============================================================================
# [คำอธิบายโจทย์]
# รับ input บรรทัดเดียว: ชุดตัวเลขที่จัดเรียงใน List
# ตรวจสอบว่าชุดตัวเลขนี้มีคุณสมบัติตาม Min Heap หรือไม่
# (เงื่อนไข: พ่อต้องน้อยกว่าหรือเท่ากับลูกซ้ายและลูกขวาทุกตำแหน่งที่มีลูก)
# แสดงผลลัพธ์: True หรือ False
#
# [ตัวอย่าง Input 1]
# 5 9 11 14 18 19 21
# [ตัวอย่าง Output 1]
# True
#
# [ตัวอย่าง Input 2]
# 5 14 11 9 18 19 21
# [ตัวอย่าง Output 2]
# False
# (ที่ index 2 ค่าคือ 14 แต่ลูกซ้ายที่ index 4 ค่าคือ 9 ซึ่งลูกน้อยกว่าพ่อ)
# ==============================================================================
def q2_heap_is_valid_min_heap():
    arr = list(map(int, input().split()))
    heap = [0] + arr
    size = len(arr)
    is_valid = True

    # วนลูปตรวจเฉพาะโหนดที่มีลูก (1 ถึง size // 2)
    for i in range(1, (size // 2) + 1):
        left = i * 2
        right = i * 2 + 1

        if left <= size and heap[i] > heap[left]:
            is_valid = False
            break
        if right <= size and heap[i] > heap[right]:
            is_valid = False
            break

    print(is_valid)


# ==============================================================================
# ข้อที่ 3: หมวด TREE นิดนึง (เต็ง 4 - นับจำนวน Leaf Nodes และ Internal Nodes)
# อ้างอิงสไลด์: 09-Tree.pdf และ 09-Heap.pdf
# ==============================================================================
# [คำอธิบายโจทย์]
# รับ input บรรทัดเดียว: ชุดตัวเลขของ Complete Binary Tree เรียงตาม Level-Order
# บรรทัดที่ 1: แสดงจำนวน Leaf Nodes (โหนดใบที่ไม่มีลูกเลย)
# บรรทัดที่ 2: แสดงจำนวน Internal Nodes (โหนดภายในที่มีลูกอย่างน้อย 1 คน)
#
# [ตัวอย่าง Input]
# 10 5 15 2 7
# (ต้นไม้มี 5 โหนด: โหนดที่มีลูกคือ 10, 5 รวม 2 ตัว | โหนดใบคือ 15, 2, 7 รวม 3 ตัว)
#
# [ตัวอย่าง Output]
# 3
# 2
# ==============================================================================
def q3_tree_count_nodes_type():
    data = list(map(int, input().split()))
    total_nodes = len(data)

    if total_nodes == 0:
        print(0)
        print(0)
        return

    # สำหรับ Complete Binary Tree โหนดที่มีลูกคือ index 1 ถึง (total_nodes // 2)
    internal_nodes = total_nodes // 2
    leaf_nodes = total_nodes - internal_nodes

    print(leaf_nodes)
    print(internal_nodes)


# ==============================================================================
# จุดสลับเลือกรันข้อสอบในห้องสอบ
# ==============================================================================
if __name__ == '__main__':
    # q1_hash_search_linear()
    # q2_heap_is_valid_min_heap()
    # q3_tree_count_nodes_type()
    pass