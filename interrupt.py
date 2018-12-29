import mraa
import time
print(mraa.getVersion()) #查看mraa库的版版本

def callback(userdata):
    print("interrupt triggered with userdata=",userdata)

pin1 = mraa.Gpio(2) #建立GPIO2 的对象
pin1.dir(mraa.DIR_IN) #设置pin1为写入模式

pin.isr(mraa.EDGE_BOTH, callback,None) #边沿触发

while(True):
    time.sleep(1) #等待中断到来