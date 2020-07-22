## This project was developed at Bosch 2020 Hackathon 

This repository consists of the code needed to be able to compute parking availability with 2 ultrasonics sensors with a GPS provided by our smartphone (see this https://github.com/EpsilonZ/GPSReporter_Android for getting the required app which will report the GPS data).

parking_data/ repo contains the map data which tells us where are the parking spots. This data is obtained from source OSM maps and parsered by our custom parser that can be found in src/city_map_parser/. For further details on how OSM parsing source maps works, see this: https://github.com/EpsilonZ/CityVisualizer/tree/master/Analytics (see bottom part where says "ADDITIONAL INFO FOR YOU ON HOW MAP PARSING WORKS. THIS IS JUST ONLY FYI, IS NOT REQUIRED TO PARSE WITH THIS TOOL")

__HARDWARE USED: 1 Raspberry Pi Model 3B+ and two ultrasonic waterproof sensors (JSN-SR04T). If you use them, modify code to set up correctly your pins!__

src/apr_monitor/main.py and use as parameter the config that can be found in src/configs/ to set the parking info in the country you are in


NOTE: This was presented together with an additional AWS connection which pushed the parking data which after was visualized with a cool dashboard
