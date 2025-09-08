# 介绍tf serving的docker编译流程
简单介绍下tf serving: 提供模型在线预估服务

# 官方docker文件地址
https://github.com/tensorflow/serving/tree/2.19.0/tensorflow_serving/tools/docker
https://github.com/tensorflow/serving/blob/2.19.0/tensorflow_serving/tools/docker/Dockerfile.devel

注: 服务器连接外网
搭建编译环境, 稍微改写了Dockerfile.devel, 见目录下Dockerfile.devel.2.19

linux为例,构建编译镜像
# 构建tf基础编译镜像2.19
docker build -f ./Dockerfile.devel.2.19  -t tf_base_2_19_devel .
# 生成容器, 二选一(第一条命令映射了容器和linnux目录)
docker run -it -v {linux_path}:{docker_path} --name {container_name} {imageid} /bin/bash
例: docker run -it -v /root/william/:/home/src --name tf_serving_dev 9dd198625184 /bin/bash
docker run -it --name {container_name} {imageid} /bin/bash

# 进入容器
docker exec -it {container_name} /bin/bash
例: docker exec -it tf_serving_dev /bin/bash

# 下载编译tf_serving源码
wget https://github.com/tensorflow/serving/archive/refs/tags/2.19.0.zip
# 解压缩
unzip 2.19.0.zip
cd serving-2.19.0/

# 编译命令 -- 编译时间较久
bazel build --color=yes --curses=yes \
            --verbose_failures \
            --output_filter=DONT_MATCH_ANYTHING \
            --config=release \
            --config=kokoro \
            tensorflow_serving/model_servers:tensorflow_model_server

# 清楚编译
bazel clean --expunge --color=yes;
rm -rf ~/.cache


# 编译二进制产出路径
bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server

# 模型启动命令
/data/code/bin/tensorflow_model_server --model_config_file=/data/code/models/deep_models.config \
                                       --model_config_file_poll_wait_seconds=60 \
                                       --monitoring_config_file=/data/code/config/prometheus_config.json \
                                       --rest_api_port=8502

说明:
model_config_file: 加载模型配置文件
model_config_file_poll_wait_seconds: 模型配置监听时间
monitoring_config_file: 监控配置
rest_api_port: http端口

