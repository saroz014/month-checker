class NumberNotInRangeError(Exception):
    """Exception raised for errors in the input value.

    Attributes:
        number -- input value which caused the error
    """

    def __init__(self, number, start, end):
        self.number = number
        self.message = f"Number is not in ({start}, {end}) range"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.number} -> {self.message}'


class StartIsGreaterThanEndError(Exception):
    """Exception raised if start value is greater than end value.

    Attributes:
        start -- starting value
        end -- ending value
    """

    def __init__(self, start, end):
        self.message = f"{start} is greater than {end}"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class StartIsEqualToEndError(Exception):
    """Exception raised if start value is equal to end value.

    Attributes:
        start -- starting value
        end -- ending value
    """

    def __init__(self, start, end):
        self.message = f"{start} is equal to {end}"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
