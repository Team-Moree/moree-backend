# -*- coding: utf-8 -*-

# author: JaeHyuk Kim <goct8@naver.com>
# version: 0.0.5
# Copyright 2022. goct8(JaeHyuk Kim) All rights reserved.

import os
import re
import sys
import time
import string
import random
import logging
import datetime
import subprocess

from xml.dom import minidom
from xml.etree import ElementTree

from typing import Generator, Callable, Optional, Union, List, Tuple, Dict


def parse_args(args: Union[List[str], None] = None) -> Dict[str, Union[str, bool]]:
    """
    Parse command-line arguments and return them as a dictionary.

    :param args: A list of arguments. If not provided, sys.argv will be used.
    :return: A dictionary where each key is the argument (without leading '--' or '-') and the value is
             the argument's value if it's provided, or True if it's a flag.
    """
    # Skip the first argument which is the script name
    if args is None:
        args = sys.argv[1:]

    context = {}
    for arg in args:
        key, eq, value = arg.lstrip('-').partition('=')

        if eq:
            context[key] = value
        else:
            context[key] = True

    return context


def get_base_url(url: str) -> Optional[str]:
    """
    Extract the base URL from the given URL.

    :param url: The full URL.
    :return: The base URL if the given URL is valid, None otherwise.
    """
    match = re.match(r'(https?://[a-zA-Z0-9.-]+(?::\d+)?)(?:/|$)', url)
    return match.group(1) if match else None


def get_child_abs_paths(dir_path: str) -> Generator[str, None, None]:
    """
    Generate absolute paths of all files in the given directory path and its subdirectories.

    :param dir_path: The directory path.
    :return: A generator yielding absolute paths of all files.
    """
    logging.info(f"GET - child_abs_paths({dir_path})")
    dir_abs_path = os.path.abspath(dir_path)

    for child_name in os.listdir(dir_abs_path):
        child_abs_path = os.path.join(dir_abs_path, child_name)

        if os.path.isdir(child_abs_path):
            yield from get_child_abs_paths(child_abs_path)
        else:
            yield child_abs_path


def get_pretty_xml(xml: ElementTree.Element, indent: Union[str, int] = 4) -> str:
    """
    Returns a pretty-printed XML string for the ElementTree.Element.

    :param xml: ElementTree.Element instance to pretty-print.
    :param indent: Indentation as a string or integer (number of spaces for indentation). Default is 4 spaces.
    :return: Pretty-printed XML string.
    """
    # Convert indent to spaces if it is an integer
    indent = " " * indent if isinstance(indent, int) else indent

    # Convert ElementTree.Element to string and parse it with minidom
    xml_str = ElementTree.tostring(xml, method='xml').decode()
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent=indent)

    # Strip each line and join them together
    pretty_lines = (line for line in pretty_xml.split('\n')[1:] if line.strip())

    return "\n".join(pretty_lines)


def epoch_to_str_time(epoch: int, timezone: int = 9) -> str:
    timezone_format = f"{format(abs(timezone), '02')}:00"
    if timezone >= 0:
        timezone_format = f"+{timezone_format}"
    else:
        timezone_format = f"-{timezone_format}"
    return f'{time.strftime(f"%Y-%m-%dT%H:%M:%S{timezone_format}", time.gmtime(epoch + (3600 * timezone)))}'


str_time_to_epoch: Callable[[str], int] = lambda str_time: int(
    datetime.datetime.strptime(str_time, '%Y-%m-%dT%H:%M:%S%z').timestamp()
)


def run_command(command: str, text: bool = True) -> Tuple[int, str]:
    logging.info(f"RUN - ({command})")
    result = ""
    response = subprocess.run(command, capture_output=True, shell=True, text=text)
    if response.stdout:
        result += f"stdout :\n{response.stdout}"
    if response.stderr:
        result += f"stderr :\n{response.stderr}"
    logging.info(f"RUN - ({command}) was finished\nstatus_code = {response.returncode}\n{result}")
    response.check_returncode()
    return response.returncode, response.stdout if response.returncode == 0 else response.stderr


