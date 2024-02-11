import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID, CONF_KEY

CONF_TM1637_6C_ID = "tm1637_6c_id"

tm1637_6c_ns = cg.esphome_ns.namespace("tm1637_6c")
TM1637_6C_Display = tm1637_6c_ns.class_("TM1637_6C_Display", cg.PollingComponent)
TM1637_6C_Key = tm1637_6c_ns.class_("TM1637_6C_Key", binary_sensor.BinarySensor)

CONFIG_SCHEMA = binary_sensor.binary_sensor_schema(TM1637_6C_Key).extend(
    {
        cv.GenerateID(CONF_TM1637_6C_ID): cv.use_id(TM1637_6C_Display),
        cv.Required(CONF_KEY): cv.int_range(min=0, max=15),
    }
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await binary_sensor.register_binary_sensor(var, config)
    cg.add(var.set_keycode(config[CONF_KEY]))
    hub = await cg.get_variable(config[CONF_TM1637_6C_ID])
    cg.add(hub.add_tm1637_6c_key(var))
