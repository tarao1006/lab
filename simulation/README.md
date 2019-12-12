# Simulation

# Usage
```
qsub -N job -o std.out -e std.err -v SIM_NUM=1 -v MAX_COUNT=8 -v IS_FIRST=1 -q uni1.q job.sh
```
環境変数を用いて、コマンドライン引数をpythonに渡します。

|値|型|概要|
|:-:|:-:|:-:|
|SIM_NUM|int (0~9)|ディレクトリの番号|
|MAX_COUNT|int|一つのジョブで担当するシミュレーションの最大数|
|IS_FIRST|bool|初回の実行かどうか。初回の場合、ディレクトリのリストを作成します。|

# Summary
## sim00
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。

|param|value|
|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.0|
|janus_slip_vel|0.1|
|janus_slip_mode|0.5|

## sim01
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。

|param|value|
|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.0|
|janus_slip_vel|0.05|
|janus_slip_mode|0.5|

## sim02
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。sim00との比較用で、fix_cellをONにした場合とOFFの違いを調べます。

|param|value|
|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.0|
|janus_slip_vel|0.1|
|janus_slip_mode|0.5|

## sim03
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。sim01との比較用で、fix_cellをONにした場合とOFFの違いを調べます。

|param|value|
|:-:|:-:|
|constitutive_eq.type|Shear_Navier_Stokes|
|shrear_rate|0.0|
|janus_slip_vel|0.05|
|janus_slip_mode|0.5|