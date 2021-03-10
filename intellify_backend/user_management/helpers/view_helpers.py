class APIViewResponse(object):
    def __init__(self, status=None, errors=[],
                 message="", data={}, status_code=""):
        self._status = status
        self._data = data
        self._errors = errors
        self._message = message
        self._status_code = status_code

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def errors(self):
        return self._errors

    @errors.setter
    def errors(self, value):
        self._errors = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    def json(self):
        return {
            "success": self.status,
            "errors": self.errors,
            "message": self.message,
            "data": self.data,
            "status_code": self.status_code
        }

    def update(self, **kwargs):
        try:
            self.status = kwargs["status"]
        except KeyError as e:
            pass

        try:
            if isinstance(kwargs["errors"], list):
                self.errors = kwargs["errors"]

            elif kwargs["errors"]:
                self.errors = [kwargs["errors"]]

        except KeyError as e:
            pass

        try:
            self.message = kwargs["message"]
        except KeyError as e:
            pass

        try:
            self.status_code = kwargs["code"]
        except KeyError as e:
            pass


class APIViewSuccessResponse(APIViewResponse):
    SUCCESS_RESPONSE = {
        "status": True,
        "message": "Success",
        "errors": [],
        "data": {},
        "status_code": "100000"
    }

    def __init__(self, status=None, errors=[], message="", data={}):
        super().__init__(**APIViewSuccessResponse.SUCCESS_RESPONSE)

    def json(self):
        return {
            "success": self._status,
            "errors": self._errors,
            "message": self._message,
            "data": self._data,
            "status_code": self._status_code
        }


class APIViewErrorResponse(APIViewResponse):
    ERROR_RESPONSE = {
        "status": False,
        "message": "Error",
        "errors": [],
        "data": {},
        "status_code": "200000"
    }

    def __init__(self, status=None, errors=[], message="", data={}):
        super().__init__(**APIViewErrorResponse.ERROR_RESPONSE)

    def json(self):
        return {
            "success": self._status,
            "errors": self._errors,
            "message": self._message,
            "data": self._data,
            "status_code": self._status_code
        }
