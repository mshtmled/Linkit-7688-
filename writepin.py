import mraa
import time
print(mraa.getVersion()) #查看mraa库的版版本

pin1 = mraa.Gpio(2) #建立GPIO2 的对象
pin1.dir(mraa.DIR_OUT) #设置pin1为写入模式
while(True):
    pin1.write(1) #pin1设置为高电平
    time.sleep(2) #延时2s
    pin1.write(0) #pin1设置为高电平
    time.sleep(2) #延时2s
    


