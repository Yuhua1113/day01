# 从键盘输入姓名，年龄，身高
name = input("请输入姓名:")

age = input("请输入年龄:")

height = input("请输入身高:")
# 输出格式是： 我的姓名是xx，年龄是xx，身高是xx
print("我的姓名是{name}，年龄是{}，身高是{}".format(name, age, height))

#F-str 格式
print(f"我的姓名是{name}，年龄是{age}，身高是{height}")