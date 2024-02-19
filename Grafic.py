import random
import pandas as pd

# Генерация DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot вид
one_hot_encoded = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Удаление исходного столбца 'whoAmI'
data = data.drop('whoAmI', axis=1)

# Объединение с one-hot DataFrame
data_one_hot = pd.concat([data, one_hot_encoded], axis=1)

# Вывод результатов
print(data_one_hot.head())
