"""
ชุดแนวข้อสอบและแบบฝึกหัดปฏิบัติการวิชา Data Structures & Algorithms
เรื่อง: Hash Table และ Heap (35 ข้อ พร้อมโค้ดเฉลย)
ลักษณะโจทย์: อิงตามแนวการเขียนโปรแกรมและการรับค่า input() ตามสไลด์ผู้สอน
"""

# ==============================================================================
# หมวดที่ 1: ฟังก์ชันแฮชพื้นฐาน (Hash Functions)
# ==============================================================================

# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 1: วิธีการพับ (Shift Folding) - ตรงตามสไลด์อาจารย์
# รับค่า int สองค่า คั่นด้วย spacebar คือ ชุดตัวเลข และ ขนาดช่วงการแบ่ง
# แสดงผลลัพธ์การแบ่งช่วง และ ผลบวกของการแบ่งช่วง
# Input:  123456789 2
# Output: 12 34 56 78 9
#         189
# ------------------------------------------------------------------------------
data_input = input().split()
num_str = data_input[0]
fold_size = int(data_input[1])

chunks = []
for i in range(0, len(num_str), fold_size):
    chunks.append(num_str[i : i + fold_size])

print(" ".join(chunks))
total_sum = sum(int(chunk) for chunk in chunks)
print(total_sum)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 2: วิธีการพับแบบกลับด้านขอบ (Boundary Folding)
# แบ่งชุดตัวเลขตามขนาดที่กำหนด โดยชิ้นส่วนตำแหน่งคู่ (index 1, 3, ...) ให้กลับด้านตัวเลข (Reverse)
# ก่อนนำมารวมกันและหาผลรวม
# Input:  123456789 2
# Output: 12 43 56 87 9
#         207
# ------------------------------------------------------------------------------
data = input().split()
num_str = data[0]
fold_size = int(data[1])

chunks = [num_str[i : i + fold_size] for i in range(0, len(num_str), fold_size)]
transformed = []
for idx, chunk in enumerate(chunks):
    if idx % 2 == 1:
        transformed.append(chunk[::-1])
    else:
        transformed.append(chunk)

print(" ".join(transformed))
print(sum(int(c) for c in transformed))


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 3: ยกกำลังแล้วหาตัวกลาง (Mid-Square / Mid-Power) - ตรงตามสไลด์อาจารย์
# รับค่า int 3 ค่า: ตัวเลขฐาน, จำนวนยกกำลัง, และความยาวตัวกลางที่ต้องการ
# หากช่วงตัวกลางแบ่งไม่ลงตัว ให้ปัดเอาตำแหน่งด้านหน้า
# Input:  44 2 2
# Output: 1936
#         93
# ------------------------------------------------------------------------------
data = input().split()
base = int(data[0])
power = int(data[1])
mid_len = int(data[2])

result_num = base ** power
result_str = str(result_num)
print(result_str)

total_len = len(result_str)
start_idx = (total_len - mid_len) // 2
mid_digits = result_str[start_idx : start_idx + mid_len]
print(mid_digits)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 4: Mid-Square Hashing หา Hash Index ของตาราง
# นำเลข key มายกกำลัง 2 ดึงเลขตรงกลางตามความยาวที่กำหนด แล้ว mod ด้วยขนาดตาราง m
# Input:  44 2 11   (key=44, ดึงตรงกลาง 2 หลัก, ขนาดตาราง m=11 -> 44^2=1936 -> mid="93" -> 93 % 11 = 5)
# Output: 5
# ------------------------------------------------------------------------------
key, mid_len, table_size = map(int, input().split())
squared = str(key ** 2)
start_idx = (len(squared) - mid_len) // 2
mid_val = int(squared[start_idx : start_idx + mid_len])
hash_index = mid_val % table_size
print(hash_index)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 5: Division Method (Modulo Hashing)
# รับค่า key และขนาดตาราง m คำนวณหาช่องดัชนี h(k) = k mod m
# Input:  47 11
# Output: 3
# ------------------------------------------------------------------------------
k, m = map(int, input().split())
print(k % m)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 6: การสกัดหลักตัวเลข (Digit Extraction Hashing)
# รับตัวเลขรหัสนักศึกษา และตำแหน่งหลักที่ต้องการนำมารวมกัน (1-based index) แล้ว mod ด้วยขนาดตาราง
# Input:  65010999 1 3 5 10  (เลข 65010999, เอาหลักที่ 1, 3, 5 คือ '6', '0', '0' -> รวมกัน 600 -> mod 10 = 0)
# Output: 0
# ------------------------------------------------------------------------------
data = input().split()
student_id = data[0]
pos1, pos2, pos3, table_size = int(data[1]), int(data[2]), int(data[3]), int(data[4])

