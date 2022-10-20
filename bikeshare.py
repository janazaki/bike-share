import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Check Input!")
    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month=input('Which month - January, February, March, April, May,  June, or all? ').lower()
        if month in months:
            break
        else:
            print("Check Input!")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all? ').lower()
        if day in days:
            break
        else:
            print("Check Input!")

        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df=df[df['month']==month.title()]
    else:
        df=df
        
    if day!='all':
        df=df[df['day']==day.title()]
    else:
        df=df 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print("The most common month is:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day=df['day'].mode()[0]
    print("The most common day of the week is:", most_common_day)
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', most_common_start_station) 

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', most_common_end_station)
    

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station']+ " to " +df['End Station']
    
    start_to_end = df['Start To End'].mode()[0]
    print("The most frequent combination of start station and end station trip:",start_to_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print('The count of user types is:\n', user_types)

    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts().to_frame()
        print("The types of users by gender are:\n",gender)
    except:
        print("\nThere is no gender data for this city.")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        most_recent_year = df['Birth Year'].max()
        print("\nThe most recent year of birth is:", int(most_recent_year))
        
        earliest_year= df['Birth Year'].min()
        print("\nThe earliest year of birth is:", int(earliest_year))

        most_common_year = df['Birth Year'].mode()[0]
        print("\nThe most common year of birth is:", int(most_common_year))
    except:
        print("\nThere is no birth year data for this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def more_data(df):
    """Displays 5 rows of data with the chosen filters if the option is chosen""" 
    
    
    while True:
        ask = input("Would you like to view 5 rows of data? (yes/no)\n").lower()
        this = 'yes'
        if ask == this:
            print(df.head())
            break 
        elif ask == 'no':
            break
        else:
            print('please answer in yes or no')
                

        
  
                  
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
