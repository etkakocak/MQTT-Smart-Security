import machine
import time
import dht
import network
from umqttsimple import MQTTClient

sensor_DHT11 = dht.DHT11(machine.Pin(28))
sensor_FLAME = machine.Pin(11, machine.Pin.IN)
sensor_SW420 = machine.Pin(27, machine.Pin.IN)
sensor_MQ2 = machine.Pin(22, machine.Pin.IN)

led_green = machine.Pin(21, machine.Pin.OUT)
led_yellow = machine.Pin(20, machine.Pin.OUT)
led_red = machine.Pin(19, machine.Pin.OUT)

mqtt_server = "io.adafruit.com"
user = "YOUR_USERNAME"
password = "YOUR_KEY"
client_id = "SEC2"
topic_tem = "YOUR_USERNAME/feeds/tem"
topic_hum = "YOUR_USERNAME/feeds/hum"
topic_fire = "YOUR_USERNAME/feeds/fire"
topic_eq = "YOUR_USERNAME/feeds/eq"
topic_gas = "YOUR_USERNAME/feeds/gas"
client = None

def DHT11():
    try:
        sensor_DHT11.measure()
        temperature = sensor_DHT11.temperature()
        humidity = sensor_DHT11.humidity()
        
        send_mqtt_message(topic_tem, temperature)
        send_mqtt_message(topic_hum, humidity)
        
        if temperature < 20 or temperature > 30:
            led_green.value(0)
            led_yellow.value(1)
        if humidity < 30 or humidity > 50:
            led_green.value(0)
            led_yellow.value(1)
    except:
        err = -1
        send_mqtt_message(topic_tem, err)
        send_mqtt_message(topic_hum, err)
        
    
def FLAME():
    if sensor_FLAME.value() == 0:
        print("FIRE!")
        led_green.value(0)
        led_red.value(1)
        send_mqtt_message(topic_fire, 1)
    
    
def SW420():
    if sensor_SW420.value() == 1:
        print("Earthquake!")
        led_green.value(0)
        led_red.value(1)
        send_mqtt_message(topic_eq, 1)


def MQ2():
    if sensor_MQ2.value() == 0:
        print("Gas leak!")
        led_green.value(0)
        led_red.value(1)
        send_mqtt_message(topic_gas, 1)


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
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(1)
    
    DHT11()
    FLAME()
    SW420()
    MQ2()
    
    time.sleep(3)
