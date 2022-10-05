import logging
from decimal import Decimal
from typing import Any, Optional

from scales_drivers.drivers import Generic
from scales_drivers.exceptions import ScalesException, SerialError
import settings


class Scales:
    def __init__(self) -> None:
        self.scales: dict[Any, Generic] = {}
        for scales_id, params in settings.scales_params.items():
            logging.debug(f'Scales id={scales_id}')
            driver: type[Generic] = params['driver']
            self.scales[scales_id] = driver(port=params['port'],
                                            baudrate=params['baudrate'],
                                            bytesize=params['bytesize'],
                                            parity=params['parity'],
                                            stopbits=params['stopbits'],
                                            timeout=0.5)
            try:
                self.scales[scales_id].scales_init()
            except SerialError:
                pass

    def get_weight(self, scales_id: int) -> Optional[Decimal]:
        scales: Generic = self.scales[scales_id]
        try:
            scales.update()
            return scales.get_weight(settings.UNIT, settings.DECIMAL_PLACES)
        except ScalesException:
            return None
        except SerialError:
            scales.scales_reinit()
            return None

    def get_status(self, scales_id: int) -> Optional[str]:
        scales = self.scales[scales_id]
        status = settings.STATUS.get(scales.get_status())
        return status
