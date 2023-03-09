# # 0-1-1
#
# weight = int(input("体重を記入してください(kg): "))
# height = int(input("身長を入力してください(cm): "))
# height = height/100
# bmi = weight /(height**2)
# print("あなたのBMIは{}".format(bmi))

# 0-2-2
# r = []
# jap = int(input("国語の点数を入力してください："))
# r.append(jap)
# math = int(input("数学の点数を入力してください："))
# r.append(math)
# eng = int(input("英語の点数を入力してください："))
# r.append(eng)
# print(r)
# sum_r = sum(r,2)
# print(sum_r)

# 0-3-1
# num = int(input('数値を入力してください：'))
# if num/2 == 0:
#     print('入力された数は偶数です')
# else:
#     print('入力された数は奇数です')
#
# greeting = int(input('数字を一つ選んでください'
#                  '１、こんにちは　'
#                  '２、景気は？　'
#                  '３、さようなら'))
# if greeting == 1:
#     print('ようこそ！')
# elif greeting == 2:
#     print('ぼちぼちです')
# elif greeting == 3:
#     print('お元気で！')
# else :
#     print('どうしました？')

# 0−4−１
# import time
#
# counts = [10,9,8,7,6,5,4,3,2,1,'Life off!']
# for count in counts:
#     print(count)
#     time.sleep(1)

# 模範解答  これでカウントダウンになってるんでしょうか。
# for i in range(10):
#     print('{},'.format(10-i),end = '')
# print('Life Off!')

# 0-4-2
# import statistics
# scores = []
# for x in range(10):
#     score = int(input('{}人目の試験の結果：'.format(x+1)))
#     scores.append(score)
#
# final_scores = []
# for score in scores:
#     final_score = score * 0.8 + 20
#     final_scores.append(final_score)
# print(final_scores)
#
# average = statistics.mean(final_scores)
# print(average)

# 0-5-1
# num = int(input('閏年可動化を判別する年を入力してください：'))
# if num % 400 == 0:
#     print('その年は閏年ですよ。')
# elif num % 100 == 0:
#     print('It is very difficult to say, but that year is not a leap year.')
# elif num % 4 == 0:
#     print('普通の閏年です')
# else:
#     print("It's not a leap year, it's just a normal year.")

#  model answer
# I had to create a function,
# but I didn't follow the instruction at all.

# def uruu(year):
#     result = None
#     if year % 400 == 0:
#         result = True
#     elif year % 100 == 0:
#         result = False
#     elif year % 4 == 0:
#         result =True
#     else:
#         result =False
#     return result
