__version__ = "1.0.0"

try:
    from .ds1307 import DS1307
    from .bh1750 import BH1750
    from .ads1x15 import ADS1115
    from .mcp23017 import MCP23017
    from .bme280 import BME280
    from .at24c02 import AT24C32N
except RuntimeError:
    print("Must be used on Eduponics Mini ESP32 board!")
