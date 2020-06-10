# Auto_daily_report
Auto_daily_report for xmu health system

### Requirement

- selenium

  ```
  pip install selenium
  ```

- chromedriver

  - download address: https://chromedriver.storage.googleapis.com/index.html

  - linux 放到/usr/bin目录下

- mail

  https://www.cnblogs.com/myccloves/p/9420584.html

  

### Config

autoReport.sh 

```shell
usrname="yourusername"      # username
password="yourpassword"     # password
email="youremail"           # email to receive result
```



### Usage

run once

```
sh autoReport.sh
```

run everyday

```
crontab -e
```

添加定时任务

```
30 7 * * * sh yourpath/Auto_daily_report/autoReport.sh
```

重启cron

```
sudo service cron restart
```



