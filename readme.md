# Readme

## Part I


  To Run code for Default Configuration i.e  every two router are connected to each other
  ```bash
  sudo python3 Q1.py 
   ```

   To Run the code for Custom Configuration i.e  r1-r3 are not directly connected

   ```bash
   sudo python3 Q1.py --config c
   ```




## Part II
After running each section the plots and server and client data will be stored in the respective folders


```bash
sudo python3 Q2.py --config <section> --congestion <congestion> --loss  <link loss percentage (int)> --time <uptime>
```

**Section** can be a,b,c,d

**congestion** can be reno,cubic,bbr,vegas

**loss** should int and between 0-100

**time** should be int and greater than 0


### Topologies in Each Section and thier Configurations

### Section a 
__client__ - h1,h2,h3


__server__ - h4



To Run section b code with default parameters (loss=0, time = 5 and congestion = all)



```bash
sudo python3 Q2.py --config a 
```


After Execution plots will be stored in ./a/plots

### Section b

__client__ - h1


__server__ - h4


To Run section b code with default parameters (loss=0, time = 5 and congestion = all)
```bash
sudo python3 Q2.py --config b 
```

After Execution plots will be stored in ./b/plots

### Section c
__client__ - h1,h2,h3


__server__ - h4


To Run section c code with default parameters (loss=0, time = 5 and congestion = all)

```bash
sudo python3 Q2.py --config c 
```
After Execution plots will be stored in ./c/plots

### Section d


__clients__ = h1


__servers__ = h4



To Run section d code with default parameters (loss=[0,1,3], time = 5 and congestion = all)
cmd to run section d
```bash
sudo python3 Q2.py --config d 
```

After Execution plots will be stored in ./d/plots



### Plotting

Running the plots.py will run the whole Q2 question and add the combined plots in thier respective folders.

First Run the Q2.py 
  
  ```bash
  sudo python3 Q2.py 
  ```

To Run plots.py

```bash
sudo python3 plots.py
```
After running plots.py addtional plots will be added (for each host combined congestion plot, for each congestion combined loss plot)

The combined plots can be observed in the corresponding folders of each section in the plots folder



### Plots Folder


```
./{section}/plots
```

