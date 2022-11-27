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

    cities = ['chicago', 'new york city', 'washington']

    city = input('\n Enter city. \nChoose either chicago, new york city, or washington: ').lower()
    print(city)
    while city not in cities:
        print('\nPlease choose a valid city, either: chicago, new york city, or washington.').lower()
        break
    else:
        print("\nWe are working with {} data".format(city.title()))
        
        
        # TO DO: get user input for month (all, january, february, ... , june)

    months = ['all', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'October', 'November', 'December']

    month = input('\nPlease select the month for which you wish to see data. Alternatively you can select all: ').lower()
    print(month)
    while month not in months:
        break
    else:
        print('\nPlease choose a valid month: ').lower()
            

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['all', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    day = input('\nPlease select the day for which you wish to see the data. Alternatively you can select all: ').lower()
    print(day)
    while day not in days:
        break
    else:
        print('\nPlease choose a valid day: ').lower()
            

    print('Awesome! we will be looking at data in {} for the month of {} on {}'.format(city, month, day))

    print('-'*40)

    return (city, month, day)
    city, month, day = get_filters()
    df = load_data(city, month, day)
    print (df)


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
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day) + 1
        
        df = df[df['day'] == day]
        
    return df



    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

        # TO DO: display the most common month
    commn_month = df['month'].mode()[0]
    print('Most popular month: ', commn_month)

        # TO DO: display the most common day of week
    commn_day = df['day'].mode()[0]
    print('Most popular day: ', commn_day)
        # TO DO: display the most common start hour
    commn_hour = df['hour'].mode()[0]
    print('Most popular hour: ', commn_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

        # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most popular Start Station: ',common_start_station)

        # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most popular End Station: ',common_end_station)

        # TO DO: display most frequent combination of start station and end station trip
    df['station_combination'] = df ['Start Station'] + ' '+ '->' + ' ' + df['End Station']
    common_combo = df['station_combination'].mode()[0]

    print('Most popular Combo Station: ', common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

        # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

        # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])

        # TO DO: Display counts of user types
    user_types =  df['User Type'].value_counts()
    print('Counts of user types: \n', user_types)

        # TO DO: Display counts of gender
    if city == 'washington':
        print('Gender data is not available for the city of washington')   
    else:
        gender_count = df['Gender'].value_counts()
        print('Counts of genders: \n', gender_count) 

        # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('Birth year data is not available for the city of washington')
    else:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year of Birth: ', int(earliest_year))

        latest_year = df['Birth Year'].max()
        print('Latest Year of Birth: ', int(latest_year))

        popular_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Birth: ', int(popular_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """ Raw data Prompt """
    raw_data = input('Would you like to see 5 lines of raw data? Yes or no: ').lower()
    
    start = 0
    
    while True:
        if raw_data != 'no':
            print(df.iloc[start:start +5])
            start += 5
            
            end_display = input('Would you like to continue? Yes or no: ').lower()
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
