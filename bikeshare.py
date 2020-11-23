import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list = ['chicago', 'new york', 'washington']
month_list = ['january', 'february', 'march', 'april', 'may', 'june','all']
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all']
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
    city = 0
    city_list = ['chicago', 'new york', 'washington']
    while city not in city_list:
        city = str(input('Choose the city you would like to see data from (chicago, new york, washington): ')).lower()           
    # TO DO: get user input for month (all, january, february, ... , june)
    month = 0
    while month not in month_list:
        month = str(input('Would you like to filter data by month (january, february, march, april, may, june) if not type all: '))         
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 0    
    while day not in day_list:
        day = str(input('Would you like to filter data by day? if not type all: '))   
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
    if month != 'all':
        month = month_list.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = month_list[df['month'].mode()[0]-1]
    print('Most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common month is: ', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour is: ' , common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station is: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common End Station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_station_comb = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most Popular trip is:    from {}     to {}.'.format(common_station_comb[0],common_station_comb[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time = ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time = ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        types_count = df['User Type'].value_counts()
        print('Users count by types is:\n', types_count)
    except:
        print('No User Type Data To Show!')
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Users count by gender is:\n', gender_count)
    except:
        print('No User Gender Data To Show!')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        most_com_year = int(df['Birth Year'].value_counts().idxmax())
        print('Most common birth year is: ', most_com_year)
        earliest_year = int(df['Birth Year'].min())
        print('Earliest birth year is: ', earliest_year)
        most_recent_year = int(df['Birth Year'].max())
        print('Most recent birth year is: ', most_recent_year)
    except:
        print('No User Birth Year Data To Show!')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def more_data(df):
    q = str(input('Do you want to see first 5 lines of raw data? yes/no ')).lower
    s, e = 0, 5
    while q != 'no':
        more_data = df.iloc[s:e]
        print(more_data)
        s += 5
        e += 5
        q = str(input('Would you like to see more data? yes/no ')).lower()

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
