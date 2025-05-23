
🔹 1. Create a DataFrame

import pandas as pd
Data = {
    'Name':['Ali', 'Sara', 'Raza', 'Aysha'],
    'Age':[22, 25, 28, 21],
    'City':['Lahore', 'Karachi', 'Islamabad', 'Multan'],
    'Education':['BS', 'MS', 'BS', 'PhD']
}
df = pd.DataFrame(Data)
print(df)

🔹 2. Print only the "Name" and "City" columns.

print(df[['Name', 'City']])

🔹 3. Add a new column called "GPA" with these values:
[3.1, 3.8, 3.5, 3.2]


df['GPA']= [3.1, 3.8, 3.5, 3.2]

🔹 4. Filter and print students who have a GPA > 3.3

df[df['GPA'] > 3.3]

🔹 5. Print only the 2nd row using .iloc[]

print(df.iloc[1])

🔹 6. Delete the "Education" column

df.drop('Education', axis=1)

🔹 7. Save the DataFrame to a CSV file named "students.csv


df.to_csv("student.csv", index=False)

To download it to your computer, run this extra line after saving:

from google.colab import files
files.download('student.csv')
