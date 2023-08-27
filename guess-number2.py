# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入去猜
# 猜對的話 印出 "你猜對了 !"
# 猜錯的話 要告訴使用者 答案是比輸入值來的大 or 小

import random
start_num = input('請輸入起始值: ')
start_num = int(start_num)
end_num = input('請輸入終值: ')
end_num = int(end_num)
r = random.randint(start_num, end_num)
count = 0
while True:
    count = count + 1 #即count = count + 1 快寫法
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('這是你猜的第', count, '次, 恭喜你猜對了 !')
        break
    elif num > r:
        print('這是你猜的第', count, '次, 答案比輸入數值小')
    elif num < r:
        print('這是你猜的第', count, '次, 答案比輸入數值大')