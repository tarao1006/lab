# Summary

## Abstract
B2の値を保持しながら、B1の値を小さくし、shear_stressに対して上むきの動きがどのような影響を与えているのかを調べるシミュレーションです。

## Parameter
|param|new value|old value|
|:-:|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.0|-|
|janus_slip_vel|0.001|-|
|janus_slip_mode|50|0.5|
|fix_cell.x|OFF|ON|
|fix_cell.y|OFF|ON|
|fix_cell.z|OFF|ON|