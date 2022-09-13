"""需求：
    1.提示用户输入用户姓名，并保存到变量中
    2.提示用户输入用户年龄，保存到变量中，并转成整数
    3.提示用户输入用户身高，保存到变量中，转换成浮点数
    4.在控制台输出用户姓名、年龄、身高对应变量的数据类型
    5.按照以下格式输出用户信息：姓名 xx 年龄 xx 身高 xx
    6.在控制台输出该用户5年之后的年龄格式 张三 5年之后是25"""

name = input("请输入名字：")
age = int(input("请输入年龄"))
height = float(input("请输入身高"))
sum_age = 5
print(f"{name, type(name)}{age, type(age)}{height, type(height)}")
print(name,"5年之后的年龄：",sum_age+age)
