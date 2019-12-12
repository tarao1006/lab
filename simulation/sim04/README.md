# Summary

## Abstract
shear_rateの値とjanus_slip_velの値を変化させた時に、z軸方向の回転がどのような値になるのかを調べるシミュレーションです。

## Parameter
|param|new value|old value|
|:-:|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.05 ~ 0.1|-|
|janus_slip_vel|0.0, 0.05 ~ 0.1|-|
|janus_slip_mode|0.5|-|
|fix_cell.x|ON|-|
|fix_cell.y|ON|-|
|fix_cell.z|ON|-|
|pin|NO|-|

### sim04-00
|param|value|
|:-:|:-:|
|shrear_rate|0.05|
|janus_slip_vel|0.0, 0.05 ~ 0.1|

### sim04-01
|param|value|
|:-:|:-:|
|shrear_rate|0.06|
|janus_slip_vel|0.0, 0.05 ~ 0.1|

### sim04-02
|param|value|
|:-:|:-:|
|shrear_rate|0.07|
|janus_slip_vel|0.0, 0.05 ~ 0.1|

### sim04-03
|param|value|
|:-:|:-:|
|shrear_rate|0.08|
|janus_slip_vel|0.0, 0.05 ~ 0.1|

### sim04-04
|param|value|
|:-:|:-:|
|shrear_rate|0.09|
|janus_slip_vel|0.0, 0.05 ~ 0.1|

### sim04-05
|param|value|
|:-:|:-:|
|shrear_rate|0.1|
|janus_slip_vel|0.0, 0.05 ~ 0.1|
