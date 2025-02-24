# Quadrotor Platform Project

## General Overview

### MIL (Model-in-the-loop)
#### Plant
- 🔵 (planned) - [Tunning of generic inner loop PID](#86a6xcb9t)
- 🔵 (planned) - [Make ground-truth available](#86a6xccjf)
- 🔵 (planned) - [Finalize plant component](#86a6xcd7r)
- 🔵 (planned) - [Create linear models for futher systems identification and inner loop PID gains tuning](#86a6xcdxm)
- ⚪ (Open) - [Identify linear model based on real drone experiments](#86a6xd1k7)
- ⚪ (Open) - [Adjust inner loop PID based on real drones experiments](#86a6xdjdr)
- ⚪ (Open) - [Compare model identified with other real experiments](#86a6xdjv8)
- ⚪ (Open) - [Create operation states for possible control (taking-off, landed, landing, etc)](#86a6xdp45)
- ⚪ (Open) - [Verify if model's interface matches with real hardware](#86a6xegnc)
#### Sensor
- ⚪ (Open) - [Create IMU model](#86a6xe7cj)
- ⚪ (Open) - [Create barometer model](#86a6xe8eb)
- ⚪ (Open) - [Create camera model](#86a6xekhk)
#### Localization
- ⚪ (Open) - [Simulate tag localization package](#86a6xerkw)
- ⚪ (Open) - [Simulate opt-track localization package](#86a6xetmy)
- ⚪ (Open) - [Simulate ORB-SLAM package](#86a6xev6b)
- ⚪ (Open) - [Investigate machine learning techniques for localization](#86a6xewb4)
#### Control
- ⚪ (Open) - [Implement PID position control](#86a6xf114)
- ⚪ (Open) - [Implement LQR position control](#86a6xf1r3)
- ⚪ (Open) - [Implement Model Preditive Control](#86a6xf3ta)
- ⚪ (Open) - [Investigate machine learning technique for control](#86a6xf81u)
#### Path planning
- ⚪ (Open) - [React to gesture commands](#86a6xfu20)
- ⚪ (Open) - [React to auditive commands](#86a6xfv5x)
- ⚪ (Open) - [investigate object detection techniques](#86a6xfvrb)
- ⚪ (Open) - [Investigate object search for techniques](#86a6xfw1u)

### SIL (Software-in-the-loop)
#### Plant
- ⚪ (Open) - [Create robot description](#86a6xguax)
- ⚪ (Open) - [Create gazebo plugin based on MIL plant model](#86a6xguge)
- ⚪ (Open) - [Compare experiments with MIL and real experiments](#86a6xgutf)
#### Sensor
- ⚪ (Open) - [Add IMU sensor gazebo plugins to robot](#86a6xgum9)
- ⚪ (Open) - [Add barometer sensor gazebo plugin to robot](#86a6xgxuz)
- ⚪ (Open) - [Add camera sensor gazebo plugin to robot](#86a6xgxyc)

### HIL (Hardware-in-the-loop)
#### Plant
- ⚪ (Open) - [Summarize available interface with Tello Drone](#86a6xh29e)
- ⚪ (Open) - [Create basic interface to send and receive commands from/to the drone](#86a6xh2eh)
- ⚪ (Open) - [Define experiments to model identification](#86a6xh2m8)
- ⚪ (Open) - [Apply model identification experiments and save data](#86a6xh2t8)

## Summary

## MIL
### Plant
<a id='86a6xcb9t'></a>
#### Tunning of generic inner loop PID
teste




<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 1m
</div>

<a id='86a6xccjf'></a>
#### Make ground-truth available
Disponibilizar ground-truth


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 
</div>

<a id='86a6xcd7r'></a>
#### Finalize plant component
finalizar bloco da planta


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 
</div>

<a id='86a6xcdxm'></a>
#### Create linear models for futher systems identification and inner loop PID gains tuning
Criar os modelos lineares para identificação e ajuste dos ganhos PID


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 
</div>

<a id='86a6xd1k7'></a>
#### Identify linear model based on real drone experiments
Levantar modelo linear com base em experimentos com drone real


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 
</div>

<a id='86a6xdjdr'></a>
#### Adjust inner loop PID based on real drones experiments
Ajustar controladores com base no hardware


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 
</div>

<a id='86a6xdjv8'></a>
#### Compare model identified with other real experiments
Comparar o modelo corrigido com experimentos reais 


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 
</div>

<a id='86a6xdp45'></a>
#### Create operation states for possible control (taking-off, landed, landing, etc)
Criar estados de operação para possível controle (voando, pousado, taking off, etc)


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 
</div>

<a id='86a6xegnc'></a>
#### Verify if model's interface matches with real hardware
Verify if model's interface matches with real hardware


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Plant | Time spent: 
</div>

### Sensor
<a id='86a6xe7cj'></a>
#### Create IMU model
Criar modelo de IMU


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Sensor | Time spent: 
</div>

<a id='86a6xe8eb'></a>
#### Create barometer model
Criar modelo de barômetro


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Sensor | Time spent: 
</div>

<a id='86a6xekhk'></a>
#### Create camera model
Create camera model


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Sensor | Time spent: 
</div>

### Localization
<a id='86a6xerkw'></a>
#### Simulate tag localization package
Localização por tag


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Localization | Time spent: 
</div>

<a id='86a6xetmy'></a>
#### Simulate opt-track localization package
Opt-track


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Localization | Time spent: 
</div>

<a id='86a6xev6b'></a>
#### Simulate ORB-SLAM package
ORB-SLAM


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Localization | Time spent: 
</div>

<a id='86a6xewb4'></a>
#### Investigate machine learning techniques for localization
Investigar técnicas avançadas de ML para localização


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Localization | Time spent: 
</div>

### Control
<a id='86a6xf114'></a>
#### Implement PID position control
PID



<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Control | Time spent: 
</div>

<a id='86a6xf1r3'></a>
#### Implement LQR position control
LQR


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Control | Time spent: 
</div>

<a id='86a6xf3ta'></a>
#### Implement Model Preditive Control
MPC


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Control | Time spent: 
</div>

<a id='86a6xf81u'></a>
#### Investigate machine learning technique for control
Tecnica de Machine Learning?


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Control | Time spent: 
</div>

### Path planning
<a id='86a6xfu20'></a>
#### React to gesture commands
Reagir a comandos visuais ou gestuais


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Path planning | Time spent: 
</div>

<a id='86a6xfv5x'></a>
#### React to auditive commands
Reagir a comandos auditivos


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Path planning | Time spent: 
</div>

<a id='86a6xfvrb'></a>
#### investigate object detection techniques
Implementar técnica de identificação de objetos


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Path planning | Time spent: 
</div>

<a id='86a6xfw1u'></a>
#### Investigate object search for techniques
Implementar técnica de procurar por objeto


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: MIL | Component: Path planning | Time spent: 
</div>

## SIL
### Plant
<a id='86a6xguax'></a>
#### Create robot description
Create robot description


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: SIL | Component: Plant | Time spent: 
</div>

<a id='86a6xguge'></a>
#### Create gazebo plugin based on MIL plant model
Create gazebo plugin based on MIL plant model


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: SIL | Component: Plant | Time spent: 
</div>

<a id='86a6xgutf'></a>
#### Compare experiments with MIL and real experiments
Compare experiments with MIL and real experiments


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: SIL | Component: Plant | Time spent: 
</div>

### Sensor
<a id='86a6xgum9'></a>
#### Add IMU sensor gazebo plugins to robot
Add sensor gazebo plugins to robot


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: SIL | Component: Sensor | Time spent: 
</div>

<a id='86a6xgxuz'></a>
#### Add barometer sensor gazebo plugin to robot
Add barometer sensor gazebo plugin to robot


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: SIL | Component: Sensor | Time spent: 
</div>

<a id='86a6xgxyc'></a>
#### Add camera sensor gazebo plugin to robot
Add camera sensor gazebo plugin to robot


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: SIL | Component: Sensor | Time spent: 
</div>

## HIL
### Plant
<a id='86a6xh29e'></a>
#### Summarize available interface with Tello Drone
Summarize available interface with Tello Drone


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: HIL | Component: Plant | Time spent: 
</div>

<a id='86a6xh2eh'></a>
#### Create basic interface to send and receive commands from/to the drone
Create basic interface to send and receive commands from/to the drone


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: HIL | Component: Plant | Time spent: 
</div>

<a id='86a6xh2m8'></a>
#### Define experiments to model identification
Define experiments to model identification


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: HIL | Component: Plant | Time spent: 
</div>

<a id='86a6xh2t8'></a>
#### Apply model identification experiments and save data
Apply model identification experiments and save data


<div style='color: gray; font-size: 0.8em; margin-bottom: 10px;'>
Platform: HIL | Component: Plant | Time spent: 
</div>

