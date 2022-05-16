# OSMO_logger
 
In my crypto activities, I discovered a need to record daily APR changes in different liquidity pools. Unable to find this publicly with a full data set to make analysis, I decided to start logging the daily APR rates myself! Note that this info is more than likely available in some form, somewhere else.

Using the osmosis REST api (api-osmosis.imperator.co) 
and the libraries:

requests
json
pandas
os
datetime


This python script logs the (1, 7, 14) day APR for each osmosis liquidity pool. With some help from pyinstaller and windows task scheduler (shown below) it can run daily at your preffered time for your very own running APR data set! 
Thanks for choosing Logical!

![Screenshot osmo logger1](https://user-images.githubusercontent.com/100737462/168699649-8b926eee-62d1-4508-8bf1-307d1a2797e6.png)

![Screenshot osmo logger2](https://user-images.githubusercontent.com/100737462/168699769-d20adb7d-031e-427a-9671-16a330f5ded2.png)

![Screenshot osmo logger task scheduler](https://user-images.githubusercontent.com/100737462/168700009-212e7c66-6384-4c0d-ba0b-ffb65fdb3340.png)
