from typing import Any

from scales_drivers.drivers import Generic, CASType6

# Devices
scales_params: dict[int, dict[str, Any]] = {
    1: {
        'port': 'com6',
        'baudrate': 9600,
        'bytesize': 8,
        'parity': 'N',
        'stopbits': 1,
        'driver': CASType6
    },
    # 2: {
    #     'port': 'com1',
    #     'baudrate': 9600,
    #     'bytesize': 8,
    #     'parity': 'N',
    #     'stopbits': 1,
    #     'driver': CASType6
    # },
}

# Unit of measure
UNIT = Generic.KG
DECIMAL_PLACES = 4

# Scale statuses in responses
STATUS: dict[int, str] = {
    Generic.STATUS_OVERLOAD: 'overload',
    Generic.STATUS_STABLE: 'stable',
    Generic.STATUS_UNSTABLE: 'unstable',
}
