

class ErrorResponse:
    def __init__(self, code, message):
        self.code = code
        self.message = message
    
    def __str__(self):
        return {
            "code": self.code,
            "message": self.message
        }

class ErrorHandlers:
    @staticmethod
    def list_already_exists(title: str) -> ErrorResponse:
        return ErrorResponse(400, f"List with title '{title}' already exists").__str__()