extracted_str = student_id[pos1 - 1] + student_id[pos2 - 1] + student_id[pos3 - 1]
extracted_val = int(extracted_str)
print(extracted_val % table_size)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 7: Multiplicative Hash Function
# สูตร h(k) = floor(m * (k * A mod 1)) กำหนดให้ A = 0.618033
# Input:  12345 100
# Output: ดัชนีแฮช
# ------------------------------------------------------------------------------
import math

k, m = map(int, input().split())
A = 0.618033
fractional_part = (k * A) % 1
hash_index = math.floor(m * fractional_part)
print(hash_index)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 8: String Hashing ด้วยผลรวมรหัส ASCII
# รับข้อความภาษาอังกฤษและขนาดตาราง m หาผลรวม ASCII ของทุกตัวอักษรแล้ว mod m
# Input:  DATA 7
# Output: 4  ('D'=68, 'A'=65, 'T'=84, 'A'=65 -> รวม 282 % 7 = 2)
# ------------------------------------------------------------------------------
text, m = input().split()
m = int(m)
ascii_sum = sum(ord(ch) for ch in text)
print(ascii_sum % m)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 9: Weighted String Hashing (ถ่วงน้ำหนักตามตำแหน่ง)
# สูตร h(s) = sum((index + 1) * ord(char)) mod m
# Input:  CAT 13
# Output: ค่า Hash Index
# ------------------------------------------------------------------------------
text, m = input().split()
m = int(m)
weighted_sum = sum((i + 1) * ord(ch) for i, ch in enumerate(text))
print(weighted_sum % m)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 10: Polynomial Rolling Hash สำหรับ String
# สูตร h(s) = (s[0]*p^0 + s[1]*p^1 + ... + s[n-1]*p^(n-1)) mod m กำหนด p = 31
# Input:  algo 1009
# Output: ค่าแฮชหลัง mod 1009
# ------------------------------------------------------------------------------
text, m = input().split()
m = int(m)
p = 31
hash_val = 0
for i, ch in enumerate(text):
    hash_val = (hash_val + ord(ch) * (p ** i)) % m
print(hash_val)


# ==============================================================================
# หมวดที่ 2: การจัดการการชน (Collision Resolution in Hash Table)
# ==============================================================================

# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 11: Linear Probing - การแทรกข้อมูลลงตาราง
# รับขนาดตาราง m และชุดตัวเลข ให้แทรกทีละตัว หากชนให้เลื่อนไปช่องถัดไปทีละ 1 (mod m)
# ช่องว่างให้แทนด้วย -1
# Input:  5
#         10 15 20
# Output: [10, 15, 20, -1, -1]
# ------------------------------------------------------------------------------
m = int(input())
nums = list(map(int, input().split()))

table = [-1] * m
for x in nums:
    idx = x % m
    while table[idx] != -1:
        idx = (idx + 1) % m
    table[idx] = x

print(table)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 12: Linear Probing - นับจำนวนครั้งที่เกิดการชน (Collisions)
# ให้แทรกชุดตัวเลขลง Hash Table แล้วพิมพ์จำนวนครั้งการชนทั้งหมดที่เกิดขึ้น
# Input:  7
#         14 21 28
# Output: 3  (21 ชน 14 นับ 1, 28 ชน 14 และ 21 นับอีก 2 รวมเป็น 3)
# ------------------------------------------------------------------------------
m = int(input())
nums = list(map(int, input().split()))

table = [-1] * m
total_collisions = 0

for x in nums:
    idx = x % m
    while table[idx] != -1:
        total_collisions += 1
        idx = (idx + 1) % m
    table[idx] = x

