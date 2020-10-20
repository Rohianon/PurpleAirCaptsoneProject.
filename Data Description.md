# Using PurpleAir data
PurpleAir sensors employ a dual laser counter to provide some level of data integrity. This is intended to provide a way of determining sensor health and fault detection. Some examples of what can go wrong with a laser counter are a fan failure, insects or other debris inside the device or just a layer of dust from long term exposure. 

If both laser counters (channels) are in agreement, the data can be seen as excellent quality. If there are different readings from the two channels, there may be a fault with one or both.

In the case of a fault, the channel may be marked as flagged or downgraded (suspect or known faulty).

PurpleAir provides ways to get direct access to the data and there are a few different ways to do this.
### - You can download the data from the page --> [sensorlist](https://www.purpleair.com/sensorlist)
This page provides an easy to use interface to download data based on a date range. You access this page by zooming into the map, then using the download button in the bottom right of the screen. Alternatively a download link is available per sensor in the “Get this widget” section after clicking a map icon.

- Select the sensor/s in the list you want to download.
- At the top of the page, enter the desired date range, then click Download Selected.


### - Accessing data directly from Thingspeak:
Another way to get the data is to use ThingSpeak.com and to do this, you will need the API Key and channelID. These two pieces of data are available from PurpleAir’s JSON.

NOTE: PurpleAir implements a rate limiting mechanism to prevent users from overloading the API servers. If you request data from the API in quick succession, you will get an error message. 

More info on using ThingSpeak’s API is [here:](https://www.mathworks.com/help/thingspeak/rest-api.html)
### - PA-II-SD data format( For this particular Project)

The SD Card version of the PA-II (PA-II-SD) has a built in real time clock and OPENLOG serial logger. The SD card contains data in CSV format that were collected for this particular project.

## ThingSpeak Data Field descriptions:
Channel A and B, primary and secondary ThingSpeak channels together provide 32 fields for each sensor.
There are six ug/m3 values and six particle counts for each channel (laser) as well as temperature, humidity, WiFi signal (RSSI), sensor uptime, free memory and analog input amongst others. 

|Column| Latest Firmware Headers | Header Description based on PA-II-SD data format |
|:-:|:-:|:-:|
1.| **UTCDateTime** | Date and time derived from the Real Time Clock and synced with NTP where possible (in UTC).
2.| **Adc** |  The voltage reading on the analog input of the control board.
3.| **Current_dewpoint_f** | Calculated dew point in F.
3.| **Current_humidity** | Current Humidity in %.
5.| **Current_temp_f** | Current temperature in F.
6.| **Firmware_ver** | Firmware version of the control board.
7.| **Gas** | FIRMWARE 4.10 and up: Bosch BSEC IAQ when BME680 gas sensor is present
8.| **Hardware** | Hardware the control board has detected.
9.| **Mac_address** | The MAC address of the WiFi module on the sensor (used as an ID for the unit).
10.| **Mem** | Free HEAP memory on the control board.
11.| **p_0_3_um** | Channel A 0.3 micrometer particle counts per deciliter of air
12.| **p_0_3_um_b** | Channel B 0.3 micrometer particle counts per deciliter of air
13.| **p_0_5_um** | Channel A 0.5 micrometer particle counts per deciliter of air
14.| **p_0_5_um_b** | Channel B 0.5 micrometer particle counts per deciliter of air
15.| **p_10_0_um** | Channel A 10.0 micrometer particle counts per deciliter of air
16.| **p_10_0_um_b** | Channel B 10.0 micrometer particle counts per deciliter of air
17.| **p_1_0_um** | Channel A 1.0 micrometer particle counts per deciliter of air
18.| **p_1_0_um_b | Channel B 1.0 micrometer particle counts per deciliter of air
19.| **p_2_5_um** | Channel A 2.5 micrometer particle counts per deciliter of air
20.| **p_2_5_um_b** | Channel B 2.5 micrometer particle counts per deciliter of air
21.| **p_5_0_um** | Channel A 5.0 micrometer particle counts per deciliter of air
22.| **p_5_0_um_b** | Channel B 5.0 micrometer particle counts per deciliter of air
23.| **pm10_0_atm** | Channel A ATM PM10.0 particulate mass in ug/m3.
24.| **pm10_0_atm_b** | Channel B ATM PM10.0 particulate mass in ug/m3.
25.| **pm10_0_cf_1** | Channel A CF=1 PM10.0 particulate mass in ug/m3
26.| **pm10_0_cf_1_b** | Channel B CF=1 PM10.0 particulate mass in ug/m3
27.| **pm1_0_atm** | Channel A ATM PM1.0 particulate mass in ug/m3.
28.| **pm1_0_atm_b** | Channel B ATM PM1.0 particulate mass in ug/m3.
29.| **pm1_0_cf_1** | Channel A CF=1 PM1.0 particulate mass in ug/m3
30.| **pm1_0_cf_1_b** | Channel B CF=1 PM1.0 particulate mass in ug/m3
31.| **pm2.5_aqi_atm** | Channel A air quality index based on PM2.5 (ATM)
32.| **pm2.5_aqi_atm_b** | Channel B air quality index based on PM2.5 (ATM)
33.| **pm2.5_aqi_cf_1** | Channel A air quality index based on PM2.5 (CF=1)
34.| **pm2.5_aqi_cf_1_b** | Channel B air quality index based on PM2.5 (CF=1)
35.| **pm2_5_atm** | Channel A ATM PM2.5 particulate mass in ug/m3.
36.| **pm2_5_atm_b** | Channel B ATM PM2.5 particulate mass in ug/m3.
37.| **pm2_5_cf_1** | Channel A CF=1 PM2.5 particulate mass in ug/m3
38.| **pm2_5_cf_1_b** | Channel B CF=1 PM2.5 particulate mass in ug/m3
39.| **Pressure** | Current pressure in millibars.
40.| **Rssi** | WiFi signal strength in dBm
41.| **Uptime** | Firmware uptime in seconds.

## PA-II NOTES:
* Each sensor contains two identical laser counters, hence channel A and B. If these two channels do not agree to some extent, then there is something wrong with one or both channesl.
* All time stamps are UTC.

## Other Notes.
## Plantower PMS sensor notes:
ATM is "atmospheric", meant to be used for outdoor applications
CF=1 is meant to be used for indoor or controlled environment applications
Original (incorrect) assumption: PurpleAir uses CF=1 values on the map. This value is lower than the ATM value in higher measured concentrations.
New (correct) statement: Due to the firmware swapping the labels, PurpleAir has inadvertently always used CF=ATM on the map. It is ATM values that are lower than CF=1 at high concentrations. This mislabeling has been present since day one and was the result of a lack of information on the sensor specs at the time we first started using the Plantower particle counters. The PurpleAir download tool had the labels switched on the 20 October 2019.

* PurpleAir sensors attempt to send both primary and secondary data every two minutes or so.

