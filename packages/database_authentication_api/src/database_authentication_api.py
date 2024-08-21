from packages.authentication_api import AuthenticationApi
class DatabaseAuthenticationApi(AuthenticationApi):
    def __init__(self ,*,connectionManager) -> None:
        self.connectionManager = connectionManager
    