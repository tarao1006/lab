# Simulation

# Usage
```
qsub -N job -o std.out -e std.err -v PICKLE_FILE="dirs.pickle" -v MAX_COUNT=8 -q uni1.q job.sh
```
環境変数を用いて、コマンドライン引数をpythonに渡します。

|name       |type|optional|default|summary|
|:-:        |:-: |:-:     |:-:    |:-:    |
|PICKLE_FILE|str |optional|dirs.pickle|読み込むpickleファイルの名前|
|MAX_COUNT  |int |optional|4|一つのループで実行するシミュレーションの数|
|CMD        |str |optional|kapsel -Iinput.udf -Ooutput.udf -Ddefine.udf -Rrestart.udf|実行するコマンド|


# Main
## sim04
shear_rateの値とjanus_slip_velの値を変化させた時に、z軸方向の回転がどのような値になるのかを調べるシミュレーションです。

|param      |shrear_rate|janus_slip_vel |janus_slip_mode|
|:-:        |:-:        |:-:            |:-:            |
|sim04      |0.05 ~ 0.1 |0.0, 0.05 ~ 0.1|0.5            |

### sim04-00 ~ sim04-05

|param   |shrear_rate|
|:-:     |:-:        |
|sim04-00|0.05       |
|sim04-01|0.06       |
|sim04-02|0.07       |
|sim04-03|0.08       |
|sim04-04|0.09       |
|sim04-05|0.10       |

## sim11, sim12
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。fix_cellの違いはシミュレーション結果に影響を与えませんでした。

|param      |shrear_rate|janus_slip_vel|janus_slip_mode|fix_cell|
|:-:        |:-:        |:-:           |:-:            |:-:     |
|sim11      |0.0        |0.001         |50             |OFF     |
|sim12      |0.0        |0.001         |50             |ON      |

## sim16 (dmo00)
bottom heavyの影響を考えた計算が正しいかを確認するシミュレーションです。

|param   |gravity|shrear_rate|janus_slip_vel|janus_slip_mode|free_rigid|pin|
|:-:     |:-:    |:-:        |:-:           |:-:            |:-:       |:-:|
|sim16-00|1.0    |0.0        |0.001         |50             |NO        |NO |
|sim16-01|5.0    |0.0        |0.001         |50             |NO        |NO |
|sim16-02|10.0   |0.0        |0.001         |50             |NO        |NO |


# Archived
## sim00 ~ sim03, sim07 ~ sim10, sim13, sim14
squirmerの進行方向の違いによるせん断応力の変化を調べるシミュレーションです。グラフを比較した結果、free_rigidの値は結果に影響を与えないようです。また、sim11/sim12を比較した時、fix_cellの違いはシミュレーション結果に影響を与えませんでした。sim07/sim08とsim13/sim14は、分割数のみの違いです。

|param      |shear_rate|janus_slip_vel|janus_slip_mode|free_rigid|fix_cell|pin   |
|:-:        |:-:       |:-:           |:-:            |:-:       |:-:     |:-:   |
|sim00/sim01|0.0       |0.1/0.05      |0.5            |YES       |OFF     |ON    |
|sim02/sim03|0.0       |0.1/0.05      |0.5            |YES       |ON      |ON    |
|sim09/sim10|0.0       |0.1/0.05      |0.5            |NO        |OFF     |ON    |
|sim13/sim14|0.0       |0.1/0.05      |0.5            |NO        |ON      |ON    |

## sim05, sim06
shear_rateを0.001に設定しています。

|param      |shear_rate|janus_slip_vel|janus_slip_mode|free_rigid|fix_cell|pin   |
|:-:        |:-:       |:-:           |:-:            |:-:       |:-:     |:-:   |
|sim05      |0.001     |0.1           |0.5            |YES       |OFF     |ON    |
|sim06      |0.001     |0.1           |0.5            |YES       |ON      |ON    |

## sim07, sim08
分割が他のシミュレーションとは異なり、10度刻みです。

|param      |shear_rate|janus_slip_vel|janus_slip_mode|free_rigid|fix_cell|pin   |
|:-:        |:-:       |:-:           |:-:            |:-:       |:-:     |:-:   |
|sim07      |0.0       |0.1           |0.5            |NO        |ON      |ON    |
|sim08      |0.0       |0.05          |0.5            |NO        |ON      |ON    |


## sim17 ~ sim25
粒子の位置は固定し、回転方向だけを変化させられるかを確かめるシミュレーションです。

YES' ->free_rigidをYESに設定し、全てのパラメータをNOにしています。

|param|gravity|shear_rate|janus_slip_vel|janus_slip_mode|pin|free_rigid|fix_cell|
|:-:  |:-:    |:-:       |:-:           |:-:            |:-:|:-:       |:-:     |
|sim17|0.0    |0.1       |0.1           |0.5            |YES|YES       |ON      |
|sim18|0.0    |0.1       |0.1           |0.5            |YES|YES       |OFF     |
|sim19|0.0    |0.1       |0.1           |0.5            |NO |YES       |ON      |
|sim20|0.0    |0.1       |0.1           |0.5            |YES|NO        |ON      |
|sim21|0.0    |0.1       |0.1           |0.5            |YES|NO        |OFF     |
|sim22|0.0    |0.1       |0.1           |0.5            |YES|YES'      |OFF     |
|sim23|0.0    |0.1       |0.1           |0.5            |YES|YES'      |ON      |
|sim24|0.0    |0.1       |0.1           |0.5            |NO |YES'      |ON      |
|sim25|0.0    |0.1       |0.1           |0.5            |NO |YES'      |OFF     |

## sim15
HDF5のテストの為のシミュレーションです。

|param      |shear_rate|janus_slip_vel|janus_slip_mode|
|:-:        |:-:       |:-:           |:-:            |
|sim15      |0.0       |0.001         |50             |

# Caution
多粒子にする場合、epsilonの値を1.0に設定することを忘れないように！
