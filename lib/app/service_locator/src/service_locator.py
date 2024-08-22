class ServiceLocator:
    _services = {}

    @classmethod
    def register_service(cls, name: str, service):
        cls._services[name] = service

    @classmethod
    def get_service(cls, name: str):
        return cls._services.get(name)
