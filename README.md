# Auto_daily_report
Auto_daily_report for xmu health system

### Introduction

- 支持在“承诺xxxx”的下拉框选择“是” ☑️
- 支持保存表单  ☑️
- 支持判断是否打卡成功   ☑️
  - 打卡失败，间隔1h后重新打卡
    - 若打卡失败5次，发邮件通知“打卡失败”
  - 打卡成功，发邮件通知 “打卡成功”

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

Ps. 可能需要指定python路径

PPs. 如果要添加定时任务，要在脚本里（email 后面）添加一句

```
cd yourpath/Auto_daily_report
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
0 7 * * * sh yourpath/Auto_daily_report/autoReport.sh >> yourlogfile 2>&1 &
```

重启cron

```
sudo service cron restart
```



### Updata

2020-6-11 修复脚本判断打卡失败情况的bug

```
until 的判断条件改成“或”的关系 （-a --> -o）
```



2020-6-12 修复python脚本打卡成功exit返回值bug

```
sys.exit(0)   #原本使用sys.exit(), 会被try...except捕捉到, 导致返回值一直是1
os._exit(0)   #os._exit()会直接退出，成功的话返回值是0，否则为1
```



2020-6-15 修复判断打卡状态并发邮件bug

1. 状态判断：保存成功后，刷新页面，通过是否有日志来进行判断

2. 发邮件bug：

   ```
   mail -s "Daily report success" email ==> mail -s "Daily report success" $email
   ```

   

### To do

- ~~判断打卡状态发邮件的功能待测试~~