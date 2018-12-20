
# 注释：以 "#" 为开头

print("我们不是HelloWord，main外")

if __name__ == '__main__':  # 运行的主函数，可以不写也可以运行，但是外的先运行，内的后运行，但是为了函数的美观性，最好写
    print("我们不是HelloWord，双引号")  # print在python3中变成了函数，引号内为输出的内容
    print('我们不是HelloWord，单引号')  # print在python3中变成了函数，引号内为输出的内容
