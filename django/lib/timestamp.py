# -*- coding: utf-8 -*-

# author: JaeHyuk Kim <goct8@naver.com>
# version: 0.0.8
# Copyright 2022. goct8(JaeHyuk Kim) All rights reserved.

import re
import time
import datetime as dt
from typing import Union
from decimal import Decimal
from functools import total_ordering


@total_ordering
class Timestamp:
    def __init__(self, timestamp: Union[dt.datetime, time.struct_time, int, float, Decimal, None] = None):
        """
        Initializes the Timestamp object with the current time if no timestamp value is provided.
        The timestamp can be provided in multiple formats - datetime, struct_time, int, float, or None.

        :param timestamp: a datetime object, struct_time object, int, float or None. If None, current time is used.
        :raises ValueError: if the type of timestamp is not datetime, struct_time, int, float or None
        """
        if timestamp is None:
            self.value = time.time()
        elif isinstance(timestamp, (int, Decimal)):
            self.value = float(timestamp)
        elif isinstance(timestamp, float):
            self.value = timestamp
        elif isinstance(timestamp, dt.datetime):
            self.value = timestamp.timestamp()
        elif isinstance(timestamp, time.struct_time):
            self.value = time.mktime(timestamp)
        else:
            raise TypeError("Invalid type for timestamp")

    @property
    def second(self) -> int:
        """
        Returns the current timestamp in seconds.

        :returns: The timestamp in seconds as an integer.
        """
        return int(self.value)

    @property
    def millisecond(self) -> int:
        """
        Returns the current timestamp in milliseconds.

        :returns: The timestamp in milliseconds as an integer.
        """
        return int(self.value * 1000)

    @property
    def microsecond(self) -> int:
        """
        Returns the current timestamp in microseconds.

        :returns: The timestamp in microseconds as an integer.
        """
        return int(self.value * 1000 * 1000)

    @property
    def nanosecond(self) -> int:
        """
        Returns the current timestamp in nanoseconds.

        :returns: The timestamp in nanoseconds as an integer.
        """
        return int(self.value * 1000 * 1000 * 1000)

    @property
    def datetime(self) -> dt.datetime:
        """
        Converts the current timestamp into a datetime object in UTC.

        :returns: The datetime representation of the timestamp in UTC.
        """
        return dt.datetime.fromtimestamp(self.value, tz=dt.timezone.utc)

    @property
    def struct_time(self) -> time.struct_time:
        """
        Converts the current timestamp into a struct_time object in UTC.

        :returns: The struct_time representation of the timestamp in UTC.
        """
        return time.gmtime(self.value)

    def __str__(self) -> str:
        """
        Returns string representation of the timestamp.

        :returns: timestamp as string
        """
        return str(self.value)

    def __int__(self) -> int:
        """
        Returns integer part of the timestamp.

        :returns: integer part of timestamp
        """
        return int(self.value)

    def __float__(self) -> float:
        """
        Returns the timestamp as a float.

        :returns: timestamp as float
        """
        return self.value

    def __add__(self, other):
        """
        Adds the given value to the current timestamp. If the other value is a Timestamp object,
        the seconds from both timestamps will be added, and a new Timestamp object will be returned.
        If the other value is a numeric type (including Decimal), it will be added to the current
        timestamp's seconds, and the result will be returned as a number.

        :param other: another Timestamp object or a number
        :returns: new Timestamp object if other is a Timestamp,
            otherwise a numeric value representing the sum of the two values
        """
        if isinstance(other, Timestamp):
            return Timestamp(self.value + other.value)
        elif isinstance(other, Decimal):
            return Timestamp(self.value + float(other))

        return Timestamp(self.value + other)

    def __radd__(self, other):
        """
        Adds the given value to the current timestamp. If the other value is a Timestamp object,
        the seconds from both timestamps will be added, and a new Timestamp object will be returned.
        If the other value is a numeric type (including Decimal), it will be added to the current
        timestamp's seconds, and the result will be returned as a number.

        :param other: another Timestamp object or a number
        :returns: new Timestamp object if other is a Timestamp,
            otherwise a numeric value representing the sum of the two values
        """
        if isinstance(other, Timestamp):
            return Timestamp(other.value + self.value)
        elif isinstance(other, Decimal):
            return Timestamp(float(other) + self.value)

        return Timestamp(other + self.value)

    def __sub__(self, other):
        """
        Subtracts the given value from the current timestamp. If the other value is a Timestamp object,
        the seconds from both timestamps will be subtracted, and a new Timestamp object will be returned.
        If the other value is a numeric type (including Decimal), it will be subtracted from the current
        timestamp's seconds, and the result will be returned as a number.

        :param other: another Timestamp object or a number
        :returns: new Timestamp object if other is a Timestamp,
            otherwise a numeric value representing the difference of the two values
        """
        if isinstance(other, Timestamp):
            return Timestamp(self.value - other.value)
        elif isinstance(other, Decimal):
            return Timestamp(self.value - float(other))

        return Timestamp(self.value - other)

    def __rsub__(self, other):
        """
        Subtracts the given value from the current timestamp. If the other value is a Timestamp object,
        the seconds from both timestamps will be subtracted, and a new Timestamp object will be returned.
        If the other value is a numeric type (including Decimal), it will be subtracted from the current
        timestamp's seconds, and the result will be returned as a number.

        :param other: another Timestamp object or a number
        :returns: new Timestamp object if other is a Timestamp,
            otherwise a numeric value representing the difference of the two values
        """
        if isinstance(other, Timestamp):
            return Timestamp(other.value - self.value)
        elif isinstance(other, Decimal):
            return Timestamp(float(other) - self.value)

        return Timestamp(other - self.value)

    def __mul__(self, other):
        """
        Multiplies the current timestamp by the given value. If the other value is a Timestamp object,
        the seconds from both timestamps will be multiplied, and a new Timestamp object will be returned.
        If the other value is a numeric type (including Decimal), it will be multiplied by the current
        timestamp's seconds, and the result will be returned as a number.

        :param other: another Timestamp object or a number
        :returns: new Timestamp object if other is a Timestamp,
            otherwise a numeric value representing the product of the two values
        """
        if isinstance(other, Timestamp):
            return Timestamp(self.value * other.value)
        elif isinstance(other, Decimal):
            return Timestamp(self.value * float(other))

        return Timestamp(self.value * other)

    def __rmul__(self, other):
        """
        Multiplies the current timestamp by the given value. If the other value is a Timestamp object,
        the seconds from both timestamps will be multiplied, and a new Timestamp object will be returned.
        If the other value is a numeric type (including Decimal), it will be multiplied by the current
        timestamp's seconds, and the result will be returned as a number.

        :param other: another Timestamp object or a number
        :returns: new Timestamp object if other is a Timestamp,
            otherwise a numeric value representing the product of the two values
        """
        if isinstance(other, Timestamp):
            return Timestamp(other.value * self.value)
        elif isinstance(other, Decimal):
            return Timestamp(float(other) * self.value)

        return Timestamp(other * self.value)

    def __truediv__(self, other):
        """
        Divides the current timestamp by the given value. If the other value is a Timestamp object,
        the seconds from both timestamps will be divided, and a new Timestamp object will be returned.
        If the other value is a numeric type (including Decimal), it will be used to divide the current
        timestamp's seconds, and the result will be returned as a number.

        :param other: another Timestamp object or a number
        :returns: new Timestamp object if other is a Timestamp,
            otherwise a numeric value representing the quotient of the two values
        """
        if isinstance(other, Timestamp):
            return Timestamp(self.value / other.value)
        elif isinstance(other, Decimal):
            return Timestamp(self.value / float(other))

        return Timestamp(self.value / other)

    def __rtruediv__(self, other):
        """
        Divides the current timestamp by the given value. If the other value is a Timestamp object,
        the seconds from both timestamps will be divided, and a new Timestamp object will be returned.
        If the other value is a numeric type (including Decimal), it will be used to divide the current
        timestamp's seconds, and the result will be returned as a number.

        :param other: another Timestamp object or a number
        :returns: new Timestamp object if other is a Timestamp,
            otherwise a numeric value representing the quotient of the two values
        """
        if isinstance(other, Timestamp):
            return Timestamp(other.value / self.value)
        elif isinstance(other, Decimal):
            return Timestamp(float(other) / self.value)

        return Timestamp(other / self.value)

    def __abs__(self):
        """
        Returns the absolute value of the timestamp's seconds.

        :returns: new Timestamp object representing the absolute value of the timestamp
        """
        return Timestamp(abs(self.value))

    def __round__(self, ndigits=None):
        """
        Rounds the seconds in the timestamp to the specified number of digits, and returns a new Timestamp object
        with the rounded value.

        :param ndigits: the number of digits to round to. If None, the value is rounded to the nearest integer.
        :returns: a new Timestamp object with the rounded seconds value
        """
        return Timestamp(round(self.value, ndigits=ndigits))

    def __eq__(self, other):
        if isinstance(other, Timestamp):
            return self.value == other.value
        elif isinstance(other, Decimal):
            return self.value == float(other)

        return self.value == other

    def __lt__(self, other):
        if isinstance(other, Timestamp):
            return self.value < other.value
        if isinstance(other, Decimal):
            return self.value < float(other)

        return self.value < other

    @staticmethod
    def _get_decimal_digit(number: float, digit: int = 6) -> str:
        """
        Helper function to get the decimal digits from a number.

        :param number: the number to get the digits from
        :param digit: the number of digits to return. Default is 6.
        :returns: decimal digits of number as zero-padded string
        """
        return f"{int((number - int(number)) * (10 ** digit))}".zfill(digit)

    def convert_to_string(self, formatter: str = "%Y-%m-%d %H:%M:%S.%3f %Z", timezone: int = 0) -> str:
        """
        Converts the timestamp to a formatted string using the given format string.
        You can control the number of decimal places by using %f in the format string.
        If you want to specify the number of decimal places, you can use %nf where n is the number of decimal places.
        For example, %3f will give you 3 decimal places.
        If you just use %f without specifying the number, it will default to 6 decimal places.

        :param formatter: the format string to use for formatting. Default is "%Y-%m-%d %H:%M:%S.%3f %Z"
        :param timezone: the timezone offset in hours.
            If set to 0, UTC time will be used.
            If the value is the same as the local timezone offset (e.g., 9 for KST), local time will be used.
            Any other values will be treated as an offset from UTC (e.g., 3 for "+03:00", -4 for "-04:00").
            Default is 0.
        :returns: the formatted timestamp string
        """
        pattern = re.compile(r"%[0-9]*f")
        matched_patterns = set(re.findall(pattern=pattern, string=formatter))

        cache = {}
        for matched_pattern in matched_patterns:
            if matched_pattern[1:-1] == "":
                formatter = formatter.replace(matched_pattern, self._get_decimal_digit(number=self.value))
            else:
                digit = int(matched_pattern[1:-1])
                if not cache.get(digit):
                    cache[digit] = self._get_decimal_digit(number=self.value, digit=digit)
                formatter = formatter.replace(matched_pattern, cache[digit])

        if timezone == 0:
            return time.strftime(formatter, time.gmtime(self.value))
        if timezone == time.altzone*-1 / 3600:
            return time.strftime(formatter, time.localtime(self.value))
        tz = dt.timezone(dt.timedelta(hours=timezone))
        if "%Z" in formatter:
            _timezone = (dt.datetime.fromtimestamp(self.value, tz=tz).strftime("%Z").replace("UTC", ""))
            formatter = formatter.replace("%Z", _timezone)
        return dt.datetime.fromtimestamp(self.value, tz=tz).strftime(formatter)

    def get_datetime_with_timezone(self, timezone: int) -> dt.datetime:
        """
        Returns a datetime object representing the current timestamp, adjusted to the given timezone.

        :param timezone: The timezone shift in hours. Positive values will shift the time forward,
            negative values will shift it backward.
        :returns: A datetime object representing the current timestamp, adjusted to the given timezone.
        """
        return dt.datetime.fromtimestamp(self.value, tz=dt.timezone(dt.timedelta(hours=timezone)))
