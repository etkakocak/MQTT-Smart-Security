# MQTT Smart Security
*This is a group project made by Etka Kocak and Furkan Yildirim. The report is personal and the author of this report is Etka Kocak.*  

**Author: Etka Kocak (ek223zf)**  
**Course: 1DT305 - Introduction to IoT**  

MQTT Smart Security is a product that can be used at home, in the workplace, and most importantly in factories or warehouses, i.e. in all places that require extra security. The project consists of 2 circuits, namely 2 devices. Circuit 1 is an alarm with a sensor that can be placed on any door, circuit 2 is a device that is placed inside the local and contains 4 different security sensors.  
Approximate time required to replicate the project: **2-3 hours**


## Objective  
The main reason why I did this project is that I think that the technological progress in the security sector should be accelerated even more. For example, alarmed doors are now a must-have in almost every home not just big locales like schools or company buildings, we live in a time when people can no longer fully trust even the keys. When you are not at home, a fire that may occur due to production negligence in an electronic device, a gas leak that may occur while you are sleeping, or an unexpected earthquake. Additionally, a high level of humidity may occur in the locales, which threatens human health. These are all things we usually see on the news or think about if it happens to us. The solution is technology. The Internet and some sensors can be our personal guards if we use them correctly.  

Circuit 1 of MQTT Smart Security with an ultrasonic distance sensor can detect when someone enters from a door while it is placed on the edge of the door. After that, it uses MQTT to send a notification to your phone and starts the alarm with a buzzer and red LED. You can turn off the alarm easily from your phone if you are the person who opens this door and enters.  

Circuit 2 is more extensive. It includes 4 different sensors and 3 LEDs (red, yellow and green).  
The temperature and humidity sensor instantly transmits the temperature (in celsius) and humidity of the room to your phone via MQTT. You can even see those data in detail as a line chart on a web page. The green led in the circuit is always on and this indicates that everything is ok, but when the yellow led is on, it means you should control the temperature and humidity of your room. If the room is too cold, or too hot, or if there is abnormal humidity, the yellow LED will be on for you to take action about it.  
The flame sensor detects a fire very quickly and send warns you with a notification to your phone. Likewise, the vibration sensor quickly detects vibrations and sends a warning notification to your phone in case of an earthquake. If this earthquake happens while you are awake, it will not help too much, but if it happens while you are asleep, it can save your life. The gas sensor detects any gas that threats human health and warns you with a notification the same way. Some gas leaks are not immediately obvious to people and can be fatal, so this is necessary for homes that use natural gas or fireplaces.  
Not temperature and humidity but those other sensors that can detect important threats turn on the red LED, which means a red alarm. The red LED, therefore, means that you must leave the house directly.