print(total_collisions)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 13: Linear Probing - ค้นหาข้อมูลและนับจำนวนก้าวที่ตรวจ (Probe Steps)
# รับขนาดตาราง m, ข้อมูลที่อยู่ในตาราง และค่าเป้าหมาย target ที่ต้องการค้นหา
# พิมพ์ index ที่พบ target และจำนวนครั้งที่วนตรวจ ถ้าไม่พบให้พิมพ์ -1
# Input:  5
#         10 15 20
#         15
# Output: Found at index: 1, Probes: 2
# ------------------------------------------------------------------------------
m = int(input())
nums = list(map(int, input().split()))
target = int(input())

table = [-1] * m
for x in nums:
    idx = x % m
    while table[idx] != -1:
        idx = (idx + 1) % m
    table[idx] = x

# ค้นหา target
start_idx = target % m
curr_idx = start_idx
probes = 0
found_idx = -1

for _ in range(m):
    probes += 1
    if table[curr_idx] == target:
        found_idx = curr_idx
        break
    if table[curr_idx] == -1:
        break
    curr_idx = (curr_idx + 1) % m

if found_idx != -1:
    print(f"Found at index: {found_idx}, Probes: {probes}")
else:
    print(f"Not Found, Probes: {probes}")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 14: Quadratic Probing - การแทรกข้อมูล
# หากเกิดการชน ให้ใช้สูตร h_i = (h(k) + i^2) mod m โดย i = 1, 2, 3, ...
# Input:  7
#         7 14 21
# Output: [7, 14, -1, -1, 21, -1, -1]
# ------------------------------------------------------------------------------
m = int(input())
nums = list(map(int, input().split()))

table = [-1] * m
for x in nums:
    h = x % m
    i = 0
    while table[(h + i * i) % m] != -1:
        i += 1
    table[(h + i * i) % m] = x

print(table)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 15: Double Hashing - การแทรกข้อมูล
# กำหนด h1(k) = k mod m และ h2(k) = prime - (k mod prime)
# สูตรช่องถัดไปเมื่อชน: (h1(k) + i * h2(k)) mod m
# Input:  7 5
#         12 19 26
# Output: ตาราง Hash หลังแทรก
# ------------------------------------------------------------------------------
m, prime = map(int, input().split())
nums = list(map(int, input().split()))

table = [-1] * m
for x in nums:
    h1 = x % m
    h2 = prime - (x % prime)
    i = 0
    while table[(h1 + i * h2) % m] != -1:
        i += 1
    table[(h1 + i * h2) % m] = x

print(table)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 16: Separate Chaining - การสร้างตารางแฮชแบบ Bucket List
# ใช้ List ภายในแต่ละช่อง เพื่อเก็บข้อมูลที่ชนกัน
# Input:  5
#         12 17 22 5 9
# Output: แต่ละบรรทัดแสดง Index และข้อมูลใน Bucket นั้น
# ------------------------------------------------------------------------------
m = int(input())
nums = list(map(int, input().split()))

table = [[] for _ in range(m)]
for x in nums:
    table[x % m].append(x)

for i in range(m):
    print(f"{i}: {table[i]}")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 17: คำนวณ Load Factor และตรวจสอบการ Rehash
# รับขนาดตารางปัจจุบัน m, จำนวนข้อมูล n และ Threshold ที่กำหนด
# หาก Load Factor (n/m) > Threshold ให้พิมพ์ "REHASH NEEDED" มิฉะนั้นพิมพ์ "OK"
# Input:  10 8 0.75
# Output: Load Factor: 0.80 -> REHASH NEEDED
# ------------------------------------------------------------------------------
m, n, threshold = input().split()
m = int(m)
n = int(n)
threshold = float(threshold)

load_factor = n / m
print(f"Load Factor: {load_factor:.2f}")
if load_factor > threshold:
    print("REHASH NEEDED")
else:
    print("OK")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 18: Linear Probing พร้อมการลบข้อมูล (Tombstone / Marker)
# เมื่อลบข้อมูลให้แทนที่ด้วย 'DELETED' เพื่อไม่ให้กระทบต่อการสืบค้น
# Input:  5
#         10 15 20
#         15
# Output: ตารางหลังลบค่า 15
# ------------------------------------------------------------------------------
m = int(input())
nums = list(map(int, input().split()))
delete_val = int(input())

table = [-1] * m
for x in nums:
    idx = x % m
    while table[idx] != -1:
        idx = (idx + 1) % m
    table[idx] = x

