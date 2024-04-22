from datetime import datetime, timedelta, timezone

class TimeConverter:

    def __init__(self):
        self.default_timezone = timezone.utc

    @staticmethod
    def timestamp_to_datetime(timestamp):
        """
        Convert a Unix timestamp to a datetime object.
        """
        return datetime.utcfromtimestamp(timestamp)
    
    @staticmethod
    def datetime_to_timestamp(dt, unix13=False):
        """
        Convert a datetime object to a Unix timestamp.
        """
        return int(dt.timestamp()) * 1000 if unix13 else int(dt.timestamp())
    
    @staticmethod
    def string_to_datetime(date_string, format='%Y-%m-%d %H:%M:%S'):
        """
        Convert a date string to a datetime object.
        """
        return datetime.strptime(date_string, format)
    
    @staticmethod
    def datetime_to_string(dt, format='%Y-%m-%d %H:%M:%S'):
        """
        Convert a datetime object to a formatted date string.
        """
        return dt.strftime(format)
    
    @staticmethod
    def add_days_to_datetime(dt, days):
        """
        Add days to a datetime object.
        """
        return dt + timedelta(days=days)


if __name__ == "__main__":
    converter = TimeConverter()
    current_time = datetime.now()
    a = current_time
    #a = converter.datetime_to_string(current_time)
    print(converter.datetime_to_timestamp(a), type(converter.datetime_to_timestamp(a)))