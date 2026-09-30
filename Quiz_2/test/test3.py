# ==============================================================================
# quiz2_homework_level.py
# รวมโค้ดระดับเดียวกับการบ้าน Grader เป๊ะๆ (สั้น ง่าย ตรงไปตรงมา 5-10 บรรทัดจบ)
# ==============================================================================


# ------------------------------------------------------------------------------
# ข้อที่ 1: [HASH] Weighted ASCII Hash (แบบเดียวกับการบ้าน EX_24 เป๊ะ)
# บรรทัด 1: แสดงผลคูณ ord(c) * ตำแหน่ง ของแต่ละตัว
# บรรทัด 2: แสดงผลลัพธ์ตำแหน่ง slot ในตาราง
# Sample Input:  cat 11
# Sample Output: 99 194 348
#                3
# ------------------------------------------------------------------------------
def run_hash_weighted():
    text, size_str = input().split()
    table_size = int(size_str)

    # 1. หาผลคูณ ord(c) * (i + 1)
    terms = [str(ord(text[i]) * (i + 1)) for i in range(len(text))]
    
    # 2. รวมผลลัพธ์แล้วหาเศษ (% table_size)
    slot = sum(map(int, terms)) % table_size

    print(" ".join(terms))
    print(slot)


# ------------------------------------------------------------------------------
# ข้อที่ 2: [COLLISION] Linear Probing หยอดข้อมูลลงตาราง
# บรรทัด 1: แสดงตำแหน่ง slot เริ่มต้นของข้อมูลแต่ละตัว (ก่อนเกิดการชน)
# บรรทัด 2: แสดงสภาพตารางแฮชทั้งหมดหลังหยอดเสร็จ
# Sample Input:  77 44 55 11
#                (ข้อมูลคือ 77 44 55 และขนาดตารางคือ 11)
# Sample Output: 0 0 0
#                77 44 55 None None None None None None None None
# ------------------------------------------------------------------------------
def run_hash_linear_probing():
    data = list(map(int, input().split()))
    items = data[:-1]
    table_size = data[-1]

    table = [None] * table_size
    initial_slots = []

    for item in items:
        pos = item % table_size
        initial_slots.append(str(pos))
        
        # ถ้าช่องไม่ว่าง ขยับไปช่องถัดไปทีละ 1
        while table[pos] is not None:
            pos = (pos + 1) % table_size
        table[pos] = item

    print(" ".join(initial_slots))
    print(" ".join(map(str, table)))


# ------------------------------------------------------------------------------
# ข้อที่ 3: [HEAP] delMin ดึงค่าน้อยสุดออก (ตามโน้ต # Quiz Heap ในสไลด์)
# บรรทัด 1: แสดงค่าต่ำสุดที่ถูกดึงออก (Root เดิม)
# บรรทัด 2: แสดงสภาพ Heap ที่เหลือทั้งหมดหลัง percDown เสร็จ
# Sample Input:  5 9 11 14 18 19 21 33 17 27
# Sample Output: 5
#                9 14 11 17 18 19 21 33 27
# ------------------------------------------------------------------------------
def run_heap_delmin():
    heap = [0] + list(map(int, input().split()))  # dummy 0 ให้ Root = 1
    size = len(heap) - 1

    min_val = heap[1]
    heap[1] = heap[size]
    heap.pop()
    size -= 1

    # ดันค่าลง (percDown)
    i = 1
    while (i * 2) <= size:
        # เลือกลูกตัวที่น้อยกว่า
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

    print(min_val)
    print(" ".join(map(str, heap[1:])))


# ------------------------------------------------------------------------------
# ข้อที่ 4: [HEAP] หาความสัมพันธ์ของโหนด (Parent, Left Child, Right Child)
# บรรทัด 1: แสดงค่าของลูกซ้ายและลูกขวา (ถ้าไม่มีให้แสดง None)
# บรรทัด 2: แสดงค่าของโหนดแม่ (Parent)
# Sample Input:  5 9 11 14 18 19 21 2
#                (Heap เดิม, เลข 2 ตัวท้ายคือ index ที่ต้องการตรวจ)
# Sample Output: 14 18
#                5
# ------------------------------------------------------------------------------
def run_heap_find_family():
    data = list(map(int, input().split()))
    heap = [0] + data[:-1]
    idx = data[-1]
    size = len(heap) - 1

    parent = heap[idx // 2] if idx // 2 > 0 else "None"
    left = heap[idx * 2] if idx * 2 <= size else "None"
    right = heap[idx * 2 + 1] if idx * 2 + 1 <= size else "None"

    print(str(left) + " " + str(right))
    print(parent)


# ==============================================================================
# จุดสลับเลือกรันใน VS Code
# (เอา # ออกหน้าข้อที่ต้องการทดสอบ แล้วกด Run Code)
# ==============================================================================
if __name__ == '__main__':
    # run_hash_weighted()
    # run_hash_linear_probing()
    # run_heap_delmin()
    # run_heap_find_family()
    pass