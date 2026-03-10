import getpass
from typing import Protocol


class FilterProtocol(Protocol):
    def validate(self, password: str) -> list:
        # Protocols usually don't need an implementation,
        # but if you want one, use NotImplementedError
        raise NotImplementedError("Filter must implement validate func!")


class LenghtFilter(FilterProtocol):
    def __init__(self, min: int = 4, max: int = None):
        self.min = min
        self.max = max

    def validate(self, password: str) -> list:
        errors = []
        if len(password) < self.min:
            errors.append("Password length is smaller than min.")

        if self.max is not None and len(password) > self.max:
            errors.append("Password length is larger than max.")

        return errors  # Crucial for your tests to work!


class SpecialCharFilter(FilterProtocol):
    def __init__(self, min_required: int = 1, special_chars=None):
        self.min_required = min_required
        self.special_chars = special_chars if special_chars else [".", ",", "*", "&"]

    def validate(self, password: str) -> list:
        errors = []
        # Count occurrences
        found = sum(1 for char in password if char in self.special_chars)

        if found < self.min_required:
            errors.append(f"Password must contain at least {self.min_required} special characters.")
        return errors


class AndFilter(FilterProtocol):
    def __init__(self, filters: list):
        self.filters = filters

    # Ensure this is at the same indentation level as __init__
    def validate(self, password: str) -> list:
        all_errors = []
        for f in self.filters:
            _error = f.validate(password)
            # Use .extend() or += to combine lists
            all_errors.extend(_error)

            # Return AFTER the loop finishes
        return all_errors

if __name__ =="__main__":
    filters=[]
    special_char_filter = SpecialCharFilter()
    filters.append(special_char_filter)
    length_filter = LenghtFilter(8)
    filters.append(length_filter)
    and_filter = AndFilter(filters)
    while True:
        password = getpass.getpass("check: ")
        errors = and_filter.validate(password)
        if len(errors)==0:
            print("pass is ok")
        else:
            print("pass error")
            for error in errors:
                print("\t-", error)