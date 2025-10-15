from pydantic import BaseModel

class DeviceRegistrationRequest(BaseModel):
    macAddress: str
    model: str
    firmwareVersion: str
    serialNumber: str
    displayName: str = None
    location: str = None
    timezone: str = None
