# INDI server log viewer  

### run INDI server:  

```bash
> indiserver -vvv -p 8080 driver_name [driver_name] > ~/indiserver_log_viewer/indiserver_log_viewer/logs/indiserver.log 2>&1
```

### run INDI server log viewer:  

```bash
~ $ git clone git@github.com:arrrlo/indiserver_log_viewer.git
~/indiserver_log_viewer $ cd indiserver_log_viewer
~/indiserver_log_viewer $ docker-compose build
~/indiserver_log_viewer $ docker-compose up
```

### open log viewer web app:  

http://127.0.0.1:8030  

