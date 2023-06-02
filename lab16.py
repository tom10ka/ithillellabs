def month_calendar():
    while True:
        month_list = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December',
        ]
        for month in month_list:
            yield month
            
