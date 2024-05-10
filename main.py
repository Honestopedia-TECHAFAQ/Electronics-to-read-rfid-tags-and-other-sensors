import RFID_library  
import sensor_library  
import relay_library 
import connectivity_library  
import time
import threading


rfid_reader = RFID_library.RFIDReader()
sensors = [sensor_library.Sensor() for _ in range(10)]
relays = [relay_library.Relay() for _ in range(3)]  
connectivity = connectivity_library.Connectivity()

light_threshold = 100  
temperature_threshold = 30  

def control_relays(sensor_data):
    if sensor_data[0] < light_threshold:
        relays[0].turn_on()
    else:
        relays[0].turn_off()
def read_rfid():
    return rfid_reader.read_tag()
def read_sensors():
    return [sensor.read() for sensor in sensors]
def transmit_data(rfid_data, sensor_data):
    connectivity.transmit_data(rfid_data, sensor_data)
def check_alerts(sensor_data):
    if sensor_data[1] > temperature_threshold:
        connectivity.send_alert("Temperature too high!")
def main_loop():
    while True:
        rfid_data = read_rfid()
        sensor_data = read_sensors()
        control_relays(sensor_data)
        transmit_data(rfid_data, sensor_data)
        check_alerts(sensor_data)
        time.sleep(1)
def run_main_loop():
    main_thread = threading.Thread(target=main_loop)
    main_thread.daemon = True
    main_thread.start()
if __name__ == "__main__":
    run_main_loop()
