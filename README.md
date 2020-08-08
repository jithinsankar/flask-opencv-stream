# flask-opencv-stream


### Dependencies
  - Python 3
  - flask
  - opencv [can be omitted if using any other library that can can import frames as jpg]

run

```sh
 
 git clone https://github.com/jithinsankar/flask-opencv-stream.git
```

note the ip address by running ifconfig

![](https://i.imgur.com/DkfN8HM.png)]

Run the following from the cloned directory
```sh
export FLASK_APP=app.py
flask run --host=0.0.0.0
```

![](https://i.imgur.com/0CGoaS9.png)]

open the ip address from any connected device in the network with port number as 5000

![](https://i.imgur.com/Wq0ZNWK.jpg)]

Directional commands from any connected device can be passed to the server.


![](https://i.imgur.com/FS8h1aR.png)]
