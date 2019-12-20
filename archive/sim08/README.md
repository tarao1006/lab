# Summary

## Abstract
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。新たに行なったシミュレーションの結果が想定される結果ではなかったので、過去に用いたudfファイルを用いてシミュレーションを行います。

## Parameter
|param|new value|old value|
|:-:|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.0|-|
|janus_slip_vel|0.05|-|
|janus_slip_mode|0.5|-|
|fix_cell.x|ON|-|
|fix_cell.y|ON|-|
|fix_cell.z|ON|-|

