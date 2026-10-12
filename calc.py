cement_per_m3=300.0
fangliang_str=input("请输入今天的生产方量（方）：")
fangliang=float(fangliang_str)
total_cement=fangliang*cement_per_m3
print(f"今天总方量为{fangliang}方,需要水泥:{total_cement}公斤。")