def check_dict_key_recursive(form: dict, context: dict, _result: Union[list, None] = None) -> Tuple[bool, str]:
    if _result is None:
        _result = []
    context_keys = context.keys()
    for form_key in form.keys():
        if form_key not in context_keys:
            _result.append(form_key)
        else:
            if isinstance(form[form_key], dict) and isinstance(context[form_key], dict):
                check_dict_key_recursive(form[form_key], context[form_key], _result)
    if _result:
        return False, f"key({', '.join(_result)}) does not exist."
    else:
        return True, f"context has all key."


def is_valid_email(email: str) -> bool:
    """
    Regular expression pattern for email.
    :param email: The email string to check.
    :rtype: bool
    """
    email_pattern = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    return bool(email_pattern.fullmatch(email))


def is_valid_password(password: str, min_length: int = 8, max_length: int = 64, number: bool = True, lower: bool = True,
                      upper: bool = True, special: bool = True) -> bool:
    """
    Regular expression pattern for a password.
    :param password: The password string to check.
    :param min_length: The minimum length for the password. Default is 8.
    :param max_length: The maximum length for the password. Default is 64.
    :param number: If True, password must include a numeric character Default is True.
    :param lower: If True, password must include a lowercase letter Default is True.
    :param upper: If True, password must include an uppercase letter Default is True.
    :param special: If True, password must include a special character (!@#$%^&*). Default is True.
    :rtype: bool
    """
    if min_length > max_length:
        raise ValueError("min_length should not be greater than max_length")

    # Start building the regex pattern
    password_pattern = "^"

    # Min and Max length
    password_pattern += f"(?=^.{{{min_length},{max_length}}}$)"

    if number:
        # At least one numeric character
        password_pattern += "(?=.*[0-9])"

    if lower:
        # At least one lowercase letter
        password_pattern += "(?=.*[a-z])"

    if upper:
        # At least one uppercase letter
        password_pattern += "(?=.*[A-Z])"

    if special:
        # At least one special character
        password_pattern += "(?=.*[!@#$%^&*])"

    # End of the regex pattern
    password_pattern += ".*$"

    # Compile the regex pattern
    password_pattern_compiled = re.compile(password_pattern)

    return bool(password_pattern_compiled.fullmatch(password))


def is_valid_phone_number(phone_number: str) -> bool:
    """
    Regular expression pattern for a Korean phone number.

    '01\\d-\\d{4}-\\d{4}': Checks for cell phone numbers (e.g., 010-XXXX-XXXX or 010XXXXXXXX)

    '02-\\d{3,4}-\\d{4}': Checks for Seoul numbers (e.g., 02-XXX-XXXX, 02-XXXX-XXXX or 02XXXXXXXX)

    '0[3-9][1-5]-\\d{3,4}-\\d{4}': Checks for other area numbers (e.g., 0XX-XXX-XXXX or 0XX-XXXX-XXXX)
    :param phone_number: The phone_number string to check.
    :rtype: bool
    """
    phone_number_pattern = re.compile(
        r"^(01\d-?\d{4}-?\d{4}|02-?\d{3,4}-?\d{4}|0[3-9][1-5]-?\d{3,4}-?\d{4})$"
    )
    return bool(phone_number_pattern.fullmatch(phone_number))


def get_random_string(length: int = 5, number: bool = True, lower: bool = True, upper: bool = True,
                      special: bool = False) -> str:
    """
    Generate a random string based on the specified conditions.

    :param length: Length of the desired random string. Default is 5.
    :param number: Whether to include digits (0-9) in the random string. Default is True.
    :param lower: Whether to include lowercase alphabets (a-z) in the random string. Default is True.
    :param upper: Whether to include uppercase alphabets (A-Z) in the random string. Default is True.
    :param special: Whether to include special characters (e.g., !@#$%) in the random string. Default is False.

    :return: Randomly generated string based on the given conditions.
    :rtype: str

    :raises ValueError: If no valid characters are selected (i.e., all parameters are False).
    """
    characters = ''

    if number:
        characters += string.digits
    if lower:
        characters += string.ascii_lowercase
    if upper:
        characters += string.ascii_uppercase
    if special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No valid characters selected!")

    return ''.join(random.choice(characters) for i in range(length))
