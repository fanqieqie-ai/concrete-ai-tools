pass_count=0
total_cars=5
for i in range(total_cars):
    print(f"---正在检测第{i+1}车---")
    slump_str=input("请输入实测坍落度(mm):")
    slump=float(slump_str)
    if  slump>=160.0 and slump <=200.0:
        print("[合格]")
        pass_count=pass_count+1
    else:
        print("[不合格]")
rate=(pass_count/total_cars)*100
print(f"\n===今日检测报告===")
print(f"总车数:{total_cars}车")
print(f"合格车数:{pass_count}车")
print(f"合格率:{rate:.1f}%")