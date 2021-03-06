class CustomException(Exception):
    pass

class InvalidNameException(CustomException):
    """Exception raised for errors in name fields.

    Attributes:
        name -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, name, message="Name should be alphabets only"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} : {self.message}'


class InvalidPhoneException(CustomException):
    """Exception raised for errors in phone fields.
    """

    def __init__(self, name, message="Phone should be numeric only"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} : {self.message}'


class InvalidPasswordLengthException(CustomException):
    """Exception raised for errors in password field.
    """

    def __init__(self, name,
                 message="Password should have minimum 8 characters"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} : {self.message}'


class UsernameAlreadyExistsException(CustomException):
    """Exception raised for duplicate username.
    """

    def __init__(self, name, message="username is already taken."):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} : {self.message}'


class EmailAlreadyExistsException(CustomException):
    """Exception raised for duplicate email.
    """

    def __init__(self, name, message="email is already taken."):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} : {self.message}'


class PhoneNumberAlreadyExistsException(CustomException):
    """Exception raised for duplicate phone number.
    """

    def __init__(self, name, message="phone number is already taken."):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} : {self.message}'



