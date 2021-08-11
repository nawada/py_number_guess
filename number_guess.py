import random

random_number = random.randrange(5000)
print(random_number)
print("数字を入力 (end と入力すると途中で終了できます)")
correct = False

for i in range(10):
    print("{}回目".format(i + 1))
    print(">>> ", end="")
    in_value = input()

    if in_value == "end":
        # end が入力されたら処理終了
        break

    while not str.isdigit(in_value):
        print("数字を入力してください\r\n>>> ", end="")
        in_value = input()

    num = int(in_value)
    if random_number == num:
        print("正解！")
        correct = True
        break
    elif random_number > num:
        print("もっと大きいです")
    else:
        print("もっと小さいです")

    # 空行だけ出力して整える
    print()

if not correct:
    print("失敗！答えは {} でした！".format(random_number))
