# write a prograam to show data in pai chart using matplotlib

import pandas as pd
import matplotlib.pyplot as plt

employee = {
    'name': ['brijesh', 'het', 'krish'],
    'course_name': ['DA', 'Data_science', 'DA'],
    'age': [25, 24, 24]
}
df = pd.DataFrame(employee)
employee_name = df['name']
employee_age=df['age']

plt.figure(figsize=(10,10))
plt.pie(employee_age, labels=employee_name, autopct='%1.1f%%')
plt.title('Employee Age Distribution')
plt.show()
