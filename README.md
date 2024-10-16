<pre>
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⡀⢺⣦⠀⠀⠂⢄⡀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣧⠈⣿⣧⠀⠀⠀⠹⣷⠄⠀⣠⠀⢾⠘⠧⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⡆⢸⣿⣧⠀⠀⠀⣠⣴⡄⢸⣆⠘⢦⡴⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⣿⣿⡄⠰⣾⣿⣿⣷⡄⠙⠃⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢹⣿⣧⠀⣿⡿⠟⠉⢠⣤⠀⠀⠀⠀⠀⠀
⠀⠀⢈⠙⠛⠛⠻⠿⠿⠿⠿⠿⣿⡇⢸⡿⠿⠀⠉⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠸⢿⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣶⣿⣿⠿⠀⠀⠀⠀⠀⠀INDI server log viewer
⠀⠀⢰⣤⣤⣤⣭⣍⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣭⣥⣤⣤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⡟⠉⠉⢻⣿⣿⠛⠙⣿⣿⣿⠉⠉⣿⣿⡇⠀⢸⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠸⢿⣿⡇⠀⠀⢸⣿⣿⣤⣤⣿⣿⣿⣴⣶⣿⣿⣿⣶⣾⠿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠋⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀

</pre>

INDI server log viewer is a web application that allows you to view the logs 
of the INDI server in real time.  

In order to use this application, you need to have Kstars with Ekos and 
INDI server installed on the machine with all astrophotography equipment 
connected and run INDI server in terminal.  

If you wish to have client-server setup in place (server machine outside 
with the scope and client machine with you in the warmth of your house), 
please [follow these steps](client-server.md).  

### prerequisites:

- Docker service installed
- docker-compose installed
- Kstarts installed with Ekos and INDI server (version 3.7.3 recommended)

### run INDI server:  

```bash
~ $ indiserver -vvv -p 8080 driver_name [driver_name] > ~/indiserver_log_viewer/indiserver_log_viewer/logs/indiserver.log 2>&1
```

### run INDI server log viewer:  

```bash
~ $ git clone git@github.com:arrrlo/indiserver_log_viewer.git
~ $ cd indiserver_log_viewer
~/indiserver_log_viewer $ docker-compose build
~/indiserver_log_viewer $ docker-compose up
```

### open log viewer web app:  

http://127.0.0.1:8030  

