from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery

DOMAIN = "stm_metro_status"

# Called when the integration is set up via UI/config entry
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up STM Metro Status from a config entry."""
    # Store an empty data object if needed
    hass.data.setdefault(DOMAIN, {})

    # Forward the setup to the sensor platform
    await hass.config_entries.async_forward_entry_setup(entry, "sensor")

    return True


# Optional: Support unloading the config entry
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # Unload the sensor platform
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    return True


# Optional: Keep async_setup for legacy YAML support (not required if using UI only)
async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the STM Metro Status integration via YAML (optional)."""
    # Store config for potential use
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    # If YAML config exists, create a config entry from it (advanced)
    # Or just ignore and rely on UI setup

    return True
