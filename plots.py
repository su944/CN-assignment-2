#plotting mtuiple plot using pyy

import matplotlib.pyplot as plt
import re
import os 
import Q2 
def host_wise_plotting():
    folders = ['a','b','c']
    congestions = ['cubic','reno','bbr','vegas']
    hosts = ['h1','h2','h3','h4']
    
    for folder in folders:
        if folder in os.listdir("./"):

            print(f"/////////////////////{folder}///////////////////////")
            
            for host in hosts:
                plt.figure()
                
                
                if host in os.listdir(f"./{folder}/text/"):
                        for congestion in congestions:
                            print(folder,host,congestion)
                            
                            if host == 'h4':
                                file = f'{folder}/text/{host}/{folder}_{host}_server_{congestion}.txt'
                                try:
                                    file = open(f'{folder}/text/{host}/{folder}_{host}_server_{congestion}.txt','r')
                                except:
                                    print("file not found" + file)
                                    continue
                            else:
                                file = f'{folder}/text/{host}/{folder}_{host}_client_{congestion}.txt'
                                try:
                                         file = open(f'{folder}/text/{host}/{folder}_{host}_client_{congestion}.txt','r')
                                except:
                                    print("file not found" + file)
                                    continue
                            data = file.read()

                            time_values = re.findall(r'-(\d+\.\d+) ', data)
                            throughput_values = re.findall(r'(\d*\.?\d*) GBytes/sec', data)
                            time_values = [0] + [float(i) for i in time_values]
                            throughput_values = [0] + [float(i) for i in throughput_values]

                          
                            plt.plot(time_values, throughput_values, marker='o',label=f"{congestion}")
                            plt.title('Time vs Throughput')
                            plt.xlabel('Time Interval (sec)')
                            plt.ylabel('Throughput (Gbits/sec)')
                        plt.legend()
                        plt.savefig(f'./{folder}/plots/{host}/{host}_each_congestion.png')
                        plt.close()
               
                
                  
def d_plotting():


    congestions = ['cubic','reno','bbr','vegas']
    print("//////////////folder -d////////////////////")
    hosts = ['h1','h4']
    for host in hosts:
        for loss in [0,1,3]:
            for congestion in congestions:
                if host == 'h4':
                     try:
                         file_path = f"./d/text/h4/d_{host}_server_{congestion}_loss_{loss}.txt"
                         file = open(file_path,'r')
                     except :
                         print("file not found "+  file_path)
                         continue
                else:
                     try:
                         
                         file_path     = f'./d/text/{host}/d_{host}_client_{congestion}_loss_{loss}.txt'
                         file = open(file_path,'r')
                     except:
                         print("file not found "+  file_path)
                         continue
                data = file.read()
                time_values = re.findall(r'-(\d+\.\d+) ', data)
                throughput_values = re.findall(r'(\d*\.?\d*) GBytes/sec', data)
                time_values = [0] + [float(i) for i in time_values]
                throughput_values = [0] + [float(i) for i in throughput_values]

                plt.plot(time_values, throughput_values, marker='o',label=f"congestion={congestion}")
                plt.title('Time vs Throughput for host '+ host + ' loss=' +str(loss))
                plt.xlabel('Time Interval (sec)')
                plt.ylabel('Throughput GBytes/sec')

                            


            plt.legend()
            os.makedirs(f"./d/plots/",exist_ok=True)
            plt.savefig(f"./d/plots/{host}_loss_{loss}.png")
            plt.close()



def c_plots():
    congestions = ["reno","vegas","cubic","bbr"]
    hosts = ["h1","h2","h3"]
    
    for congestion in congestions: 
            plt.figure()
            for host in hosts:
                    try:
                         file_path = f"./c/text/{host}/c_{host}_client_{congestion}.txt"
                         file = open(file_path,'r')
                    except :
                         print("file not found "+  file_path)
                         continue
                    data = file.read()
                    time_values = re.findall(r'-(\d+\.\d+) ', data)
                    throughput_values = re.findall(r'(\d*\.?\d*) GBytes/sec', data)
                    time_values = [0] + [float(i) for i in time_values]
                    throughput_values = [0] + [float(i) for i in throughput_values]

                    plt.plot(time_values, throughput_values, marker='o',label=f"{host}")
                    plt.title('Time vs Throughput for congestion='+congestion)
                    plt.xlabel('Time Interval (sec)')
                    plt.ylabel('Throughput GBytes/sec')
            plt.legend()
            os.makedirs(f"./c/addplots/",exist_ok=True)
            plt.savefig(f"./c/addplots/{congestion}.png")
            plt.close()






# Q2.main()


host_wise_plotting()
d_plotting()
c_plots()