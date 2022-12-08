import base64
import re

RE_INT_AND_MATH = re.compile(r"((-?(?:\d+(?:\.\d+)?))|([-+\/*()])|(-?\.\d+))")


def validate_input(query: str) -> str:
    """
    Performs the validation of the input parms
    :param query:
    :return:
    """
    is_base64(query)
    decoded_params = base64.b64decode(query).decode("utf-8")
    validated_params = only_simple_math_and_numbers(decoded_params)
    return validated_params


def is_base64(query: str) -> bool:
    """
    Checks if the input parm is base64 encoded or not
    :param query:
    :return:
    """
    try:
        return base64.b64encode(base64.b64decode(query)) == query
    except ValueError:
        raise ValueError("Only base64 encoded strings accepted")


def only_simple_math_and_numbers(params: str) -> str:
    """
    Validates if we are just getting inputs as math and number not some
    other irrelevant charters
    :param params:
    :return:
    """
    if RE_INT_AND_MATH.match(params):
        return params
    else:
        raise ValueError("Only simple math + - * / ( ) and numbers [0-9] required")
