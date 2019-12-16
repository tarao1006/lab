# Summary

## Abstract
B2の値を保持しながら、B1の値を小さくし、shear_stressに対して上むきの動きがどのような影響を与えているのかを調べるシミュレーションです。sim11と比較すると、fix_cellの値がONになっています。

## Parameter
|param|new value|old value|
|:-:|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.0|-|
|janus_slip_vel|0.001|-|
|janus_slip_mode|50|0.5|
|fix_cell.x|ON|OFF|
|fix_cell.y|ON|OFF|
|fix_cell.z|ON|OFF|
