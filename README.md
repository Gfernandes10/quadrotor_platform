# Quadrotor Platform Project

## General Overview

### MIL (Model-in-the-loop)
#### Plant
- [Tunning of generic inner loop PID](#86a6xcb9t) - <span style='color:blue;'>planned</span>
- [Make ground-truth available](#86a6xccjf) - <span style='color:blue;'>planned</span>
- [Finalize plant component](#86a6xcd7r) - <span style='color:blue;'>planned</span>
- [Create linear models for futher systems identification and inner loop PID gains tuning](#86a6xcdxm) - <span style='color:blue;'>planned</span>
- [Identify linear model based on real drone experiments](#86a6xd1k7) - <span style='color:gray;'>Open</span>
- [Adjust inner loop PID based on real drones experiments](#86a6xdjdr) - <span style='color:gray;'>Open</span>
- [Compare model identified with other real experiments](#86a6xdjv8) - <span style='color:gray;'>Open</span>
- [Create operation states for possible control (taking-off, landed, landing, etc)](#86a6xdp45) - <span style='color:gray;'>Open</span>
- [Verify if model's interface matches with real hardware](#86a6xegnc) - <span style='color:gray;'>Open</span>
#### Sensor
- [Create IMU model](#86a6xe7cj) - <span style='color:gray;'>Open</span>
- [Create barometer model](#86a6xe8eb) - <span style='color:gray;'>Open</span>
- [Create camera model](#86a6xekhk) - <span style='color:gray;'>Open</span>
#### Localization
- [Simulate tag localization package](#86a6xerkw) - <span style='color:gray;'>Open</span>
- [Simulate opt-track localization package](#86a6xetmy) - <span style='color:gray;'>Open</span>
- [Simulate ORB-SLAM package](#86a6xev6b) - <span style='color:gray;'>Open</span>
- [Investigate machine learning techniques for localization](#86a6xewb4) - <span style='color:gray;'>Open</span>
#### Control
- [Implement PID position control](#86a6xf114) - <span style='color:gray;'>Open</span>
- [Implement LQR position control](#86a6xf1r3) - <span style='color:gray;'>Open</span>
- [Implement Model Preditive Control](#86a6xf3ta) - <span style='color:gray;'>Open</span>
- [Investigate machine learning technique for control](#86a6xf81u) - <span style='color:gray;'>Open</span>
#### Path planning
- [React to gesture commands](#86a6xfu20) - <span style='color:gray;'>Open</span>
- [React to auditive commands](#86a6xfv5x) - <span style='color:gray;'>Open</span>
- [investigate object detection techniques](#86a6xfvrb) - <span style='color:gray;'>Open</span>
- [Investigate object search for techniques](#86a6xfw1u) - <span style='color:gray;'>Open</span>

### SIL (Software-in-the-loop)
#### Plant
- [Create robot description](#86a6xguax) - <span style='color:gray;'>Open</span>
- [Create gazebo plugin based on MIL plant model](#86a6xguge) - <span style='color:gray;'>Open</span>
- [Compare experiments with MIL and real experiments](#86a6xgutf) - <span style='color:gray;'>Open</span>
#### Sensor
- [Add IMU sensor gazebo plugins to robot](#86a6xgum9) - <span style='color:gray;'>Open</span>
- [Add barometer sensor gazebo plugin to robot](#86a6xgxuz) - <span style='color:gray;'>Open</span>
- [Add camera sensor gazebo plugin to robot](#86a6xgxyc) - <span style='color:gray;'>Open</span>

### HIL (Hardware-in-the-loop)
#### Plant
- [Summarize available interface with Tello Drone](#86a6xh29e) - <span style='color:gray;'>Open</span>
- [Create basic interface to send and receive commands from/to the drone](#86a6xh2eh) - <span style='color:gray;'>Open</span>
- [Define experiments to model identification](#86a6xh2m8) - <span style='color:gray;'>Open</span>
- [Apply model identification experiments and save data](#86a6xh2t8) - <span style='color:gray;'>Open</span>

## Summary

### MIL
#### Plant
<a id='86a6xcb9t'></a>
##### Tunning of generic inner loop PID
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 1m
</div>
**Description:**
teste




<a id='86a6xccjf'></a>
##### Make ground-truth available
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Disponibilizar ground-truth


<a id='86a6xcd7r'></a>
##### Finalize plant component
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
finalizar bloco da planta


<a id='86a6xcdxm'></a>
##### Create linear models for futher systems identification and inner loop PID gains tuning
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Criar os modelos lineares para identificação e ajuste dos ganhos PID


<a id='86a6xd1k7'></a>
##### Identify linear model based on real drone experiments
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Levantar modelo linear com base em experimentos com drone real


<a id='86a6xdjdr'></a>
##### Adjust inner loop PID based on real drones experiments
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Ajustar controladores com base no hardware


<a id='86a6xdjv8'></a>
##### Compare model identified with other real experiments
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Comparar o modelo corrigido com experimentos reais 


<a id='86a6xdp45'></a>
##### Create operation states for possible control (taking-off, landed, landing, etc)
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Criar estados de operação para possível controle (voando, pousado, taking off, etc)


<a id='86a6xegnc'></a>
##### Verify if model's interface matches with real hardware
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Verify if model's interface matches with real hardware


#### Sensor
<a id='86a6xe7cj'></a>
##### Create IMU model
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Sensor | <strong>Time spent:</strong> 
</div>
**Description:**
Criar modelo de IMU


<a id='86a6xe8eb'></a>
##### Create barometer model
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Sensor | <strong>Time spent:</strong> 
</div>
**Description:**
Criar modelo de barômetro


<a id='86a6xekhk'></a>
##### Create camera model
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Sensor | <strong>Time spent:</strong> 
</div>
**Description:**
Create camera model


#### Localization
<a id='86a6xerkw'></a>
##### Simulate tag localization package
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Localization | <strong>Time spent:</strong> 
</div>
**Description:**
Localização por tag


<a id='86a6xetmy'></a>
##### Simulate opt-track localization package
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Localization | <strong>Time spent:</strong> 
</div>
**Description:**
Opt-track


<a id='86a6xev6b'></a>
##### Simulate ORB-SLAM package
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Localization | <strong>Time spent:</strong> 
</div>
**Description:**
ORB-SLAM


<a id='86a6xewb4'></a>
##### Investigate machine learning techniques for localization
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Localization | <strong>Time spent:</strong> 
</div>
**Description:**
Investigar técnicas avançadas de ML para localização


#### Control
<a id='86a6xf114'></a>
##### Implement PID position control
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Control | <strong>Time spent:</strong> 
</div>
**Description:**
PID



<a id='86a6xf1r3'></a>
##### Implement LQR position control
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Control | <strong>Time spent:</strong> 
</div>
**Description:**
LQR


<a id='86a6xf3ta'></a>
##### Implement Model Preditive Control
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Control | <strong>Time spent:</strong> 
</div>
**Description:**
MPC


<a id='86a6xf81u'></a>
##### Investigate machine learning technique for control
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Control | <strong>Time spent:</strong> 
</div>
**Description:**
Tecnica de Machine Learning?


#### Path planning
<a id='86a6xfu20'></a>
##### React to gesture commands
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Path planning | <strong>Time spent:</strong> 
</div>
**Description:**
Reagir a comandos visuais ou gestuais


<a id='86a6xfv5x'></a>
##### React to auditive commands
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Path planning | <strong>Time spent:</strong> 
</div>
**Description:**
Reagir a comandos auditivos


<a id='86a6xfvrb'></a>
##### investigate object detection techniques
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Path planning | <strong>Time spent:</strong> 
</div>
**Description:**
Implementar técnica de identificação de objetos


<a id='86a6xfw1u'></a>
##### Investigate object search for techniques
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> MIL | <strong>Component:</strong> Path planning | <strong>Time spent:</strong> 
</div>
**Description:**
Implementar técnica de procurar por objeto


### SIL
#### Plant
<a id='86a6xguax'></a>
##### Create robot description
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> SIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Create robot description


<a id='86a6xguge'></a>
##### Create gazebo plugin based on MIL plant model
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> SIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Create gazebo plugin based on MIL plant model


<a id='86a6xgutf'></a>
##### Compare experiments with MIL and real experiments
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> SIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Compare experiments with MIL and real experiments


#### Sensor
<a id='86a6xgum9'></a>
##### Add IMU sensor gazebo plugins to robot
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> SIL | <strong>Component:</strong> Sensor | <strong>Time spent:</strong> 
</div>
**Description:**
Add sensor gazebo plugins to robot


<a id='86a6xgxuz'></a>
##### Add barometer sensor gazebo plugin to robot
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> SIL | <strong>Component:</strong> Sensor | <strong>Time spent:</strong> 
</div>
**Description:**
Add barometer sensor gazebo plugin to robot


<a id='86a6xgxyc'></a>
##### Add camera sensor gazebo plugin to robot
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> SIL | <strong>Component:</strong> Sensor | <strong>Time spent:</strong> 
</div>
**Description:**
Add camera sensor gazebo plugin to robot


### HIL
#### Plant
<a id='86a6xh29e'></a>
##### Summarize available interface with Tello Drone
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> HIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Summarize available interface with Tello Drone


<a id='86a6xh2eh'></a>
##### Create basic interface to send and receive commands from/to the drone
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> HIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Create basic interface to send and receive commands from/to the drone


<a id='86a6xh2m8'></a>
##### Define experiments to model identification
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> HIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Define experiments to model identification


<a id='86a6xh2t8'></a>
##### Apply model identification experiments and save data
<div style='color: gray; font-size: 0.9em; margin-bottom: 10px;'>
<strong>Platform:</strong> HIL | <strong>Component:</strong> Plant | <strong>Time spent:</strong> 
</div>
**Description:**
Apply model identification experiments and save data


