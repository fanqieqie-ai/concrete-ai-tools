slump_str=input("请输入实测坍落度(mm):")
slump=float(slump_str)
min_slump=160.0
max_slump=200.0
if  slump>=min_slump and slump <=max_slump:
    print(f"实测坍落度{slump}mm,[合格],可以出厂。")
else:
    print(f"实测坍落度{slump}mm,[不合格],请调整！")