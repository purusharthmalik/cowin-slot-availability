# Cowin-slot-availability

A python script that you can keep running in the background to get instantly notified whenever a slot opens up in your district.

Once executed, the script will check the cowin API for slots in your district every 60 seconds.

The cowin API will only function on Indian IP addresses, so you may have to disable your VPN.

## Usage

<ul>
  <li>Make sure you have Python installed in your system. If not, you can install it either using <a href = "https://www.anaconda.com/products/individual">Anaconda</a>(recommended) or from the <a href = "https://www.python.org/downloads/">Official Python website</a>.
  </li>
  <li>Clone the repository to your system</li>
  <li>Open termianl or command line and navigate to the cloned folder</li>
  <li>To install the required libraries, execute the following command:</li>
 
  ```pip install -r requirements.txt```
  <li>Execute the script:</li>
  
  ```python availablity_checker.py ```
  <li>Enter the necessary information:</br>
  <img src = "/.images/inputs.png" width = 400></li>
  </br>
  <li>Result:</br>
  <img src = "/.images/results.png" width = 400>
  </li>
  <li>Notifications:</br>
  <img src = "/.images/notifs.png" width = 400>
  </li>
