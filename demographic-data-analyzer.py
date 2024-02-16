import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  selecao_male = (df['sex'] == 'Male')

  average_age_men = round(df[selecao_male]['age'].mean(), 1)

  # What is the percentage of people who have a Bachelor's degree?
  selecao_education = (df['education'] == 'Bachelors')

  percentage_bachelors = round((len(df[selecao_education]) / len(df)) * 100, 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  selecaoH = (df['education'] == 'Bachelors') | (
      df['education'] == 'Masters') | (df['education'] == 'Doctorate')
  selecaoL = (df['education'] != 'Bachelors') & (
      df['education'] != 'Masters') & (df['education'] != 'Doctorate')
  selecao50 = (df['salary'] == '>50K')
  # percentage with salary >50K

  higher_education = len(df['education'][selecaoH & selecao50])
  lower_education = len(df['education'][selecaoL & selecao50])

  # percentage with salary >50K
  higher_education_rich = round((higher_education / len(df[selecaoH])) * 100,
                                1)
  lower_education_rich = round((lower_education / len(df[selecaoL])) * 100, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  selecao_rich = (df['hours-per-week'] == 1) & (df['salary'] == '>50K')

  num_min_workers = len(df[df['hours-per-week'] == 1])

  rich_percentage = round((len(df[selecao_rich]) / num_min_workers) * 100, 1)
  # What country has the highest percentage of people that earn >50K?
  total_pais=df.groupby('native-country')[['native-country']].value_counts()
  mais_de_50K=df[df['salary']=='>50K'].groupby('native-country')['salary'].value_counts()  
  result_country= (mais_de_50K/total_pais).idxmax()
  result_percentage=((mais_de_50K/total_pais).max().round(3))*100
  
  
  highest_earning_country =result_country[0]
  highest_earning_country_percentage =result_percentage

  # Identify the most popular occupation for those who earn >50K in India.
  selecao=(df['native-country']== 'India') & (df['salary']=='>50K')
  result_india=df[selecao].groupby('occupation')['occupation'].value_counts().idxmax()
  top_IN_occupation = result_india

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }

calculate_demographic_data()