# ลบข้อมูล
for i in range(m):
    if table[i] == delete_val:
        table[i] = "DELETED"
        break

print(table)


# ==============================================================================
# หมวดที่ 3: โครงสร้างและคุณสมบัติของ Heap (Heap Properties)
# ==============================================================================

# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 19: คำนวณตำแหน่ง Parent, Left Child, Right Child (0-indexed)
# รับจำนวนสมาชิก n และตำแหน่ง i ที่ต้องการตรวจสอบ หากไม่มีให้แสดง -1
# Input:  7 1
# Output: Parent: 0, Left: 3, Right: 4
# ------------------------------------------------------------------------------
n, i = map(int, input().split())

parent = (i - 1) // 2 if i > 0 else -1
left = 2 * i + 1 if (2 * i + 1) < n else -1
right = 2 * i + 2 if (2 * i + 2) < n else -1

print(f"Parent: {parent}, Left: {left}, Right: {right}")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 20: ตรวจสอบว่าเป็น Min-Heap หรือไม่ (Is Min-Heap?)
# ตรวจสอบว่าโหนดพ่อทุกโหนดต้องมีค่าน้อยกว่าหรือเท่ากับโหนดลูกเสมอ
# Input:  3 5 8 10 12 9
# Output: YES (ถ้าไม่ใช่ให้พิมพ์ NO)
# ------------------------------------------------------------------------------
arr = list(map(int, input().split()))
n = len(arr)
is_min_heap = True

