from collections import deque
from enum import Enum
import unittest


class MatchingBraceCases(Enum):
    NO_OPENING_BRACE = "No matching opening brace found"
    MISMATCHED_OPENING_BRACE = "Found character with mismatched brace"
    UNMATCHED_OPENING_BRACE = "Found unmatched opening brace"
    EMPTY_STACK = "Passed"


def is_opening_brace(char):
    chars = ["[", "(", "{"]
    if char in chars:
        return True
    return False


def is_closing_brace(char):
    chars = ["]", ")", "}"]
    if char in chars:
        return True
    return False


def is_a_match(char1, char2):
    matches = {"[": "]", "(": ")", "{": "}"}
    return matches[char1] == char2


def check_braces(text):
    stack = deque()
    for char in text:
        if is_opening_brace(char):
            stack.append(char)
        elif is_closing_brace(char):
            if not stack:
                return MatchingBraceCases.NO_OPENING_BRACE.value
            top_char_in_stack = stack.pop()
            if not is_a_match(top_char_in_stack, char):
                return MatchingBraceCases.MISMATCHED_OPENING_BRACE.value

    if stack:
        return MatchingBraceCases.UNMATCHED_OPENING_BRACE.value
    return MatchingBraceCases.EMPTY_STACK.value


class CheckBracesTest(unittest.TestCase):
    def test_no_opening_brace(self):
        code = "something}"
        result = check_braces(code)
        self.assertEqual(result, MatchingBraceCases.NO_OPENING_BRACE.value)

    def test_mismatched_opening_brace(self):
        code = "(something}"
        result = check_braces(code)
        self.assertEqual(result, MatchingBraceCases.MISMATCHED_OPENING_BRACE.value)

    def test_unmatched_opening_brace(self):
        code = "{something"
        result = check_braces(code)
        self.assertEqual(result, MatchingBraceCases.UNMATCHED_OPENING_BRACE.value)

    def test_matching_braces(self):
        code = "{something}"
        result = check_braces(code)
        self.assertEqual(result, MatchingBraceCases.EMPTY_STACK.value)