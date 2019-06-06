# kdd99 attack detection



---

基于sklearn和kdd99数据集实现的根据网络流量信息进行入侵检测的机器学习模型

**实验环境：** python2.7+mongodb

**数据依赖：** 10%的kdd99数据集

---

**实现功能：** 根据以下连接特征：

 1.TCP连接基本特征

（1）duration. 连接持续时间

（2）protocol_type. 协议类型

（3）service. 目标主机的网络服务类型

（4）flag. 连接正常或错误的状态

（5）src_bytes. 从源主机到目标主机的数据的字节数

（6）dst_bytes. 从目标主机到源主机的数据的字节数

（7）land. 若连接来自/送达同一个主机/端口则为1，否则为0

（8）wrong_fragment. 错误分段的数量

（9）urgent. 加急包的个数

2.基于时间的网络流量统计特征

（1）count. 过去两秒内，与当前连接具有相同的目标主机的连接数

（2）srv_count. 过去两秒内，与当前连接具有相同服务的连接数

（3）serror_rate. 过去两秒内，在与当前连接具有相同目标主机的连接中，出现“SYN” 错误的连接的百分比

（4）srv_serror_rate. 过去两秒内，在与当前连接具有相同服务的连接中，出现“SYN” 错误的连接的百分比

（5）rerror_rate. 过去两秒内，在与当前连接具有相同目标主机的连接中，出现“REJ” 错误的连接的百分比

（6）srv_rerror_rate. 过去两秒内，在与当前连接具有相同服务的连接中，出现“REJ” 错误的连接的百分比

（7）same_srv_rate. 过去两秒内，在与当前连接具有相同目标主机的连接中，与当前连接具有相同服务的连接的百分比

（8）diff_srv_rate. 过去两秒内，在与当前连接具有相同目标主机的连接中，与当前连接具有不同服务的连接的百分比

（9）srv_diff_host_rate. 过去两秒内，在与当前连接具有相同服务的连接中，与当前连接具有不同目标主机的连接的百分比

3.基于主机的网络流量统计特征

（1）dst_host_count. 前100个连接中，与当前连接具有相同目标主机的连接数

（2）dst_host_srv_count. 前100个连接与当前连接有相同目标主机相同服务的连接数

（3）dst_host_same_srv_rate. 前100个连接与当前连接有相同目标主机相同服务的连接百分比

（4）dst_host_diff_srv_rate. 前100个连接与当前连接有相同目标主机不同服务的连接百分比

（5）dst_host_same_src_port_rate. 前100个连接中与当前连接具有相同目标主机相同源端口的连接所占的百分比

（6）dst_host_srv_diff_host_rate. 前100个连接中与当前连接具有相同目标主机相同服务的连接中，与当前连接具有不同源主机的连接所占的百分比

（7）dst_host_serror_rate. 前100个连接中与当前连接具有相同目标主机的连接中，出现SYN错误的连接所占的百分比

（8）dst_host_srv_serror_rate. 前100个连接中与当前连接具有相同目标主机相同服务的连接中，出现SYN错误的连接所占的百分比

（9）dst_host_rerror_rate. 前100个连接中，与当前连接具有相同目标主机的连接中，出现REJ错误的连接所占的百分比

（10）dst_host_srv_rerror_rate. 前100个连接中，与当前连接具有相同目标主机相同服务的连接中，出现REJ错误的连接所占的百分比

判断网络流量是否属于正常请求（0），或以下两类攻击（1和2）：

- DOS, denial-of-service. 拒绝服务攻击

  back/land/Neptune/pod/smurf/teardrop/apache2/udpstorm/processtable/mailbom

- PROBING, surveillance and probing, 端口监视或扫描

  ipsweep/nmap/portsweep/satan/saint/mscan



---

**模型介绍：** 这里首先分别训练了以下单一模型：

- 多层感知机


- 随机森林


- 自适应增强


- 逻辑斯蒂回归


- 极度随机树

然后利用投票法集成所有模型，利用网格搜索确定参数

---

**运行流程：** 首先解压两个rar文件，再运行process.py将数据导入mongodb，之后进入单个文件夹运行xx_runner.py即可，其中，All文件夹下为集成模型。





