import mraa
import time
print(mraa.getVersion()) #查看mraa库的版版本

pin1 = mraa.Gpio(2) #建立GPIO2 的对象
pin1.dir(mraa.DIR_IN) #设置pin1为写入模式

while True:
    print("P1 state:",pin1.read()) #读取pin1电平
    time.sleep(0.5)
    

