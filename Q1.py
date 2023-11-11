from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
import argparse
from mininet.link import TCLink

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class NetworkTopo(Topo):
    def build(self, **_opts):
        # Add 3 routers in three different subnets
        # Configuring subnet1 for router1, IP=10.0.0.1
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.0.0.1/24')
        s1 = self.addSwitch('s1')
        self.addLink(s1, r1, intfName2='r1-eth1', params2={'ip': '10.0.0.1/24'},cls=TCLink)
        h1 = self.addHost(name='h1', ip='10.0.0.2/24', defaultRoute='via 10.0.0.1')
        h2 = self.addHost(name='h2', ip='10.0.0.3/24', defaultRoute='via 10.0.0.1')
        self.addLink(h1, s1,cls=TCLink)
        self.addLink(h2, s1,cls=TCLink)
        
        # Configuring subnet2 for router2, IP=10.1.0.1
        r2 = self.addHost('r2', cls=LinuxRouter, ip='10.1.0.1/24')
        s2 = self.addSwitch('s2')
        self.addLink(s2, r2, intfName2='r2-eth1', params2={'ip': '10.1.0.1/24'},cls=TCLink)
        h3 = self.addHost(name='h3', ip='10.1.0.2/24', defaultRoute='via 10.1.0.1')
        h4 = self.addHost(name='h4', ip='10.1.0.3/24', defaultRoute='via 10.1.0.1')
        self.addLink(h3, s2,cls=TCLink)
        self.addLink(h4, s2,cls=TCLink)

        # Configuring subnet3 for router3, IP=10.2.0.1
        r3 = self.addHost('r3', cls=LinuxRouter, ip='10.2.0.1/24')
        s3 = self.addSwitch('s3')
        self.addLink(s3, r3, intfName2='r3-eth1', params2={'ip': '10.2.0.1/24'},cls=TCLink)
        h5 = self.addHost(name='h5', ip='10.2.0.2/24', defaultRoute='via 10.2.0.1')
        h6 = self.addHost(name='h6', ip='10.2.0.3/24', defaultRoute='via 10.2.0.1')
        self.addLink(h5, s3,cls=TCLink)
        self.addLink(h6, s3,cls=TCLink)

        # Adding router-router connections
        self.addLink(r1, r2, intfName1='r1-eth2', intfName2='r2-eth2',
                     params1={'ip': '10.10.0.1/24'}, params2={'ip': '10.10.0.2/24'},cls=TCLink)
        self.addLink(r2, r3, intfName1='r2-eth3', intfName2='r3-eth2',
                     params1={'ip': '10.20.0.1/24'}, params2={'ip': '10.20.0.2/24'},cls=TCLink)
        self.addLink(r3, r1, intfName1='r3-eth3', intfName2='r1-eth3',
                     params1={'ip': '10.30.0.1/24'}, params2={'ip': '10.30.0.2/24'},cls=TCLink)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Mininet Example")
    parser.add_argument("--config", help="Configuration parameter")
    args = parser.parse_args()
    print(args.config)
    setLogLevel('info')
    topo = NetworkTopo()
    net = Mininet(topo=topo, waitConnected=True)

    # Add routing for reaching networks that aren't directly connected
    info(net['r1'].cmd("ip route add 10.1.0.0/24 via 10.10.0.2 dev r1-eth2"))
    if args.config == 'c': 
        info(net['r1'].cmd("ip route add 10.2.0.0/24 via 10.10.0.2 dev r1-eth2")) #***********************
    else:
        info(net['r1'].cmd("ip route add 10.2.0.0/24 via 10.30.0.1 dev r1-eth3"))
    info(net['r2'].cmd("ip route add 10.2.0.0/24 via 10.20.0.2 dev r2-eth3"))
    info(net['r2'].cmd("ip route add 10.0.0.0/24 via 10.10.0.1 dev r2-eth2"))
    if args.config == 'c':
        info(net['r3'].cmd("ip route add 10.0.0.0/24 via 10.20.0.1 dev r3-eth2")) 
    else:
        info(net['r3'].cmd("ip route add 10.0.0.0/24 via 10.30.0.2 dev r3-eth3")) 
    info(net['r3'].cmd("ip route add 10.1.0.0/24 via 10.20.0.1 dev r3-eth2"))

    net.start()
    info('*** Adding static routes on routers:\n')
    info('*** Routing Tables on Routers:\n')

    for router in ['r1', 'r2', 'r3']:
        info(net[router].cmd('route'))
    
    CLI(net)
    net.stop()
