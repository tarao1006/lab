# Simulation

# Usage
```
qsub -N job -o std.out -e std.err -v PICKLE_FILE="dirs.pickle" -v MAX_COUNT=8 -q uni1.q job.sh
```
環境変数を用いて、コマンドライン引数をpythonに渡します。

|値|型|概要|
|:-:|:-:|:-:|
|SIM_NUM|int (0~99)|ディレクトリの番号|
|MAX_COUNT|int|一つのジョブで担当するシミュレーションの最大数|
|IS_FIRST|bool|初回の実行かどうか。初回の場合、ディレクトリのリストを作成します。|

# Summary
## sim00 ~ sim03, sim05 ~ sim14
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。グラフを比較した結果、free_rigidの値は結果に影響を与えないようです。また、sim11/sim12を比較した時、fix_cellの違いはシミュレーション結果に影響を与えませんでした。sim07/sim08とsim13/sim14は、分割数のみの違いです。

|param          |sim00/sim01|sim02/sim03|sim05/sim06|sim07/sim08|sim09/sim10|sim11/sim12|sim13/sim14|
|:-:            |        :-:|        :-:|        :-:|        :-:|        :-:|        :-:|        :-:|
|shrear_rate    |        0.0|        0.0|      0.001|        0.0|        0.0|        0.0|        0.0|
|janus_slip_vel |   0.1/0.05|   0.1/0.05|        0.1|   0.1/0.05|   0.1/0.05|      0.001|   0.1/0.05|
|janus_slip_mode|        0.5|        0.5|        0.5|        0.5|        0.5|         50|        0.5|
|free_rigid     |        YES|        YES|        YES|         NO|         NO|         NO|         NO|
|fix_cell       |        OFF|         ON|     OFF/ON|         ON|        OFF|     OFF/ON|         ON|

## sim15
HDF5のテストの為のシミュレーションです。

|param          |sim15|
|:-:            |  :-:|
|shear_rate     |  0.0|
|janus_slip_vel |0.001|
|janus_slip_mode|   50|
|fix_cell       |   ON|

## sim16 (dmo00)
bottom heavyの影響を考えた計算が正しいかを確認するシミュレーションです。

|param          |sim16-00|sim16-01|sim16-02|
|:-:            |     :-:|     :-:|     :-:|
|gravity        |     1.0|     5.0|    10.0|
|shrear_rate    |     0.0|
|janus_slip_vel |   0.001|
|janus_slip_mode|      50|
|PIN            |      NO|
|free_rigid     |      NO|

## sim17
粒子の位置は固定し、回転方向だけを変化させられるかを確かめるシミュレーションです。

 |param          |sim17|
 |:-:            |  :-:|
 |gravity        |  0.0|
 |shear_rate     |  0.1|
 |janus_slip_vel |  0.1|
 |janus_slip_mode|  0.5|
 |PIN            |  YES|
 |free_rigid     |  YES|
 |fix_cell       |   ON|

## sim18
粒子の位置は固定し、回転方向だけを変化させられるかを確かめるシミュレーションです。

 |param          |sim17|
 |:-:            |  :-:|
 |gravity        |  0.0|
 |shear_rate     |  0.1|
 |janus_slip_vel |  0.1|
 |janus_slip_mode|  0.5|
 |PIN            |  YES|
 |free_rigid     |  YES|
 |fix_cell       |  OFF|

## sim18
粒子の位置は固定し、回転方向だけを変化させられるかを確かめるシミュレーションです。

 |param          |sim17|
 |:-:            |  :-:|
 |gravity        |  0.0|
 |shear_rate     |  0.1|
 |janus_slip_vel |  0.1|
 |janus_slip_mode|  0.5|
 |PIN            |   NO|
 |free_rigid     |  YES|
 |fix_cell       |   ON|

## sim04
shear_rateの値とjanus_slip_velの値を変化させた時に、z軸方向の回転がどのような値になるのかを調べるシミュレーションです。

|param          |          value|
|:-:            |            :-:|
|shrear_rate    |     0.05 ~ 0.1|
|janus_slip_vel |0.0, 0.05 ~ 0.1|
|janus_slip_mode|            0.5|
|PIN            |             NO|

### sim04-00 ~ sim04-05
|param         |       sim04-00|       sim04-01|       sim04-02|       sim04-03|       sim04-04|       sim04-05|
|:-:           |            :-:|            :-:|            :-:|            :-:|            :-:|            :-:|
|shrear_rate   |           0.05|           0.06|           0.07|           0.08|           0.09|           0.10|
