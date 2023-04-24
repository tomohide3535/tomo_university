print("入力する整数の数を入力してください。")
n = int(input())
list = []

for i in range(n):
    print("整数を入力してください。")
    i = int(input())
    list.append(i)

print("最大値：", max(list))