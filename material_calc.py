fangliang_str=input("请输入今日各车方量(方,用英文逗号隔开):")
fangliang_list=fangliang_str.split(",")
cement_per_m3=300.0
total_fangliang=0.0
total_cement=0.0
for f in fangliang_list:
    fangliang=float(f)
    total_fangliang+=fangliang
    total_cement+=fangliang*cement_per_m3
print(f"\n===今日生产物料统计报告===")
print(f"今日总生产方量:{total_fangliang:.2f}方")
print(f"每方水泥用量:{cement_per_m3}公斤")
print(f"今日水泥总用量:{total_cement:.2f}公斤")
print(f"折合水泥用量:{(total_cement/1000):.2f}吨")