## List of material
|Component |Function |Price and link |
|-|-|-|
|Raspberry Pi Pico W |Programmable microcontroller with WiFi |[98.00 SEK](https://www.electrokit.com/en/product/raspberry-pi-pico-w/) | 
|DHT11 digital temperature and humidity sensor |Sensor for measure humidity and temperature  | [49.00 SEK](https://www.electrokit.com/en/product/digital-temperature-and-humidity-sensor-dht11/) | 
|HC-SR04 ultrasonic distance sensor |Sensor for detecting the distance to an object using sonar | [59.00 SEK](https://www.electrokit.com/en/product/distance-sensor-ultrasound-hc-sr04-2-400cm/) | 
|Pcs Ir Flame Sensor Module |Sensor that can detect a fire or any other bright light sources | [120.49 SEK](https://www.amazon.se/flamsensor-flamdetekteringsmodul-flamdetekteringssensor-kompatibel-justerbar/dp/B095Q6BW85/ref=sr_1_20?crid=29QIEGVQM7K4J&keywords=Pcs+IR+Infrared+Flame+Sensor+Module&qid=1687994286&sprefix=pcs+ir+infrared+flame+sensor+module%2Caps%2C123&sr=8-20) | 
|SW-420 vibration sensor |High sensitivity non-directional vibration sensor | [3.31 SEK](https://www.aliexpress.com/item/32954150924.html?pdp_npi=2%40dis%21SEK%213%2C31kr%213%2C09kr%21%21%21%21%21%402103011116879947026103811ef6e3%2166297503897%21btf&_t=pvid:7e2cd612-34b9-488e-bc54-46d429f7d5d4&afTraceInfo=32954150924__pc__pcBridgePPC__xxxxxx__1687994702&spm=a2g0o.ppclist.product.mainProduct) | 
|MQ-2 gas sensor |Smoke and combustible gas sensor that can detect flammable gas in a range of 300 - 10000ppm | [11.35 SEK](https://www.aliexpress.com/item/1005002742237575.html?&_t=pvid:de58b1a8-b9d3-45bb-92d2-4b4a610e9e9e&afTraceInfo=1005002742237575__pc__pcBridgePPC__xxxxxx__1687994954&spm=a2g0o.ppclist.product.mainProduct) | 
|LED traffic lights light-emitting module |A device that collects LEDs of 3 different colors in a single module | [8.82 SEK](https://www.aliexpress.com/item/32891804932.html?pdp_npi=2%40dis%21SEK%218%2C82kr%217%2C16kr%21%21%21%21%21%402103010c16879951118826566e7bf9%2165741865597%21btf&_t=pvid:424926ad-fb26-412c-89da-0ed2ade8d03c&afTraceInfo=32891804932__pc__pcBridgePPC__xxxxxx__1687995112&spm=a2g0o.ppclist.product.mainProduct) | 
|Buzzer |Audio device that generates a sound from an incoming electrical signal | [37.50 SEK](electrokit.com/en/product/buzzer-3-8-khz/) | 
|LED red |Semiconductor, diode-based, light-emitting electronic circuit element | [9.00 SEK](https://www.electrokit.com/en/product/led-red-3-mm-low-current-2ma-tllr4401/) |   

*NOTE: It can be expensive to buy all these components separately, there are large packages that can be purchased these components in bulk with the breadboard, cables, and resistors. It will be more profitable because these packages will have more of the above. The package I bought is sold out. However, there are many packages that contain all of these on the Internet.*


## Computer Setup
Thonny IDE was used for the software of the circuits. Raspberry Pi Pico W can work with many different IDEs and you can use whatever you want.  
Thonny IDE is simple to use, you can follow the steps below if you choose it:

**1- Download**  
[Download Thonny IDE](https://thonny.org/)  

**2- Setup Raspberry Pi Pico W**  
![image](/img/setup1.png)  
Green arrow: Make sure you have selected Raspberry Pi Pico W as interpreter.  
Red arrow: Both circuits have their codes in folders ``/Circuit1`` and ``/Circuit2``. Please note that codes in each of the folders can only be saved to one Pico W device. So you will need 2 Pico W. Copy and paste those codes and don't forget to choose Pico W as the save location when saving with CTRL+S.  

**3- Libraries**  
![image](/img/setup2.png) 
Some libraries in the code may be missing on your Pico W and the code may not work at the beginning. The libraries I use are usually the ones found on Pico W devices that have been installed, but if it is not found on your device, you can download a missing library from Tools and then Manage Libraries, which is shown with an arrow in the picture.

**4- WiFi**  
The code should be updated with some personal information of the user and the devices should be runned after that.  
The SSID and password of user's WiFi must be written in the code.  
```/Circuit1/main.py```:
``` Python
wlan.connect("SSID HERE", "PASSWORD HERE") # line 38
```
```/Circuit2/main.py```:
``` Python
wlan.connect("SSID HERE", "PASSWORD HERE") # line 76
```

**5- MQTT**   
You need to create an MQTT cloud server account. If you have an account on such a platform, you can use that. Or you can choose [io.adafruit.com](io.adafruit.com) as I use it.  
After creating your account, create the topics in the feeds section with the names written in the codes below.   
![image](/img/setup3.png)   
As you can see in the image, create the topics with the names written in the codes below from the feeds section. Most importantly is My Key section, you will not write password of your in the code, you will write your personal key that you will find in the My Key section.  
```/Circuit1/main.py```:
``` Python
mqtt_server = "io.adafruit.com" # line 26
topic = "YOUR_USERNAME/feeds/sui" # line 28
user = "YOUR_USERNAME" # line 29
password = "YOUR_KEY" # line 30
```
```/Circuit2/main.py```:
``` Python
mqtt_server = "io.adafruit.com"  # line 16
user = "YOUR_USERNAME" # line 17
password = "YOUR_KEY" # line 18
topic_tem = "YOUR_USERNAME/feeds/tem" # line 20
topic_hum = "YOUR_USERNAME/feeds/hum" # line 21
topic_fire = "YOUR_USERNAME/feeds/fire" # line 22
topic_eq = "YOUR_USERNAME/feeds/eq" # line 23
topic_gas = "YOUR_USERNAME/feeds/gas" # line 24
```

**5- Mobile (optional)**  
io.adafruit.com is not only a cloud server, it can also be used as a dashboard. So you can only use your computer to view your IoT data. However, if you want to receive notifications from the phone and access the dashboard much more easily, you can download a MQTT Dashboard.   
There are many MQTT Dashboard applications, but this is the application I use as my dashboard:   
[Download Link](https://play.google.com/store/apps/details?id=com.app.vetru.mqttdashboard&hl=en_US)

**6- Run it**  
After making circuit connections, your devices are now ready to run. If you want, you can run it by connecting to the computer via USB, you can plug it into the socket with a charger or run it with a powerbank.   


## Putting everything together   

### Diagram of the Circuit 1:   
![image](/img/diagram_circuit1.png)   

### Diagram of the Circuit 2:   
![image](/img/diagram_circuit2.png)  

### Connections
The connections are simple, but there are considerations. Diagrams also show which GPIOs connected to pins, but feel free to connect to other GPIOs. The diagrams above are made in an integrated circuit design application called "Digital" and show the connections very clearly.   
However, in case something is not understood from the diagrams, it is useful to go over it in a little detail.   

**Circuit 1:**  
* ``Buzzer``: Has two pins(+ and -). Connect +(long) pin to GPIO and -(short) pin to GND with at least 220Ω resistor.  
* ``LED``: Has two pins(+ and -). Connect +(long) pin to GPIO and -(short) pin to GND with at least 220Ω resistor.  
* ``HC-SR04``: Has four pins(GND, Echo, Trigger, Vcc). Connect Vcc to 3.3 volt output, GND to GND and Trigger to GPIO. Echo pin is important, it should be connected to another GPIO with 1kΩ resistor and also be connected to GND with at least 1kΩ resistor. 

**Circuit 2:**  
*All Vcc pins connects to 3.3 volt output and all GND pins to GND (without any resistor)!*
* ``DHT11``: Has three pins(Vcc, Out, GND). Out pin should be connected first to GPIO without resistor and then to 3.3 volt output with at least 4.7kΩ resistor.   
* ``Flame``: Has three pins(DO, GND, Vcc). DO pin should be connected first to GPIO without resistor and then to 3.3 volt output with 10kΩ resistor.  
* ``SW420``: Has three pins(DO, GND, Vcc). DO pin should be connected to GPIO, no resistor needed.  
* ``MQ2``: Has four pins(Vcc, GND, DO, AO). DO pin should be connected to GPIO, no resistor needed. No need to connect AO pin. 
* ``LEDS``: Has four pins(G, Y, R, GND). G, Y and R should be connected to diffrent GPIOs. G for green, Y for yellow, R for red. No resistor needed. 

It is important to be careful about connecting right resistors. Resistors protect electronic components from overcurrent, and using the wrong resistor may cause the components to burn or explode. If something like this happens, other components in the circuit may also be damaged, so it is important to be careful. Even if there is no physical damage, the use of wrong resistors may also cause the components working incorrectly, or sensors from detecting correctly.  

## Platform  
I preferred to use an MQTT cloud server for this IoT project. An MQTT cloud server platform enables communication between IoT devices using the MQTT protocol. It allows devices to send data to each other, in other words, a message broker. MQTT offers secure messaging between IoT devices, topic-based filtering, security measures, and integrations with other services.  
As I mentioned before, **io.adafruit.com** has been my choice for a cloud server platform. I preferred the Android application called **MQTT Dashboard** for a dashboard. However, io.adafruit.com also had a dashboard, the reason I used another application from the phone was to receive notifications. Both are completely free platforms.  

I didn't find this platform right away and I've looked at other platforms before. There are 2 reasons why I prefer the io.adafruit.com platform.
Most of the other MQTT cloud server platforms I've looked at first are really complex. They ask a lot of unnecessary details for the connection. This is most likely because they have an old back-end. It's not easy to update and so they're probably wondering things that even my internet company doesn't know, in order to establish a simple connection over WiFi.  
Not only that, really most of them need to change their UI designer, or maybe they do it on purpose, I don't know, but it's really complicated to use. It takes an hour to find where to create even a simple topic and this is very annoying. It's more like an airplane cockpit than a basic cloud server, hundreds of buttons in random places on the page.  
The second reason is that most platforms are paid, they require a monthly subscription. A certain fee can be paid for a really high-quality cloud server. But that can't be $45, $35 a month, no matter how high quality they are. Either the developers of this platform do not know how much money 45 dollars per month is or they do it on purpose so that too many people don't use their servers. Anyway, it's the free market, but they should consider how reasonable it is to ask for $45 per month when there are free alternatives like io.adafruit.com.  


## Transmitting the data / connectivity
