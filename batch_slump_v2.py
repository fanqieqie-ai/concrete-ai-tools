input_str=input("请输入所有车的坍落度（用英文逗号隔开）:")
slump_str_list=input_str.split(",")
pass_count=0
total_cars=len(slump_str_list)
for s in slump_str_list:
    slump=float(s)
    if  slump>=160.0 and slump<=200.0:
        print(f"车号{s}:合格")
        pass_count=pass_count+1
    else:
        print(f"车号{s}:不合格")
rate = (pass_count / total_cars)*100
print(f"\n===今日检测报告===")
print(f"总车数:{total_cars}车")
print(f"合格车数:{pass_count}车")
print(f"合格率:{rate:.1f}%")