# Simulating-Traffic-in-San-Francisco

For this sim, we are using object-oriented-programming to imitate San Francisco's traffic along Taylor, Jones and Pine St. 

We created 4 classes to make this simulation possible. The sample of the simulation, video and schema are available in this repo. 

### Classes Created 

#### Car 
Each car was stored as an object to a lane. This enabled us to measure the average time of the car throughout the entire system. Also, the car object determines whether it will turn in intersections or not. 


#### Lane 
Lane objects are basically the segments of the street that are before or after intersections. There are two types of lanes: inflow and outflow (Pine St. B is an exception). This object also performs movements amongst cars in the system. 

#### Lane Connection 
Lane Connection is a set of lanes where a car can potentially go. This also enabled the simulation of traffic light rules in the system. 

#### Traffic System 
The traffic system is the main body of the simulation where the movements in the lanes, intersections and traffic lights occur.  All objects are stored in this system. 
