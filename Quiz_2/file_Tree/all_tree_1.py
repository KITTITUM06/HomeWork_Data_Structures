# ==============================================================================
# รวมแนวข้อสอบ: TREE (เน้น Traversal Order และนิยามพื้นฐาน)
# โครงสร้าง Complete Binary Tree บน List (ช่อง 0 เป็น dummy, Root คือ index 1)[cite: 2]
# ==============================================================================


# ==============================================================================
# ข้อที่ 1: Tree Traversal ครบ 3 รูปแบบ (Preorder, Inorder, Postorder)
# ==============================================================================
# [ตัวอย่าง Input]
# 10 5 15 2 7
#
# [ตัวอย่าง Output ตามโหมด]
# Preorder : 10 5 2 7 15
# Inorder  : 2 5 7 10 15
# Postorder: 2 7 5 15 10
# ==============================================================================
def q1_tree_traversals():
    tree = [0] + list(map(int, input().split()))
    size = len(tree) - 1

    pre_res = []
    in_res = []
    post_res = []

    def traverse(i):
        if i <= size:
            # 1. Preorder (Root -> ซ้าย -> ขวา)
            pre_res.append(str(tree[i]))

            # เดินไปซ้าย
            traverse(i * 2)

            # 2. Inorder (ซ้าย -> Root -> ขวา)
            in_res.append(str(tree[i]))

            # เดินไปขวา
            traverse(i * 2 + 1)

            # 3. Postorder (ซ้าย -> ขวา -> Root)
            post_res.append(str(tree[i]))

    traverse(1)

    # --- เลือก print ตามที่โจทย์สั่ง ---
    # แบบ Preorder:
    print(" ".join(pre_res))

    # แบบ Inorder:
    # print(" ".join(in_res))

    # แบบ Postorder:
    # print(" ".join(post_res))


# ==============================================================================
# ข้อที่ 2: ตรวจสอบว่าเป็น Binary Search Tree (BST) หรือไม่
# ==============================================================================
# [คำอธิบาย]
# ท่องแบบ Inorder ออกมา ถ้าค่าเรียงจากน้อยไปมาก แปลว่าเป็น BST ถูกต้อง[cite: 1]
#
# [ตัวอย่าง Input 1]
# 10 5 15 2 7
# [ตัวอย่าง Output 1]
# True
# ==============================================================================
def q2_is_bst():
    tree = [0] + list(map(int, input().split()))
    size = len(tree) - 1
    in_order = []

    def inorder(i):
        if i <= size:
            inorder(i * 2)
            in_order.append(tree[i])
            inorder(i * 2 + 1)

    inorder(1)

    # เช็กว่าลิสต์ in_order เรียงจากน้อยไปมากหรือไม่
    is_valid = True
    for i in range(len(in_order) - 1):
        if in_order[i] >= in_order[i + 1]:
            is_valid = False
            break

    print(is_valid)


# ==============================================================================
# ข้อที่ 3: หาความสูงของต้นไม้ (Height of Complete Binary Tree)
# ==============================================================================
# [คำอธิบาย]
# รับ Complete Binary Tree มา แล้วตอบความสูง (จำนวนชั้น / Root อยู่ระดับ 0 หรือ 1 ตามโจทย์)
#
# [ตัวอย่าง Input]
# 10 5 15 2 7
# [ตัวอย่าง Output]
# 2
# (มี 3 ระดับ: 10 อยู่ชั้น 0, 5/15 อยู่ชั้น 1, 2/7 อยู่ชั้น 2 -> ความสูงคือ 2)
# ==============================================================================
def q3_tree_height():
    data = list(map(int, input().split()))
    num_nodes = len(data)

    if num_nodes == 0:
        print(0)
        return

    # สำหรับ Complete Tree หาความสูงจากจำนวนโหนดได้ทันที
    import math
    height = int(math.log2(num_nodes))
    print(height)


# ==============================================================================
# จุดสลับเลือกรันใน VS Code
# ==============================================================================
if __name__ == '__main__':
    # q1_tree_traversals()
    # q2_is_bst()
    # q3_tree_height()
    pass