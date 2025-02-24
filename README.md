# Quadrotor Platform Project

## General Overview

### MIL (Model-in-the-loop)
#### Plant
- [Tunning of generic inner loop PID](#86a6xcb9t) - planned
- [Make ground-truth available](#86a6xccjf) - planned
- [Finalize plant component](#86a6xcd7r) - planned
- [Create linear models for futher systems identification and inner loop PID gains tuning](#86a6xcdxm) - planned
- [Identify linear model based on real drone experiments](#86a6xd1k7) - Open
- [Adjust inner loop PID based on real drones experiments](#86a6xdjdr) - Open
- [Compare model identified with other real experiments](#86a6xdjv8) - Open
- [Create operation states for possible control (taking-off, landed, landing, etc)](#86a6xdp45) - Open
- [Verify if model's interface matches with real hardware](#86a6xegnc) - Open
#### Sensor
- [Create IMU model](#86a6xe7cj) - Open
- [Create barometer model](#86a6xe8eb) - Open
- [Create camera model](#86a6xekhk) - Open
#### Localization
- [Simulate tag localization package](#86a6xerkw) - Open
- [Simulate opt-track localization package](#86a6xetmy) - Open
- [Simulate ORB-SLAM package](#86a6xev6b) - Open
- [Investigate machine learning techniques for localization](#86a6xewb4) - Open
#### Control
- [Implement PID position control](#86a6xf114) - Open
- [Implement LQR position control](#86a6xf1r3) - Open
- [Implement Model Preditive Control](#86a6xf3ta) - Open
- [Investigate machine learning technique for control](#86a6xf81u) - Open
#### Path planning
- [React to gesture commands](#86a6xfu20) - Open
- [React to auditive commands](#86a6xfv5x) - Open
- [investigate object detection techniques](#86a6xfvrb) - Open
- [Investigate object search for techniques](#86a6xfw1u) - Open

### SIL (Software-in-the-loop)
#### Plant
- [Create robot description](#86a6xguax) - Open
- [Create gazebo plugin based on MIL plant model](#86a6xguge) - Open
- [Compare experiments with MIL and real experiments](#86a6xgutf) - Open
#### Sensor
- [Add IMU sensor gazebo plugins to robot](#86a6xgum9) - Open
- [Add barometer sensor gazebo plugin to robot](#86a6xgxuz) - Open
- [Add camera sensor gazebo plugin to robot](#86a6xgxyc) - Open

### HIL (Hardware-in-the-loop)
#### Plant
- [Summarize available interface with Tello Drone](#86a6xh29e) - Open
- [Create basic interface to send and receive commands from/to the drone](#86a6xh2eh) - Open
- [Define experiments to model identification](#86a6xh2m8) - Open
- [Apply model identification experiments and save data](#86a6xh2t8) - Open

## Summary

### MIL
#### Plant
<a id='86a6xcb9t'></a>
##### Tunning of generic inner loop PID
**Time spent:** 1m
**Platform:** MIL
**Component:** Plant
**Description:** teste




<a id='86a6xccjf'></a>
##### Make ground-truth available
**Time spent:** 
**Platform:** MIL
**Component:** Plant
**Description:** Disponibilizar ground-truth


<a id='86a6xcd7r'></a>
##### Finalize plant component
**Time spent:** 
**Platform:** MIL
**Component:** Plant
**Description:** finalizar bloco da planta


<a id='86a6xcdxm'></a>
##### Create linear models for futher systems identification and inner loop PID gains tuning
**Time spent:** 
**Platform:** MIL
**Component:** Plant
**Description:** Criar os modelos lineares para identificação e ajuste dos ganhos PID


<a id='86a6xd1k7'></a>
##### Identify linear model based on real drone experiments
**Time spent:** 
**Platform:** MIL
**Component:** Plant
**Description:** Levantar modelo linear com base em experimentos com drone real


<a id='86a6xdjdr'></a>
##### Adjust inner loop PID based on real drones experiments
**Time spent:** 
**Platform:** MIL
**Component:** Plant
**Description:** Ajustar controladores com base no hardware


<a id='86a6xdjv8'></a>
##### Compare model identified with other real experiments
**Time spent:** 
**Platform:** MIL
**Component:** Plant
**Description:** Comparar o modelo corrigido com experimentos reais 


<a id='86a6xdp45'></a>
##### Create operation states for possible control (taking-off, landed, landing, etc)
**Time spent:** 
**Platform:** MIL
**Component:** Plant
**Description:** Criar estados de operação para possível controle (voando, pousado, taking off, etc)


<a id='86a6xegnc'></a>
##### Verify if model's interface matches with real hardware
**Time spent:** 
**Platform:** MIL
**Component:** Plant
**Description:** Verify if model's interface matches with real hardware


#### Sensor
<a id='86a6xe7cj'></a>
##### Create IMU model
**Time spent:** 
**Platform:** MIL
**Component:** Sensor
**Description:** Criar modelo de IMU


<a id='86a6xe8eb'></a>
##### Create barometer model
**Time spent:** 
**Platform:** MIL
**Component:** Sensor
**Description:** Criar modelo de barômetro


<a id='86a6xekhk'></a>
##### Create camera model
**Time spent:** 
**Platform:** MIL
**Component:** Sensor
**Description:** Create camera model


#### Localization
<a id='86a6xerkw'></a>
##### Simulate tag localization package
**Time spent:** 
**Platform:** MIL
**Component:** Localization
**Description:** Localização por tag


<a id='86a6xetmy'></a>
##### Simulate opt-track localization package
**Time spent:** 
**Platform:** MIL
**Component:** Localization
**Description:** Opt-track


<a id='86a6xev6b'></a>
##### Simulate ORB-SLAM package
**Time spent:** 
**Platform:** MIL
**Component:** Localization
**Description:** ORB-SLAM


<a id='86a6xewb4'></a>
##### Investigate machine learning techniques for localization
**Time spent:** 
**Platform:** MIL
**Component:** Localization
**Description:** Investigar técnicas avançadas de ML para localização


#### Control
<a id='86a6xf114'></a>
##### Implement PID position control
**Time spent:** 
**Platform:** MIL
**Component:** Control
**Description:** PID



<a id='86a6xf1r3'></a>
##### Implement LQR position control
**Time spent:** 
**Platform:** MIL
**Component:** Control
**Description:** LQR


<a id='86a6xf3ta'></a>
##### Implement Model Preditive Control
**Time spent:** 
**Platform:** MIL
**Component:** Control
**Description:** MPC


<a id='86a6xf81u'></a>
##### Investigate machine learning technique for control
**Time spent:** 
**Platform:** MIL
**Component:** Control
**Description:** Tecnica de Machine Learning?


#### Path planning
<a id='86a6xfu20'></a>
##### React to gesture commands
**Time spent:** 
**Platform:** MIL
**Component:** Path planning
**Description:** Reagir a comandos visuais ou gestuais


<a id='86a6xfv5x'></a>
##### React to auditive commands
**Time spent:** 
**Platform:** MIL
**Component:** Path planning
**Description:** Reagir a comandos auditivos


<a id='86a6xfvrb'></a>
##### investigate object detection techniques
**Time spent:** 
**Platform:** MIL
**Component:** Path planning
**Description:** Implementar técnica de identificação de objetos


<a id='86a6xfw1u'></a>
##### Investigate object search for techniques
**Time spent:** 
**Platform:** MIL
**Component:** Path planning
**Description:** Implementar técnica de procurar por objeto


### SIL
#### Plant
<a id='86a6xguax'></a>
##### Create robot description
**Time spent:** 
**Platform:** SIL
**Component:** Plant
**Description:** Create robot description


<a id='86a6xguge'></a>
##### Create gazebo plugin based on MIL plant model
**Time spent:** 
**Platform:** SIL
**Component:** Plant
**Description:** Create gazebo plugin based on MIL plant model


<a id='86a6xgutf'></a>
##### Compare experiments with MIL and real experiments
**Time spent:** 
**Platform:** SIL
**Component:** Plant
**Description:** Compare experiments with MIL and real experiments


#### Sensor
<a id='86a6xgum9'></a>
##### Add IMU sensor gazebo plugins to robot
**Time spent:** 
**Platform:** SIL
**Component:** Sensor
**Description:** Add sensor gazebo plugins to robot


<a id='86a6xgxuz'></a>
##### Add barometer sensor gazebo plugin to robot
**Time spent:** 
**Platform:** SIL
**Component:** Sensor
**Description:** Add barometer sensor gazebo plugin to robot


<a id='86a6xgxyc'></a>
##### Add camera sensor gazebo plugin to robot
**Time spent:** 
**Platform:** SIL
**Component:** Sensor
**Description:** Add camera sensor gazebo plugin to robot


### HIL
#### Plant
<a id='86a6xh29e'></a>
##### Summarize available interface with Tello Drone
**Time spent:** 
**Platform:** HIL
**Component:** Plant
**Description:** Summarize available interface with Tello Drone


<a id='86a6xh2eh'></a>
##### Create basic interface to send and receive commands from/to the drone
**Time spent:** 
**Platform:** HIL
**Component:** Plant
**Description:** Create basic interface to send and receive commands from/to the drone


<a id='86a6xh2m8'></a>
##### Define experiments to model identification
**Time spent:** 
**Platform:** HIL
**Component:** Plant
**Description:** Define experiments to model identification


<a id='86a6xh2t8'></a>
##### Apply model identification experiments and save data
**Time spent:** 
**Platform:** HIL
**Component:** Plant
**Description:** Apply model identification experiments and save data


