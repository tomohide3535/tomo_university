#####1~10文字の文字列を入力してください。

print("1~10文字以上の数字、大文字、小文字のアルファベットを入力してください。")
s = str(input())
####指定の回数繰り返す場合はrangeを使う
for i in range(100):
    
    if len(s) > 0 and len(s) < 11:
        print("入力された文字列：", s)
        break
    else:
        print("1~10文字以上の数字、大文字、小文字のアルファベットを入力してください。")
        s = str(input())
    i += 1
