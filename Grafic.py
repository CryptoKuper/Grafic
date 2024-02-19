import random
import pandas as pd

# Генерация DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание one-hot представления без использования get_dummies
one_hot_encoded = pd.DataFrame(0, columns=unique_values, index=data.index)

# Установка 1 в соответствующих позициях
for index, value in enumerate(data['whoAmI']):
    one_hot_encoded.at[index, value] = 1

# Объединение с исходным DataFrame
data_one_hot = pd.concat([data, one_hot_encoded], axis=1)

# Удаление исходного столбца 'whoAmI'
data_one_hot = data_one_hot.drop('whoAmI', axis=1)

# Вывод результатов
print(data_one_hot.head())
