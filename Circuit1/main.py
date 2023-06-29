import machine
import time
import network
from umqttsimple import MQTTClient

hcsr04_trigger = machine.Pin(22, machine.Pin.OUT)
hcsr04_echo = machine.Pin(15, machine.Pin.IN)
led_pin = machine.Pin(16, machine.Pin.OUT)
buzzer_pin = machine.Pin(7, machine.Pin.OUT)

def measure_distance():
    hcsr04_trigger.value(1)
    time.sleep_us(10)
    hcsr04_trigger.value(0)
    pulse_time = machine.time_pulse_us(hcsr04_echo, 1, 1000000)
    distance = pulse_time / 2 / 29.1
    return distance

def alarm():
    led_pin.value(1)
    buzzer_pin.value(1) 
    time.sleep(0.5) 
    led_pin.value(0) 
    buzzer_pin.value(0) 

mqtt_server = "io.adafruit.com"
client_id = "SEC"
topic = "YOUR_USERNAME/feeds/sui"
user = "YOUR_USERNAME"
password = "YOUR_KEY"

client = None

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect("SSID HERE", "PASSWORD HERE")
        while not wlan.isconnected():
            pass
    print("WiFi = True. IP:", wlan.ifconfig()[0])

def connect_mqtt():
    global client
    client = MQTTClient(client_id, mqtt_server, 1883, user, password, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker' % (mqtt_server))

def send_mqtt_message(topic, message):
    global client  
    client.publish(topic, bytes(str(message), 'utf-8'))
    print("MQTT publish:", topic, "about:", message)

connect_wifi()
connect_mqtt()

while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")

    if distance < 10:
        send_mqtt_message(topic, 1)
        alarm()

    time.sleep(0.1)