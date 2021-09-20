import pandas as pd
import time
import numpy as np
import json
CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv',
                'washington': 'washington.csv'}
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
weekdays = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

class text():
    def spin(self, string, num):
        self.clear = "\b"*(8 + len(string))
        for _ in range(num):
            for ch in '-\\|/':
                print('__' + '(' + ch + ')' + string + '(' + ch +
                      ')' + '_', end='', flush=True)
                time.sleep(0.1)
                print(self.clear, end='', flush=True)


def print_spin(message, num):
    fido = text()
    fido.spin(message, num)

def obtain_filters():
    """ Ask the user to specify the city, month and day of which
    they seek statistics about
    Returns:
    (str) city - input name of the city to analyze
    (str) month - input name of month to filter by or with no filter with option
                    "all"
    (str) day - input name of the day of the week to filter by or with no filter
                with option "all" """

    print('\n')
    print_spin('USbikeshare', 8)
    print('_(/)USbikeshare(/)______________________________')
    print()
    print('Hello! we\'re glad you are here to explore USbikeshare data Python prompt\nLet\'s explore the data to gain some insight' )

    # obtain the city_filter input#
    print()
    city = input('Please enter the name of city you want to analyze(Chicago, New york city, Washington): ').lower()
    city = city.casefold()
    while city not in CITY_DATA:
        city = input('Sorry! name of city not found. Please try again!: ').lower()
        city = city.casefold()
    print()
    # obtain the month filter input#
    month = input('Please enter  the month for your analysis from January to June or "all" to apply no filter: ').lower()
    month = month.casefold()
    while month not in months:
        month = input('Sorry! name of month not found. Please try again!: ').lower()
        month = month.casefold()

    # obtain the day_filter input#
    print()
    day = input('What day of week would you like to see  or enter "all" to apply no filter: ' )
    day = day.casefold()
    while day not in weekdays:
        day = input('Sorry! name of day not found. Please try again!: ')
        day = day.casefold()

    # selction confirmation#
    while True:
        print()
        filters = input('\nAre you sure you want to apply the following filters?'
                    '\nCity(ies): {}\nMonth(s): {}\nWeekdays(s): {}\n\n [yes]\n[no]\n'.format(city, month, day))
        if filters == 'yes':
            break
        else:
            city = input('Please enter the name of city you want to analyze(Chicago, New york city, Washington): ').lower()
            city = city.casefold()
            while city not in CITY_DATA:
                city = input('Sorry! name of city not found. Please try again!: ').lower()
                city = city.casefold()
            print()
            # obtain the month filter input#
            month = input('Please enter  the month for your analysis from January to June or "all" to apply no filter: ').lower()
            month = month.casefold()
            while month not in months:
                month = input('Sorry! name of month not found. Please try again!: ').lower()
                month = month.casefold()

            # obtain the day_filter input#
            print()
            day = input('Please enter the day for your analysis from monday to sunday or "all" to apply no filter: ' )
            day = day.casefold()
            while day not in weekdays:
                day = input('Sorry! name of day not found. Please try again!: ')
                day = day.casefold()

    print('='*50)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    print()
    print('\nPlease wait the program is loading the data...')
    start_time = time.time()

    # Load data file into a dataframe#
    df = pd.read_csv(CITY_DATA[city])

    #convert the start time column to datetime#
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from start time to create new columns#
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #filtering by month if applicable

    if month != 'all':
        # use the index of month list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day of week if applicable

    if day != 'all':
    #filter by day of the week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """ Displays statistics on the most frequent times of travel."""
    if 'Start Time' in df.columns:
        print()
        print('Calculating the most frequent times of travel...'.center(50, '-'))
        start_time = time.time()
        print('Time Statistics'.center(50, '-'))
        #convert the start time to column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # TO DO: display the most common month
        # Extracting month from the Start Time column to create a month column
        df['month'] = df['Start Time'].dt.month
        # Finding the most common month of the year
        popular_month = df['month'].mode()[0]
        print('Most common month: ', popular_month)

        # TO DO: display the most common day of week
        # Extracting dayofweek from the Start Time column to create a day_of_week column
        df['day_of_week'] = df['Start Time'].dt.day_name()
        # finding the most common day of week
        popular_day = df['day_of_week'].mode()[0]
        print('Most common Day of the Week: ', popular_day)

        # TO DO: display the most common start hour
        # Extracting hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour
        # finding the most common hour of the day
        popular_hour = df['hour'].mode()[0]
        print('Most common Hour of the Day: ', popular_hour)

        print('\nThis took %s seconds.' % (time.time() - start_time))
        print('='*50)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print()
    print(' Calculating The Most Popular Stations and Trip '.center(50, '='))
    start_time = time.time()
    print(' Station Stats '.center(50, '-'))

    # TO DO: display most commonly used start station
    if 'Start Station' in df.columns:
        print('Most popular Station: ', df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    if 'End Station' in df.columns:
        print('Most popular End Station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        # -------------------START--------------------------
        df['frequent_path'] ="{} to {}".format(df['Start Station'], df['End Station'])
        print('Most frequent path is from: ', df['frequent_path'].mode()[0])

        print('\nThis took %s seconds.' % (time.time() - start_time))
        print('='*50)
def Trip_Duration_statistics(df):
    """Displays statistics on the total and average trip duration."""
    print()
    print('Calculating Trip Duration...'.center(50))
    print('Trip_Duration_statistics'.center(50, '-'))
    start_time = time.time()
    # TO DO: to display total travel time
    if 'Trip Duration' in df.columns:
        print('Total Trip Duration: ', df['Trip Duration'].sum())
    # TO DO: to display the average trip duration
    if 'Trip Duration' in df.columns:
        print('Average Trip Duration: ', df['Trip Duration'].mean())

        print('\nThis took %s seconds.' % (time.time() - start_time))
        print('='*50)
def user_stats(df):
    """ Displays statistics on bikeshare users."""
    print()
    print('Calculating user Statistics'.center(50, '=') )
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender,'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)

def main():
    while True:
        city, month, day = obtain_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        Trip_Duration_statistics(df)
        user_stats(df)

        #To prompt the user whether they would like to see the raw data
        choose = ['yes','no']
        user_input = input('Would you like to see more data? (Enter:Yes/No).\n').lower()

        while user_input.lower() not in choose:
            user_input = input('Please Enter Yes or No:\n').lower()
            user_input = user_input.lower()
        n = 0
        while True :
            if user_input.lower() == 'yes':

                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see more data? (Type:Yes/No).\n')
                while user_input.lower() not in choose:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break



        restart = input('\nWould you like to restart? (Enter:Yes/No).\n')
        #check wheather the user is entering the valid entry or not
        while restart.lower() not in choose:
            restart = input('Please Enter Yes or No:\n')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('Program terminated!'.center(78, '-'))
            break
        else:
            continue

if __name__ == '__main__':
    main()
