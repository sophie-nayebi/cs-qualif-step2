from pydantic import BaseModel, validator
import re
import pytz

class DeviceRegistrationRequest(BaseModel):
    macAddress: str
    model: str
    firmwareVersion: str
    serialNumber: str
    displayName: str = None
    location: str = None
    timezone: str = None

    @validator('macAddress', 'model', 'firmwareVersion', 'serialNumber')
    def not_empty(cls, v):
        if v is None or v.strip() == '':
            raise ValueError('Field cannot be empty or null')
        return v

    @validator('firmwareVersion')
    def valid_firmware(cls, v):
        if not bool(re.search("\d+\.\d+\.\d+", v)):
            raise ValueError('Firmware version format is not valid')
        return v

    @validator('location')
    def valid_location(cls, v):
        if v is not None and not bool(re.search(".+, .+", v)):
            raise ValueError('Location is not valid')
        return v

    @validator('timezone')
    def valid_timezone(cls, v):
        if v is not None and not v in pytz.all_timezones:
            raise ValueError('Time zone is not valid')
        return v