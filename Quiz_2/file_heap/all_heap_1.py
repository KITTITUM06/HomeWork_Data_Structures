# โครงสร้าง: ใช้ List โดยช่อง index 0 เก็บค่า dummy 0 ไว้เสมอ (Root อยู่ index 1)
# สูตรหลัก: Parent = i // 2 | Left Child = 2*i | Right Child = 2*i + 1
# ==============================================================================

# ข้อที่ 1: การเพิ่มข้อมูลใหม่ลงใน Min Heap (Insert & Percolate Up)
# ==============================================================================
# [คีย์เวิร์ดในโจทย์]
# - เพิ่มข้อมูล, แทรกค่า, insert, percolate up, ดันขึ้นบน, นำค่าใหม่ใส่ในฮีพ

# [ลักษณะ Input / Output]
# Input บรรทัดที่ 1: ชุดตัวเลขใน Heap เดิม (คั่นด้วยเว้นวรรค)
# Input บรรทัดที่ 2: ค่าตัวเลขใหม่ที่ต้องการเพิ่มเข้าไป 1 ค่า
# Output: ชุดตัวเลขใน Heap ใหม่หลังการจัดระเบียบดันขึ้นบนเสร็จสมบูรณ์

# [ตัวอย่างทดสอบ]
# Input:
# 5 9 11 14 18 19 21 33 17 27
# 7

