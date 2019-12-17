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
## sim00 ~ sim03, sim05 ~ sim12
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。free_rigidをYESに設定しているシミュレーションは、おそらく計算結果がよくないです。また、sim07/sim08とsim13/sim14は、分割数のみの違いです。グラフを比較した結果、free_rigidの値は結果に影響を与えないことが分かった。

|param          |sim00/sim01|sim02/sim03|sim05/sim06|sim07/sim08|sim09/sim10|sim11/sim12|sim13/sim14|
|:-:            |        :-:|        :-:|        :-:|        :-:|        :-:|        :-:|        :-:|
|shrear_rate    |        0.0|        0.0|      0.001|        0.0|        0.0|        0.0|        0.0|
|janus_slip_vel |   0.1/0.05|   0.1/0.05|        0.1|   0.1/0.05|   0.1/0.05|      0.001|   0.1/0.05|
|janus_slip_mode|        0.5|        0.5|        0.5|        0.5|        0.5|         50|        0.5|
|free_rigid     |        YES|        YES|        YES|         NO|         NO|         NO|         NO|
|fix_cell       |        OFF|         ON|     OFF/ON|         ON|        OFF|     OFF/ON|         ON|

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
