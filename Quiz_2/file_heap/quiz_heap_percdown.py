# ==============================================================================
# ข้อสอบเต็ง 1: percDown + minChild (ตามหน้าสไลด์ที่เขียน # Quiz Heap เป๊ะๆ)
# อ้างอิงสไลด์: 09-Tree.pdf (หน้า 7)
# ==============================================================================

# รับข้อมูล Min Heap ในบรรทัดเดียว (ใส่ dummy 0 ไว้ตำแหน่งแรกเพื่อให้ root อยู่ index 1)
heap = [0] + list(map(int, input().split()))
size = len(heap) - 1

# 1. ฟังก์ชัน minChild ตามสไลด์ฝั่งขวา
def min_child(h, i, current_size):
    # ถ้ามีลูกคนเดียว (ลูกซ้าย)
    if i * 2 + 1 > current_size:
        return i * 2
    # ถ้ามี 2 คน เลือกลูกตัวที่ค่าน้อยกว่า
    if h[i * 2] < h[i * 2 + 1]:
        return i * 2       # ลูกซ้าย
    else:
        return i * 2 + 1   # ลูกขวา

# 2. ฟังก์ชัน percDown ตามสไลด์ฝั่งซ้าย
def perc_down(h, i, current_size):
    # เช็กไปเรื่อยๆ ตราบใดที่ยังมีลูกอยู่ (i * 2 <= current_size)
    while (i * 2) <= current_size:
        mc = min_child(h, i, current_size)  # mc คือ index ของลูกตัวที่น้อยที่สุด
        
        # เช็กกับลูกว่าแม่มากกว่าลูกไหม ถ้าแม่มากกว่าให้สลับค่า
        if h[i] > h[mc]:
            # สลับค่า (Swap)
            h[i], h[mc] = h[mc], h[i]
            i = mc  # เลื่อนลงไปตรวจตำแหน่งลูกต่อ
        else:
            break

# ตัวอย่างการจำลองการลบ Root (delMin):
# เอาตัวสุดท้ายมาไว้ที่ Root แล้ว pop ตัวท้ายทิ้ง จากนั้นสั่ง percDown ลงไป
min_val = heap[1]
heap[1] = heap[size]
heap.pop()
size = size - 1

# ดันค่าลงจากตำแหน่ง root (index 1)
perc_down(heap, 1, size)

# --- รูปแบบ Output ---
# บรรทัดแรก: ค่าที่ถูกลบออก (5)
# บรรทัดสอง: สภาพ Heap ล่าสุดหลังเลื่อนลงสมบูรณ์ (9 14 11 17 18 19 21 33 27)
print(min_val)
print(" ".join(map(str, heap[1:])))