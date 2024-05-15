from re import search as regex_search
from re import escape as regex_escape
from string import punctuation


class FilterModule(object):

    def filters(self):
        return {
            "meets_password_complexity": self.meets_password_complexity,
        }

    @staticmethod
    def meets_password_complexity(pwd: str) -> bool:
        pwd = str(pwd)
        return all([
            len(pwd) >= 8,
            regex_search(r'[0-9]', pwd) is not None,
            regex_search(r'[a-z]', pwd) is not None,
            regex_search(r'[A-Z]', pwd) is not None,
            regex_search(fr'[{regex_escape(punctuation)}]', pwd) is not None,
        ])
