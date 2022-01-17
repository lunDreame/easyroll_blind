"""Constants for the Detailed Hello World Push integration."""
"""Constants for the Detailed Hello World Push integration."""
from typing import DefaultDict
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import DEVICE_CLASS_TEMPERATURE, PLATFORM_SCHEMA
from homeassistant.config import CONF_NAME
# This is the internal name of the integration, it should also match the directory
# name for the integration.
DOMAIN = "easyroll_blind"
VERSION = "1.0.0"

ENDPOINT_START = 1
ENDPOINT_END = 254

SEARCH_TIMEOUT = 5
SEARCH_PERIOD = 120

CONF_AREA_NAME = "area_name"
CONF_NETWORK_SEARCH = "network_search"
CONF_REFRESH_INTERVAL = "refresh_interval"
CONF_USE_SETUP_MODE = "use_setup"
CONF_HOST = "host"
CONF_ADD_ANODHER = "add_another"
CONF_ADD_GROUP_DEVICE = "add_group_device"

SNAME_SAVE_TOP = "Save Top"
SNAME_SAVE_BOTTOM = "Save Buttom"
SNAME_SAVE_M1 = "Save M1"
SNAME_SAVE_M2 = "Save M2"
SNAME_SAVE_M3 = "Save M3"

SNAME_MOVE_M1 = "Move M1"
SNAME_MOVE_M2 = "Move M2"
SNAME_MOVE_M3 = "Move M3"

SNAME_FORCE_UP = "Force Up"
SNAME_FORCE_DOWN = "Force Down"

SNAME_JOG_UP = "Jog Up"
SNAME_JOG_DOWN = "Jog Down"

SNAME_FIND_ME = "Fine Me"
SNAME_AUTO_LEVELING = "Leveling"

DEFAULT_REFRESH_INTERVAL = 10
DEFAULT_CMD_REFRESH_INTERVAL = 1

OPTIONS = [
    #(CONF_DEVICE_NAME, "", cv.string),
    (CONF_REFRESH_INTERVAL, DEFAULT_REFRESH_INTERVAL, vol.All(vol.Coerce(int), vol.Range(0, 600))),
    (CONF_USE_SETUP_MODE, False, cv.boolean),
    (CONF_ADD_GROUP_DEVICE, False, cv.boolean),
]

DATA_SCHEMA = vol.Schema( {
    vol.Required(CONF_AREA_NAME): str,
    vol.Required(CONF_NETWORK_SEARCH): bool
    }
)
