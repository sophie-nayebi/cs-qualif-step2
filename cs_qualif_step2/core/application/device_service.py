import hashlib
from xml.dom import NotFoundErr

from cs_qualif_step2.core.application.dto.personalised_config import PersonalizedDeviceConfig
from cs_qualif_step2.core.domain.device.device_repository import DeviceRepository
from cs_qualif_step2.core.application.dto.device_config import DeviceConfig
from cs_qualif_step2.core.domain.device.devicefactory import DeviceFactory
from cs_qualif_step2.core.domain.device.exception.device_with_same_mac_address_exception import \
    DeviceWithSameMacAddressException


class DeviceService:
    def __init__(self, device_repository: DeviceRepository, device_factory: DeviceFactory) -> None:
        self.device_repository = device_repository
        self.device_factory = device_factory

    def register_device(self, device_config: DeviceConfig) -> str:
        device_with_same_mac_address = self.device_repository.find_by_mac_address(device_config.macAddress)
        if device_with_same_mac_address is not None:
            raise DeviceWithSameMacAddressException(device_with_same_mac_address.get_mac_address())

        device = self.device_factory.create_device(device_config)

        self.device_repository.save(device)

        return str(device.get_device_id())

    def get_config(self, device_id: str) -> PersonalizedDeviceConfig:
        device = self.device_repository.find_by_id(device_id)
        if device is None:
            raise NotFoundErr("Device not found")
        return PersonalizedDeviceConfig()