## File Directory


This script will 
* take the blade from a predefined position i.e. -76657 to the scanner position (-94000)
* then take the blade under the camera position i.e. -85000 from the scanner position
* Finally, the blade will be taken to predefined inital positon i.e. -76657


* If the blade is at the predefined intial position then run

$ python to_scanner.py

* If the blade is at not at the predefined position then run the following scripts accordingly

$ python to_initial_position.py
$ python to_scanner.py

