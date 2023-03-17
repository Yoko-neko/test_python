age = int(input('電車に乗る方の年齢を入力してください。(数字でお願いします):' ))

def train_fare(age):
    if age >= 12:
        return 10000
    elif age >= 6:
        return 5000
    else:
        return 0
result = train_fare(age)
print('運賃は{}円ですよ^_^'.format(result))
