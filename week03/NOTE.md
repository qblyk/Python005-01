学习笔记

arch   #查看系统位  32/64

cat /etc/redhat-release   ##查看操作系统版本

所需下载的安装包：

mysql-community-client-5.7.32-1.el7.x86_64.rpm

mysql-community-common-5.7.32-1.el7.x86_64.rpm

mysql-community-libs-5.7.32-1.el7.x86_64.rpm

mysql-community-libs-compat-5.7.32-1.el7.x86_64.rpm

mysql-community-server-5.7.32-1.el7.x86_64.rpm

下载地址：

https://dev.mysql.com/downloads/mysql/5.7.html

安装命令：

yum install *.rpm

文件上传到服务器：

scp -r '/Users/blyk/Downloads/mysql-community-client-5.7.32-1.el7.x86_64.rpm' root@81.68.90.212:/opt/mysql/

１）scp是命令，-r是参数

２）localfile.txt 是文件的路径和文件名

３）username是服务器账号

４）192.168.0.1是要上传的服务器ip地址

５）/home/username/是要拷入的文件夹路径

启动mysql：

systemctl start mysqld.service

开机启动设置：

systemctl enable mysqld

确定安装版本：

rpm -qa | grep -i 'mysql'

查看mysql初始密码：

grep 'password' /var/log/mysqld.log | head -1

SC,&>c%?!3yC

打开mysql：

mysql -uroot -pqcL_584652199

mysql -uroot -p   #需要手动数据 

 

修改密码：

ALTER USER 'root'@'localhost' IDENTIFIED BY 'qcL_584652199';

ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';

查看密码强度要求：

mysql>  SHOW VARIABLES LIKE 'validate_password%';

set global validate_password_policy=0;   #设置为低

set global validatepasswordlength=6;      #设置长度为6位

