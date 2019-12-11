# Summary

## Abstract
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。

## Parameter
constitutive_eq.type: Shear_Navier_Stokes

shrear_rate: 0.0
janus_slip_vel: 0.05
janus_slip_mode: 0.5

- changed parameters
fix_cell.x: 'OFF' <- 'ON'
fix_cell.y: 'OFF' <- 'ON'
fix_cell.z: 'OFF' <- 'ON'