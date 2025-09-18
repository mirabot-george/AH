# 电机控制模式

TOML文件设定舵机配置 (cf. [r_hand.toml](config/r_hand.toml)).
设置电机ID和每个手指的角度偏移.

# 工具
- *change_id*: 更改舵机ID. `cargo run --bin=change_id -- -h` 查看参数列表
- *goto*: 驱动一个电机到指定位置. `cargo run --bin=goto -- -h` 查看参数列表
- *get_zeros*: 设置舵机零位. `cargo run --bin=get_zeros -- -h` 查看参数列表
- *set_zeros*: 移动手到config文件设定的初始位置. `cargo run --bin=set_zeros -- -h` 查看参数列表
