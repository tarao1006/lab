# Summary

## Abstract
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。sim00でshear_rateを0.0に設定しましたが粘度がマイナスになったり、値が1からかけ離れたり、正常なシミュレーションが行えていないようなので、shear_rateと0.001としてシミュレーションを行なってみます。

## Parameter
|param|new value|old value|
|:-:|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.001|-|
|janus_slip_vel|0.1|-|
|janus_slip_mode|0.5|-|
|fix_cell.x|OFF|ON|
|fix_cell.y|OFF|ON|
|fix_cell.z|OFF|ON|
