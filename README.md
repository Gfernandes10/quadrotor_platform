# Quadrotor Platform Project

## General Overview

## MIL (Model-in-the-loop)
### Plant
- 🔵 (planned) - [Tunning of generic inner loop PID](#86a6xcb9t)
- 🔵 (planned) - [Make ground-truth available](#86a6xccjf)
- 🔵 (planned) - [Finalize plant component](#86a6xcd7r)
- 🔵 (planned) - [Create linear models for futher systems identification and inner loop PID gains tuning](#86a6xcdxm)
- ⚪ (Open) - [Identify linear model based on real drone experiments](#86a6xd1k7)
- ⚪ (Open) - [Adjust inner loop PID based on real drones experiments](#86a6xdjdr)
- ⚪ (Open) - [Compare model identified with other real experiments](#86a6xdjv8)
- ⚪ (Open) - [Create operation states for possible control (taking-off, landed, landing, etc)](#86a6xdp45)
- ⚪ (Open) - [Verify if model's interface matches with real hardware](#86a6xegnc)
### Sensor
- ⚪ (Open) - [Create IMU model](#86a6xe7cj)
- ⚪ (Open) - [Create barometer model](#86a6xe8eb)
- ⚪ (Open) - [Create camera model](#86a6xekhk)
### Localization
- ⚪ (Open) - [Simulate tag localization package](#86a6xerkw)
- ⚪ (Open) - [Simulate opt-track localization package](#86a6xetmy)
- ⚪ (Open) - [Simulate ORB-SLAM package](#86a6xev6b)
- ⚪ (Open) - [Investigate machine learning techniques for localization](#86a6xewb4)
### Control
- ⚪ (Open) - [Implement PID position control](#86a6xf114)
- ⚪ (Open) - [Implement LQR position control](#86a6xf1r3)
- ⚪ (Open) - [Implement Model Preditive Control](#86a6xf3ta)
- ⚪ (Open) - [Investigate machine learning technique for control](#86a6xf81u)
### Path planning
- ⚪ (Open) - [React to gesture commands](#86a6xfu20)
- ⚪ (Open) - [React to auditive commands](#86a6xfv5x)
- ⚪ (Open) - [investigate object detection techniques](#86a6xfvrb)
- ⚪ (Open) - [Investigate object search for techniques](#86a6xfw1u)

## SIL (Software-in-the-loop)
### Plant
- ⚪ (Open) - [Create robot description](#86a6xguax)
- ⚪ (Open) - [Create gazebo plugin based on MIL plant model](#86a6xguge)
- ⚪ (Open) - [Compare experiments with MIL and real experiments](#86a6xgutf)
### Sensor
- ⚪ (Open) - [Add IMU sensor gazebo plugins to robot](#86a6xgum9)
- ⚪ (Open) - [Add barometer sensor gazebo plugin to robot](#86a6xgxuz)
- ⚪ (Open) - [Add camera sensor gazebo plugin to robot](#86a6xgxyc)

## HIL (Hardware-in-the-loop)
### Plant
- ⚪ (Open) - [Summarize available interface with Tello Drone](#86a6xh29e)
- ⚪ (Open) - [Create basic interface to send and receive commands from/to the drone](#86a6xh2eh)
- ⚪ (Open) - [Define experiments to model identification](#86a6xh2m8)
- ⚪ (Open) - [Apply model identification experiments and save data](#86a6xh2t8)

## Summary

## MIL (Model-in-the-loop)
### Plant
<a id='86a6xcb9t'></a>
#### <ins>Tunning of generic inner loop PID</ins>
###### Platform: MIL | Component: Plant | Time spent: 1m
teste




<a id='86a6xccjf'></a>
#### <ins>Make ground-truth available</ins>
###### Platform: MIL | Component: Plant | Time spent: 
Disponibilizar ground-truth


<a id='86a6xcd7r'></a>
#### <ins>Finalize plant component</ins>
###### Platform: MIL | Component: Plant | Time spent: 
finalizar bloco da planta


<a id='86a6xcdxm'></a>
#### <ins>Create linear models for futher systems identification and inner loop PID gains tuning</ins>
###### Platform: MIL | Component: Plant | Time spent: 
Criar os modelos lineares para identificação e ajuste dos ganhos PID


<a id='86a6xd1k7'></a>
#### <ins>Identify linear model based on real drone experiments</ins>
###### Platform: MIL | Component: Plant | Time spent: 
Levantar modelo linear com base em experimentos com drone real


<a id='86a6xdjdr'></a>
#### <ins>Adjust inner loop PID based on real drones experiments</ins>
###### Platform: MIL | Component: Plant | Time spent: 
Ajustar controladores com base no hardware


<a id='86a6xdjv8'></a>
#### <ins>Compare model identified with other real experiments</ins>
###### Platform: MIL | Component: Plant | Time spent: 
Comparar o modelo corrigido com experimentos reais 


<a id='86a6xdp45'></a>
#### <ins>Create operation states for possible control (taking-off, landed, landing, etc)</ins>
###### Platform: MIL | Component: Plant | Time spent: 
Criar estados de operação para possível controle (voando, pousado, taking off, etc)


<a id='86a6xegnc'></a>
#### <ins>Verify if model's interface matches with real hardware</ins>
###### Platform: MIL | Component: Plant | Time spent: 
Verify if model's interface matches with real hardware


### Sensor
<a id='86a6xe7cj'></a>
#### <ins>Create IMU model</ins>
###### Platform: MIL | Component: Sensor | Time spent: 
Criar modelo de IMU


<a id='86a6xe8eb'></a>
#### <ins>Create barometer model</ins>
###### Platform: MIL | Component: Sensor | Time spent: 
Criar modelo de barômetro


<a id='86a6xekhk'></a>
#### <ins>Create camera model</ins>
###### Platform: MIL | Component: Sensor | Time spent: 
Create camera model


### Localization
<a id='86a6xerkw'></a>
#### <ins>Simulate tag localization package</ins>
###### Platform: MIL | Component: Localization | Time spent: 
Localização por tag


<a id='86a6xetmy'></a>
#### <ins>Simulate opt-track localization package</ins>
###### Platform: MIL | Component: Localization | Time spent: 
Opt-track


<a id='86a6xev6b'></a>
#### <ins>Simulate ORB-SLAM package</ins>
###### Platform: MIL | Component: Localization | Time spent: 
ORB-SLAM


<a id='86a6xewb4'></a>
#### <ins>Investigate machine learning techniques for localization</ins>
###### Platform: MIL | Component: Localization | Time spent: 
Investigar técnicas avançadas de ML para localização


### Control
<a id='86a6xf114'></a>
#### <ins>Implement PID position control</ins>
###### Platform: MIL | Component: Control | Time spent: 
PID



<a id='86a6xf1r3'></a>
#### <ins>Implement LQR position control</ins>
###### Platform: MIL | Component: Control | Time spent: 
LQR


<a id='86a6xf3ta'></a>
#### <ins>Implement Model Preditive Control</ins>
###### Platform: MIL | Component: Control | Time spent: 
MPC


<a id='86a6xf81u'></a>
#### <ins>Investigate machine learning technique for control</ins>
###### Platform: MIL | Component: Control | Time spent: 
Tecnica de Machine Learning?


### Path planning
<a id='86a6xfu20'></a>
#### <ins>React to gesture commands</ins>
###### Platform: MIL | Component: Path planning | Time spent: 
Reagir a comandos visuais ou gestuais


<a id='86a6xfv5x'></a>
#### <ins>React to auditive commands</ins>
###### Platform: MIL | Component: Path planning | Time spent: 
Reagir a comandos auditivos


<a id='86a6xfvrb'></a>
#### <ins>investigate object detection techniques</ins>
###### Platform: MIL | Component: Path planning | Time spent: 
Implementar técnica de identificação de objetos


<a id='86a6xfw1u'></a>
#### <ins>Investigate object search for techniques</ins>
###### Platform: MIL | Component: Path planning | Time spent: 
Implementar técnica de procurar por objeto


## SIL (Software-in-the-loop)
### Plant
<a id='86a6xguax'></a>
#### <ins>Create robot description</ins>
###### Platform: SIL | Component: Plant | Time spent: 
Create robot description


<a id='86a6xguge'></a>
#### <ins>Create gazebo plugin based on MIL plant model</ins>
###### Platform: SIL | Component: Plant | Time spent: 
Create gazebo plugin based on MIL plant model


<a id='86a6xgutf'></a>
#### <ins>Compare experiments with MIL and real experiments</ins>
###### Platform: SIL | Component: Plant | Time spent: 
Compare experiments with MIL and real experiments


### Sensor
<a id='86a6xgum9'></a>
#### <ins>Add IMU sensor gazebo plugins to robot</ins>
###### Platform: SIL | Component: Sensor | Time spent: 
Add sensor gazebo plugins to robot


<a id='86a6xgxuz'></a>
#### <ins>Add barometer sensor gazebo plugin to robot</ins>
###### Platform: SIL | Component: Sensor | Time spent: 
Add barometer sensor gazebo plugin to robot


<a id='86a6xgxyc'></a>
#### <ins>Add camera sensor gazebo plugin to robot</ins>
###### Platform: SIL | Component: Sensor | Time spent: 
Add camera sensor gazebo plugin to robot


## HIL (Hardware-in-the-loop)
### Plant
<a id='86a6xh29e'></a>
#### <ins>Summarize available interface with Tello Drone</ins>
###### Platform: HIL | Component: Plant | Time spent: 
Summarize available interface with Tello Drone


<a id='86a6xh2eh'></a>
#### <ins>Create basic interface to send and receive commands from/to the drone</ins>
###### Platform: HIL | Component: Plant | Time spent: 
Create basic interface to send and receive commands from/to the drone


<a id='86a6xh2m8'></a>
#### <ins>Define experiments to model identification</ins>
###### Platform: HIL | Component: Plant | Time spent: 
Define experiments to model identification


<a id='86a6xh2t8'></a>
#### <ins>Apply model identification experiments and save data</ins>
###### Platform: HIL | Component: Plant | Time spent: 
Apply model identification experiments and save data