# Output:
# 5 7 11 14 9 19 21 33 17 27 18
# ==============================================================================
def q1_insert():
    heap = [0] + list(map(int, input().split()))  # ใส่ dummy 0 เพื่อให้ root เริ่มที่ index 1
    new_val = int(input())

    heap.append(new_val)      # 1. นำข้อมูลใหม่ไปต่อท้ายสุด
    i = len(heap) - 1

    # 2. ดันค่าขึ้นด้านบน เทียบกับตำแหน่งพ่อ (i // 2)
    while i // 2 > 0:
        if heap[i] < heap[i // 2]:
            heap[i], heap[i // 2] = heap[i // 2], heap[i]
            i = i // 2
        else:
            break

    # แสดงผลลัพธ์ตั้งแต่ช่อง 1 เป็นต้นไป โดยแปลงเป็นสตริงเชื่อมด้วยเว้นวรรค
    print(" ".join(map(str, heap[1:])))


# ==============================================================================
# ข้อที่ 2: การลบค่าน้อยสุดออกแล้วเลื่อนลง (delMin & Percolate Down)
# *ในสไลด์อาจารย์เขียนโน้ตลายมือว่า "Quiz Heap" เน้น minChild ค่าน้อยสุดเสมอ*
# ==============================================================================
# [คีย์เวิร์ดในโจทย์]
# - ลบค่าน้อยสุด, delMin, remove min, percolate down, เลื่อนลงล่าง, minChild
#
# [ลักษณะ Input / Output]
# Input: ชุดตัวเลขใน Min Heap (คั่นด้วยเว้นวรรค)
# Output บรรทัดที่ 1: ค่าต่ำสุดที่ถูกลบออก (Root)
# Output บรรทัดที่ 2: สภาพ Min Heap ที่เหลือหลังเลื่อนลงสมบูรณ์
#
# [ตัวอย่างทดสอบ]
# Input:
# 5 9 11 14 18 19 21 33 17 27

# Output:
# 5
# 9 14 11 17 18 19 21 33 27
# ==============================================================================
def min_child(h, i, size):
    # กรณีมีลูกซ้ายคนเดียว (ไม่มีลูกขวา)
    if i * 2 + 1 > size:
        return i * 2
    # กรณีมีทั้งสองลูก เลือกลูกตัวที่ค่าน้อยกว่าเสมอ
    if h[i * 2] < h[i * 2 + 1]:
        return i * 2
    else:
        return i * 2 + 1

def q2_delmin():
    heap = [0] + list(map(int, input().split()))
    size = len(heap) - 1
    if size == 0:
        return

    min_val = heap[1]             # เก็บค่าตัวน้อยสุดเดิมไว้
    heap[1] = heap[size]          # เอาตัวท้ายสุดขึ้นมาแทนที่ Root
    heap.pop()                    # ลบช่องท้ายสุดออก
    size = size - 1

    # ดันค่าลงข้างล่าง (percDown)
    i = 1
    while (i * 2) <= size:
        mc = min_child(heap, i, size)
        if heap[i] > heap[mc]:
            heap[i], heap[mc] = heap[mc], heap[i]
            i = mc
        else:
            break

    print(min_val)
    print(" ".join(map(str, heap[1:])))


# ==============================================================================
# ข้อที่ 3: สร้าง Min Heap จาก List ทั้งก้อน (buildHeap ใน O(n))
# ==============================================================================
# [คีย์เวิร์ดในโจทย์]
# - buildHeap, สร้างฮีพจาก list, แปลงชุดตัวเลขเป็นฮีพ, O(n)
#
# [ลักษณะ Input / Output]
# Input: ชุดตัวเลขที่ยังไม่ได้เรียงลำดับ 1 บรรทัด (คั่นด้วยเว้นวรรค)
# Output: ลำดับตัวเลขหลังจัดรูปเป็น Min Heap สมบูรณ์
#
# [ตัวอย่างทดสอบ]
# Input:
# 9 5 6 2 3
# Output:
# 2 3 6 5 9
# ==============================================================================
def q3_buildheap():
    arr = list(map(int, input().split()))
    size = len(arr)
    heap = [0] + arr  

    def perc_down(i):
        while (i * 2) <= size:
            mc = min_child(heap, i, size)
            if heap[i] > heap[mc]:
                heap[i], heap[mc] = heap[mc], heap[i]
                i = mc
            else:
                break

    # เริ่มทำจากตัวสุดท้ายที่มีลูก (len // 2) วิ่งถอยหลังมาหา Root (index 1)
    i = size // 2
    while i > 0:
        perc_down(i)
        i = i - 1

    print(" ".join(map(str, heap[1:])))


# ==============================================================================
# ข้อที่ 4: ตรวจสอบความสัมพันธ์ Parent และ Children ตามตำแหน่ง Index
# ==============================================================================
# [คีย์เวิร์ดในโจทย์]
# - หา parent, หา child, หาโหนดพ่อ, หาโหนดลูกซ้ายขวา, index ของฮีพ
#
# [ลักษณะ Input / Output]
# Input บรรทัดที่ 1: ชุดตัวเลขใน Min Heap (คั่นด้วยเว้นวรรค)
# Input บรรทัดที่ 2: เลข index ที่ต้องการตรวจสอบ (เริ่มนับที่ 1)
# Output: แสดงค่าของ Parent, Left Child, Right Child (หากไม่มีให้แสดง None)
#
# [ตัวอย่างทดสอบ]
# Input:
# 5 9 11 14 18 19 21
# 2
# Output:
# Parent: 5
# Left: 14
# Right: 18
# ==============================================================================
def q4_find_family():
    heap = [0] + list(map(int, input().split()))
    target = int(input())
    size = len(heap) - 1

    # Parent อยู่ที่ index 
    if target // 2 > 0:
        parent = heap[target // 2]
    else:
        parent = "None"

    # Left Child อยู่ที่ 2 * index
    if target * 2 <= size:
        left = heap[target * 2]
    else:
        left = "None"

    # Right Child อยู่ที่ 2 * index + 1
    if target * 2 + 1 <= size:
        right = heap[target * 2 + 1]
    else:
        right = "None"

    print("Parent: " + str(parent))
    print("Left: " + str(left))
    print("Right: " + str(right))


# ==============================================================================
# จุดสลับเลือกรันข้อสอบใน VS Code
# (เวลาต้องการรันข้อไหน ให้ลบเครื่องหมาย # หน้าข้อนั้นออก แล้วกด Run Python File)
# ==============================================================================
if __name__ == '__main__':
    # q1_insert()
    # q2_delmin()
    # q3_buildheap()
    # q4_find_family()
    pass