for i in range((n - 2) // 2 + 1):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] > arr[left]:
        is_min_heap = False
        break
    if right < n and arr[i] > arr[right]:
        is_min_heap = False
        break

print("YES" if is_min_heap else "NO")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 21: ตรวจสอบว่าเป็น Max-Heap หรือไม่ (Is Max-Heap?)
# ตรวจสอบว่าโหนดพ่อทุกโหนดต้องมีค่ามากกว่าหรือเท่ากับโหนดลูกเสมอ
# Input:  20 15 10 8 12
# Output: YES
# ------------------------------------------------------------------------------
arr = list(map(int, input().split()))
n = len(arr)
is_max_heap = True

for i in range((n - 2) // 2 + 1):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        is_max_heap = False
        break
    if right < n and arr[i] < arr[right]:
        is_max_heap = False
        break

print("YES" if is_max_heap else "NO")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 22: หาจำนวนโหนดใบ (Leaf Nodes) และโหนดภายใน (Internal Nodes)
# จากขนาดของ Heap n โหนดที่ดัชนี floor(n/2) ถึง n-1 จะเป็น Leaf Nodes เสมอ
# Input:  7
# Output: Internal Nodes: 3, Leaf Nodes: 4
# ------------------------------------------------------------------------------
n = int(input())
internal_count = n // 2
leaf_count = n - internal_count
print(f"Internal Nodes: {internal_count}, Leaf Nodes: {leaf_count}")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 23: คำนวณความสูงของ Heap (Height of Complete Binary Tree)
# รับจำนวนโหนด n หาความสูงของต้นไม้ (โหนดเดี่ยวสูง 0)
# Input:  10
# Output: Height: 3  (เพราะ 2^3 <= 10 < 2^4)
# ------------------------------------------------------------------------------
import math

n = int(input())
if n <= 0:
    print("Height: -1")
else:
    height = math.floor(math.log2(n))
    print(f"Height: {height}")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 24: ค้นหาค่าต่ำสุดใน Max-Heap
# ค่าต่ำสุดของ Max-Heap จะต้องอยู่ที่ Leaf Node เสมอ (ตั้งแต่ index n//2 ถึง n-1)
# Input:  50 30 40 10 20 35 38
# Output: Minimum value: 10
# ------------------------------------------------------------------------------
arr = list(map(int, input().split()))
n = len(arr)
leaf_nodes = arr[n // 2 :]
print(f"Minimum value: {min(leaf_nodes)}")


# ==============================================================================
# หมวดที่ 4: การแทรกและการลบใน Heap (Heap Operations: Sift-Up / Sift-Down)
# ==============================================================================

# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 25: Min-Heap Insertion (Sift-Up)
# มี Min-Heap เดิมอยู่ รับค่าใหม่ 1 ค่า นำไปต่อท้ายแล้วทำ Sift-Up
# Input:  10 20 30 40 50
#         15
# Output: [10, 20, 15, 40, 50, 30]
# ------------------------------------------------------------------------------
heap = list(map(int, input().split()))
val = int(input())

heap.append(val)
curr = len(heap) - 1

while curr > 0:
    parent = (curr - 1) // 2
    if heap[curr] < heap[parent]:
        heap[curr], heap[parent] = heap[parent], heap[curr]
        curr = parent
    else:
        break

print(heap)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 26: Max-Heap Insertion (Sift-Up)
# มี Max-Heap เดิมอยู่ รับค่าใหม่ 1 ค่า นำไปต่อท้ายแล้วทำ Sift-Up
# Input:  50 40 30 10 20
#         45
# Output: [50, 40, 45, 10, 20, 30]
# ------------------------------------------------------------------------------
heap = list(map(int, input().split()))
val = int(input())

heap.append(val)
curr = len(heap) - 1

while curr > 0:
    parent = (curr - 1) // 2
    if heap[curr] > heap[parent]:
        heap[curr], heap[parent] = heap[parent], heap[curr]
        curr = parent
    else:
        break

print(heap)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 27: Min-Heap Extract-Min (Delete Root & Sift-Down)
# ลบค่า Root (ค่าน้อยที่สุด) นำตัวสุดท้ายขึ้นแทนที่ แล้วทำ Sift-Down
# Input:  5 10 20 30 15
# Output: Extracted: 5
#         Remaining Heap: [10, 15, 20, 30]
# ------------------------------------------------------------------------------
heap = list(map(int, input().split()))

if heap:
    min_val = heap[0]
    last_val = heap.pop()
    if heap:
        heap[0] = last_val
        curr = 0
        n = len(heap)
        while True:
            left = 2 * curr + 1
            right = 2 * curr + 2
            smallest = curr

            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right

            if smallest != curr:
                heap[curr], heap[smallest] = heap[smallest], heap[curr]
                curr = smallest
            else:
                break
    print(f"Extracted: {min_val}")
    print(f"Remaining Heap: {heap}")


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 28: Max-Heap Extract-Max (Delete Root & Sift-Down)
# ลบค่า Root (ค่ามากที่สุด) นำตัวสุดท้ายขึ้นแทนที่ แล้วทำ Sift-Down
# Input:  50 30 40 10 20
# Output: Extracted: 50
#         Remaining Heap: [40, 30, 20, 10]
# ------------------------------------------------------------------------------
heap = list(map(int, input().split()))

if heap:
    max_val = heap[0]
    last_val = heap.pop()
    if heap:
        heap[0] = last_val
        curr = 0
        n = len(heap)
        while True:
            left = 2 * curr + 1
            right = 2 * curr + 2
            largest = curr

            if left < n and heap[left] > heap[largest]:
                largest = left
            if right < n and heap[right] > heap[largest]:
                largest = right

            if largest != curr:
                heap[curr], heap[largest] = heap[largest], heap[curr]
                curr = largest
            else:
                break
    print(f"Extracted: {max_val}")
    print(f"Remaining Heap: {heap}")


# ==============================================================================
# หมวดที่ 5: การสร้าง Heap, เรียงลำดับ และการประยุกต์ใช้งาน (Heapify & Sorting)
# ==============================================================================

# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 29: Build Min-Heap ด้วยกระบวนการ Heapify (Bottom-Up)
# รับ Array ตัวเลขธรรมดา แปลงเป็น Min-Heap โดยเริ่ม Sift-Down จากตัวพ่อล่างสุด
# Input:  9 4 7 1 -2 6 5
# Output: [-2, 1, 5, 4, 9, 6, 7]
# ------------------------------------------------------------------------------
arr = list(map(int, input().split()))
n = len(arr)

def sift_down_min(arr, n, i):
    curr = i
    while True:
        left = 2 * curr + 1
        right = 2 * curr + 2
        smallest = curr
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != curr:
            arr[curr], arr[smallest] = arr[smallest], arr[curr]
            curr = smallest
        else:
            break

for i in range((n - 2) // 2, -1, -1):
    sift_down_min(arr, n, i)

print(arr)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 30: Build Max-Heap ด้วยกระบวนการ Heapify (Bottom-Up)
# รับ Array ตัวเลข แปลงเป็น Max-Heap
# Input:  1 3 5 4 6 13 10
# Output: [13, 6, 10, 4, 3, 1, 5]
# ------------------------------------------------------------------------------
arr = list(map(int, input().split()))
n = len(arr)

def sift_down_max(arr, n, i):
    curr = i
    while True:
        left = 2 * curr + 1
        right = 2 * curr + 2
        largest = curr
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != curr:
            arr[curr], arr[largest] = arr[largest], arr[curr]
            curr = largest
        else:
            break

for i in range((n - 2) // 2, -1, -1):
    sift_down_max(arr, n, i)

print(arr)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 31: Heap Sort เรียงจากน้อยไปมาก (Ascending)
# สร้าง Max-Heap แล้วสลับ Root กับตัวท้าย ลดขอบเขตแล้ว Heapify ซ้ำ
# Input:  12 11 13 5 6 7
# Output: 5 6 7 11 12 13
# ------------------------------------------------------------------------------
arr = list(map(int, input().split()))
n = len(arr)

def max_heapify(a, size, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < size and a[l] > a[largest]:
        largest = l
    if r < size and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, size, largest)

# สร้าง Max-Heap
for i in range(n // 2 - 1, -1, -1):
    max_heapify(arr, n, i)

# Heap Sort
for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    max_heapify(arr, i, 0)

print(" ".join(map(str, arr)))


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 32: Heap Sort เรียงจากมากไปน้อย (Descending)
# สร้าง Min-Heap แล้วสลับ Root กับตัวท้าย
# Input:  12 11 13 5 6 7
# Output: 13 12 11 7 6 5
# ------------------------------------------------------------------------------
arr = list(map(int, input().split()))
n = len(arr)

def min_heapify(a, size, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < size and a[l] < a[smallest]:
        smallest = l
    if r < size and a[r] < a[smallest]:
        smallest = r
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
        min_heapify(a, size, smallest)

for i in range(n // 2 - 1, -1, -1):
    min_heapify(arr, n, i)

for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    min_heapify(arr, i, 0)

print(" ".join(map(str, arr)))


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 33: หาค่าที่มากที่สุดเป็นอันดับที่ K (K-th Largest Element)
# ใช้ Min-Heap ขนาด K โดยสมาชิกที่หัว Heap จะเป็นคำตอบ
# Input:  3 2 1 5 6 4
#         2
# Output: 5
# ------------------------------------------------------------------------------
import heapq

nums = list(map(int, input().split()))
k = int(input())

min_heap = []
for x in nums:
    heapq.heappush(min_heap, x)
    if len(min_heap) > k:
        heapq.heappop(min_heap)

print(min_heap[0])


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 34: หาค่าที่น้อยที่สุดเป็นอันดับที่ K (K-th Smallest Element)
# นำข้อมูลเข้า Min-Heap แล้ว pop ออกมา k ครั้ง
# Input:  7 10 4 3 20 15
#         3
# Output: 7  (ลำดับ: 3, 4, 7)
# ------------------------------------------------------------------------------
import heapq

nums = list(map(int, input().split()))
k = int(input())

heapq.heapify(nums)
kth_smallest = None
for _ in range(k):
    kth_smallest = heapq.heappop(nums)

print(kth_smallest)


# ------------------------------------------------------------------------------
# โจทย์ข้อที่ 35: ต่อเชือกด้วยต้นทุนต่ำสุด (Minimum Cost of Connecting Ropes)
# มีเชือกหลายเส้น ต้องการต่อให้เป็นเส้นเดียว โดยต้นทุนการต่อแต่ละครั้งเท่ากับผลรวมความยาวเชือก
# ให้หาต้นทุนรวมที่ต่ำที่สุด (ใช้ Min-Heap ดึง 2 เส้นที่สั้นที่สุดมาต่อกันเสมอ)
# Input:  4 3 2 6
# Output: Total Minimum Cost: 29
# ------------------------------------------------------------------------------
import heapq

ropes = list(map(int, input().split()))
heapq.heapify(ropes)

total_cost = 0
while len(ropes) > 1:
    first = heapq.heappop(ropes)
    second = heapq.heappop(ropes)
    cost = first + second
    total_cost += cost
    heapq.heappush(ropes, cost)

print(f"Total Minimum Cost: {total_cost}")