from ipaddress import ip_address
from re import search as regex_search
from re import escape as regex_escape
from string import punctuation


class FilterModule(object):

    def filters(self):
        return {
            "meets_password_complexity": self.meets_password_complexity,
            "is_boolean": self.is_boolean,
            "build_cert_san": self.build_cert_san,
            "ensure_list": self.ensure_list,
            "extend_list": self.extend_list,
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

    @staticmethod
    def is_boolean(value: any) -> bool:
        return isinstance(value, bool)

    @staticmethod
    def build_cert_san(san_raw: list[str]) -> str:
        san = []

        for sr in san_raw:
            try:
                ip_address(sr)
                san.append(f'IP:{sr}')

            except ValueError:
                san.append(f'DNS:{sr}')

        return ','.join(san)

    @staticmethod
    def ensure_list(data: (str, dict, list)) -> list:
        # if user supplied a string instead of a list => convert it to match our expectations
        if data is None:
            return []

        if isinstance(data, list):
            return data

        return [data]

    @classmethod
    def extend_list(cls, l1: any, l2: any) -> list:
        out = cls.ensure_list(l1)
        out.extend(cls.ensure_list(l2))
        out = list(set(out))  # dedupe
        return out
