# VFS
Got tired of checking on my South African visa status manually, so I wrote a simple python web scraper.

### Site

To check my South African visa status I've been manually entering my credentials at https://www.vfsvisaonline.com/DHAOnlineTracking/OnlineTracking.aspx. But Python could do this quicker.

![screenshot_site](https://user-images.githubusercontent.com/12800512/234707904-d8718e34-2e92-47fe-aa54-d16d0bf2ae49.png)


### Version 1

Initially I wrote a script to handle this. With multiple applications to check this was somewhat inefficient.

![image](https://user-images.githubusercontent.com/12800512/234707821-e127fdfb-99ca-4afa-a727-f124c09ecd37.png)


### Version 2

Hence I rewrote the script using a python class and testing via unittest. After all, Selenium is routinely used for testing.

![image](https://user-images.githubusercontent.com/12800512/234707980-38eeee08-655c-4d0b-aed6-27dd4b5262af.png)


![image](https://user-images.githubusercontent.com/12800512/234708053-63023063-ab27-4942-aeb5-1954014ee0c9.png)


### Result

After running `unittest.main()`, the script shows that all tests return the same value as always. I'll be excited when one of these simple tests fails, as it may indicate that my visa application is no longer pending.

![screenshot_test_result](https://user-images.githubusercontent.com/12800512/234707875-fcd1a4b2-6259-475a-9013-e945f711b3da.png)
