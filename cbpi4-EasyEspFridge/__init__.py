import asyncio
import aiohttp
from cbpi.api import *

@parameters([
    Property.Text(
        label="Address",
        description="Please enter the address of your device. E.g.: 192.168.0.5 or esp.fritz.box"
    ),
    Property.Select(
        label="TaskId",
        description="Can be found in EasyESP->Devices->Task **number**",
        options=list(range(1, 13))
    ),
    Property.Select(
        label="ReadingInterval",
        description="Select the delay between reading the values in seconds",
        options=list(range(1, 61, 3))
    )
])
class EasyEspFridgeSensor(CBPiSensor):
    def __init__(self, cbpi, id, props):
        super().__init__(cbpi, id, props)
        self.value = 0
        self.address = self.props.get("Address")  # Device address
        self.taskId = self.props.get("TaskId")  # Task ID from EasyESP
        self.interval = int(self.props.get("ReadingInterval"))  # Reading interval in seconds

        # Constructing the URL for HTTP GET request
        self.url = f"http://{self.address}/json?tasknr={self.taskId}&view=sensorupdate"

    async def read_sensor(self):
        """Reads the sensor value from the specified ESP device."""
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.url) as response:
                    if response.status == 200:
                        data = await response.json()
                        # Extracts the temperature value from the JSON response
                        self.value = float(data['TaskValues'][0]['Value'])
                        self.push_update(self.value)
                    else:
                        # Notifies on status code other than 200
                        self.cbpi.notify("EasyEspFridge Error", f"Failed to read sensor data. HTTP Status: {response.status}", type="danger")
            except Exception as e:
                # Handles exceptions during the HTTP request
                self.cbpi.notify("EasyEspFridge Error", f"Exception while reading sensor data: {str(e)}", type="danger")

    async def run(self):
        """Main loop to continuously read sensor values at the specified interval."""
        while self.running:
            await self.read_sensor()
            self.log_data(self.value)
            self.push_update(self.value)
            await asyncio.sleep(self.interval)  # Waits for the specified interval before the next read

def setup(cbpi):
    cbpi.plugin.register("EasyEsp Sensor", EasyEspFridgeSensor)
