
![](imgs/RDK_Solution.jpg)

[English](./README.md) | 简体中文


## RDK Solutions 简介

RDK Solutions仓库基于[RDK](https://d-robotics.cc/rdk)开发, 提供大多数主流算法的部署例程. 例程包含导出D-Robotics *.bin模型, 使用 Python 和 C/C++ API 推理 D-Robotics *.bin模型的流程. 部分模型还包括数据采集, 模型训练, 导出, 转化, 部署流程.

### RDK Solutions 支持如下平台.
 - 支持 [RDK X5](https://developer.d-robotics.cc/rdkx5)平台 (Bayes-e)
 - 支持 [RDK Ultra](https://developer.d-robotics.cc/rdkultra) 平台 (Bayse)
 - 即将支持 [RDK S100](https://developer.d-robotics.cc/rdks100) 平台 (Nash-e)
 - 即将支持 [RDK S100P](https://developer.d-robotics.cc/rdks100) 平台 (Nash-m)
 - 部分支持 [RDK X3](https://developer.d-robotics.cc/rdkx3) 平台 (Bernoulli2)

### 推荐系统版本
- RDK X3: RDK OS 2.1.1, Based on Ubuntu 20.04 aarch64, TROS-Foxy.
- RDK X5: RDK OS 3.1.0, Based on Ubuntu 22.04 aarch64, TROS-Humble.
- RDK Ultra: RDK OS 1.0.1, Based on Ubuntu 20.04 aarch64, TROS-Foxy.

## RDK板卡准备

参考[RDK用户手册](https://developer.d-robotics.cc/information), 使得板卡能正常访问互联网从, 确保能做到以下条件之一.

 - 利用ssh连接RDK板卡, 可以通过Termianl向RDK板卡输入命令, 知道RDK板卡的IP地址. 包括但是不限于MobaXtern, Windows Terminal等.
 - 利用VSCode Remote SSH插件远程连接RDK板卡, 可以正常的使用VSCode. 也可使用其他的IDE.
 - 利用VNC访问板卡, 能通过xfce的图形化界面操作板卡.
 - 利用HDMI连接板卡, 能通过xfce的图形化界面操作板卡.


## 依赖库安装参考
### D-Robotics System Software BSP C/C++ & Python API

随系统烧录, 以debian包的形式管理.
```bash
sudo apt update # 确保有 archive.d-robotics.cc 源
sudo apt install hobot-spdev
sudo apt show hobot-spdev
```
地瓜开发者社区释放的RDK OS系统会自带`hobot-spdev`这个包, 部分代理商的系统会没有这个包, 具体问题请联系代理商, 社区不会主动支持第三方镜像的相关问题.
```bash
$ sudo apt show hobot-spdev

Package: hobot-spdev
Version: 3.0.4-20241220150054
Maintainer: developer@d-robotics.cc
Installed-Size: 969 kB
Depends: hobot-multimedia,hobot-camera,hobot-dnn
Download-Size: 424 kB
APT-Manual-Installed: yes
APT-Sources: http://archive.d-robotics.cc/ubuntu-rdk-x5-beta jammy/main arm64 Packages
Description: Python and C/C++ Development Interface
```

### D-Robotics ToolChain C API
随系统烧录, 是最基本的C API.
还可以参考[RDK用户手册算法工具链](https://developer.d-robotics.cc/rdk_doc/04_toolchain_development)章节, 获取OE包, 从OE包中获取libdnn.so及其头文件.

OE路径: `package/host/host_package/x5_aarch64/dnn_1.24.5.tar.gz`

## 参考资源
- [地瓜机器人](https://d-robotics.cc/): `https://d-robotics.cc/`
- [地瓜开发者社区](https://developer.d-robotics.cc/): `https://developer.d-robotics.cc/`
- [RDK用户手册](https://developer.d-robotics.cc/information): `https://developer.d-robotics.cc/information`


## RDK算法工具链资源

- [社区资源中心](https://developer.d-robotics.cc/resource): `https://developer.d-robotics.cc/resource`

- [RDK X3 算法工具链社区手册](https://developer.d-robotics.cc/api/v1/fileData/horizon_xj3_open_explorer_cn_doc/index.html): `https://developer.d-robotics.cc/api/v1/fileData/horizon_xj3_open_explorer_cn_doc/index.html`

- [RDK X3 OpenExplore 产品发布](https://developer.d-robotics.cc/forumDetail/136488103547258769): `https://developer.d-robotics.cc/forumDetail/136488103547258769`

- [RDK Ultra 算法工具链社区手册](https://developer.d-robotics.cc/api/v1/fileData/horizon_j5_open_explorer_cn_doc/index.html): `https://developer.d-robotics.cc/api/v1/fileData/horizon_j5_open_explorer_cn_doc/index.html`

- [RDK Ultra OpenExplore 产品发布](https://developer.d-robotics.cc/forumDetail/118363912788935318): `https://developer.d-robotics.cc/forumDetail/118363912788935318`

- [RDK X5 算法工具链社区手册](https://developer.d-robotics.cc/api/v1/fileData/x5_doc-v126cn/index.html): `https://developer.d-robotics.cc/api/v1/fileData/x5_doc-v126cn/index.html`

- [RDK X5 OpenExplore 产品发布](https://developer.d-robotics.cc/forumDetail/251934919646096384): `https://developer.d-robotics.cc/forumDetail/251934919646096384`


## 反馈
如果您有任何问题或遇到任何问题, 我们热烈欢迎您将它们发布到[地瓜开发者社区](https://developer.d-robotics.cc)或直接在此仓库中提交`issue`/`comment`. 您的反馈对我们来说是无价的, 我们一直渴望帮助您, 并改善我们的资源.

## 特别声明

**本仓库所提供的数据和模型性能仅供开发者社区参考, 不代表商业量产交付的最终性能.**
