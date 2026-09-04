base, exp, m_len = map(int, input().split())
result= str(base ** exp)

total_len = len(result)
start_idx = (total_len - m_len) // 2
end_idx = start_idx + m_len

middle= result[start_idx:end_idx]

print(result)
print(middle)