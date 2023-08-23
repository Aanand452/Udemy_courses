import numpy as np
import pandas as pd


def udemy():

    udemy_df = pd.read_csv(
        "/Users/anandkumar/Downloads/data/Udemy Data Analysis.csv")

    print(udemy_df)

    # Beofre Analyzing the data should explore the data

    print(udemy_df.shape)

    print(udemy_df.columns)

    print(udemy_df.dtypes)

    print(udemy_df.count())

    print(udemy_df.value_counts)

    # what are all different subjects for which udemy is offering courses?
    print(udemy_df.head(4))

    print(udemy_df.nunique())

    # which subject has the maximum number of courses

    print(udemy_df.subject.value_counts())

    # Show all the courses which are Free of cost.

    print(udemy_df[udemy_df.is_paid == False])

    # Show all the courses which are paid

    print(udemy_df[udemy_df.is_paid == True])

    # which are the top selling courses

    print(udemy_df.sort_values('num_subscribers', ascending=False))

    # which are the least selling courses

    print(udemy_df.sort_values("num_subscribers"))

    # Show all courses of Graphic Design where the price is below 100 ?
    print(udemy_df[(udemy_df.subject == "Graphic Design")
          & (udemy_df.price > '100')])

    # list all the courese which are related to the python
    print(udemy_df[udemy_df.course_title.str.contains('Python')])

    print(udemy_df[udemy_df['published_timestamp'] == pd.to_datetime(
        udemy_df.published_timestamp)])
    print(udemy_df.dtypes)
    print(udemy_df[udemy_df['year'] ==
          udemy_df['published_timestamp'].dt.year])
    print(udemy_df[udemy_df.year == 2015])

    # What is the Max. Number of Subscribers for Each Level of courses ?
    print(udemy_df.groupby('level').num_subscribers.max())


udemy()
