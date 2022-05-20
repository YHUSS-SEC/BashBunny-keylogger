# BashBunny-keylogger
Python-based BashBunny Keylogger Program with DUCKY Scripts (Windows OS ONLY!!) 

## Instructions 
### SMTP credentials

SMTP mail server name is set by default to localhost, but, can be changed to other email severs of your choice.

https://github.com/YHUSS-SEC/BashBunny-keylogger/blob/90e77237aee5ef87872d5ab5ee3a055440ecc89c/main.py#L78-L82

* I had no issues using port 587.
 
* If you wanted to include mail server authentication you will need to amend my code to suit your needs. 

* If you are running this exploit on a local mail server ,as I did to test out this vulnrability, please do not amend the code.

* on LINES 80 + 81, it is heavily advised that both the sender_email and receiver_email values are set the same as it worked perfectly for me. of course you will have different email+password combination as I have, so, just edit the values to values that are your own credentials.


### Timer Function Edit

Whilst testing this exploit, i had a default timer set to 10 seconds for the sendlogs function as well as the logstatus function. the relevant lines can be found on LINE 89 and LINE 91.

https://github.com/YHUSS-SEC/BashBunny-keylogger/blob/90e77237aee5ef87872d5ab5ee3a055440ecc89c/main.py#L89-L92

* I suggest that the time is increased considerably as you dont want your email being spammed every 10 seconds. I only the integer set to 10 during the testing phase but suggest that the int is upped to at least 600 (10 Mins).

* It is heavily advised that integer values on LINE 89 + LINE 91 are both matching to avoid any potential errors/syntax  

### Pyinstaller 
* Once the main.py file has been edited to your liking, the raw main.py file should then be compiled into an .exe format with all libraries installed on the python IDE.

* Pyinstaller is the exe application compiler that I used.

* if you would like a resource that helped me with understanding how pyinstaller works, click [HERE](https://www.youtube.com/watch?v=WLBpBVObWDI)

### switch.txt Configuration

Within the switch.txt file the default location to put the main.exe file is within the /temp folder.

https://github.com/YHUSS-SEC/BashBunny-keylogger/blob/f1dba783f01614dd32c30ce3a2b11ad30331e23b/switch.txt#L15-L18

* If you would like to change the file destination of main.exe, you can do so by amending the end of lINE 15.

* On LINE 15, the default switch folder is switch1, if you have placed the file into switch2 then you must change this also.

* On line 18 the default is set to /temp directory, so, whatever file location you changed on LINE 15 must be mirroring the location specified on LINE 18.

### BashBunny Directory Format For File Placement

* Dir Print: X:/BashBunny/payloads/switch1/"(main.exe | switch.txt | payload.txt)"

**REMEMBER!!** main.exe + switch.txt + payload.txt MUST be placed in the switch1 or switch2 folder

* If you place the files into the switch1 folder, the switch position on the BashBunny must be set to switch position 1
  
* If you place the files into the switch2 folder, the switch position on the BashBunny must be set to switch position 2 

* If you are unsure about the Directory structure or the physical switch positions of the BashBunny there is a [BashBunny-Wiki](https://github.com/hak5/bashbunny-wiki/blob/master/index.md) that will clear things up



