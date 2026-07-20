def double(n):
    if n == 1:
        return 1
    return double(n - 1) * 2

n = int(input())
print(double(n))

# ตัวอย่าง เนื่องจาก n=3 จะได้ double(3) = double(2) =  2*2 = 4 
# ถ้า input n=4 จะได้ double(4) = double(3) * 2 = 4 * 2 = 8