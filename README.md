# EasyEspFridgeSensor Plugin for CraftBeerPi 4

This plugin enables CraftBeerPi 4 to read sensor data from an ESP device running EasyESP firmware. It's designed for homebrewers looking to integrate ESP-based temperature sensors into their brewing setup.

## Features

- Reads temperature data from ESP devices.
- Configurable task ID and device address.
- Adjustable reading interval.


## Configuration

- **Address**: The IP address or hostname of your ESP device.
- **TaskId**: The task number of the sensor in the EasyESP configuration.
- **ReadingInterval**: Time in seconds between sensor readings.

## Usage

Once configured, the plugin will read the temperature value from the specified ESP device at the set intervals and update the sensor value in CraftBeerPi.

## Support

For issues and features request, please file an issue in the GitHub repository.

## Contributing

Contributions to the plugin are welcome. Please fork the repository and submit a pull request with your improvements.

## License

This plugin is released under the MIT license. See the LICENSE file for more details.
