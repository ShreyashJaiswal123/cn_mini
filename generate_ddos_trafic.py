from mininet.topo import Topo
from mininet.net import Mininet
# from mininet.node import CPULimitedHost
from mininet.link import TCLink
# from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
# from mininet.cli import CLI
from mininet.node import OVSKernelSwitch, RemoteController
from time import sleep

from datetime import datetime
from random import randrange, choice


''' 
    mininet custom topology

                                            controller c0
                                                   |
             ______________________________________|_________________________________________________                               
            /               /               /               \                   \                   \                                    
        switch 1        switch 2        switch 3        switch 4            switch 5            switch 6
        /   |   \       /   |  \        /   |  \        /   |   \           /   |   \           /   |   \   
       h1  h2   h3     h4  h5  h6      h7  h8  h9      h10  h11  h12      h13  h14  h15      h16  h17  h18

'''



# main class for topology
class MyTopo( Topo ):

    def build( self ):

        # topology contatings 6 switches with links between 2 neighbour switches 
        # each switch contains 3 hosts we have provided static ip to each and every host

        switch1 = self.addSwitch( 's1', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        host1 = self.addHost( 'h1', cpu=1.0/20,mac="00:00:00:00:00:01", ip="10.0.0.1/24" )
        host2 = self.addHost( 'h2', cpu=1.0/20, mac="00:00:00:00:00:02", ip="10.0.0.2/24" )
        host3 = self.addHost( 'h3', cpu=1.0/20, mac="00:00:00:00:00:03", ip="10.0.0.3/24" )    

        switch2 = self.addSwitch( 's2', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        host4 = self.addHost( 'h4', cpu=1.0/20, mac="00:00:00:00:00:04", ip="10.0.0.4/24" )
        host5 = self.addHost( 'h5', cpu=1.0/20, mac="00:00:00:00:00:05", ip="10.0.0.5/24" )
        host6 = self.addHost( 'h6', cpu=1.0/20, mac="00:00:00:00:00:06", ip="10.0.0.6/24" )

        switch3 = self.addSwitch( 's3', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        host7 = self.addHost( 'h7', cpu=1.0/20, mac="00:00:00:00:00:07", ip="10.0.0.7/24" )
        host8 = self.addHost( 'h8', cpu=1.0/20, mac="00:00:00:00:00:08", ip="10.0.0.8/24" )
        host9 = self.addHost( 'h9', cpu=1.0/20, mac="00:00:00:00:00:09", ip="10.0.0.9/24" )

        switch4 = self.addSwitch( 's4', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        host10 = self.addHost( 'h10', cpu=1.0/20, mac="00:00:00:00:00:10", ip="10.0.0.10/24" )
        host11 = self.addHost( 'h11', cpu=1.0/20, mac="00:00:00:00:00:11", ip="10.0.0.11/24" )
        host12 = self.addHost( 'h12', cpu=1.0/20, mac="00:00:00:00:00:12", ip="10.0.0.12/24" )

        switch5 = self.addSwitch( 's5', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        host13 = self.addHost( 'h13', cpu=1.0/20, mac="00:00:00:00:00:13", ip="10.0.0.13/24" )
        host14 = self.addHost( 'h14', cpu=1.0/20, mac="00:00:00:00:00:14", ip="10.0.0.14/24" )
        host15 = self.addHost( 'h15', cpu=1.0/20, mac="00:00:00:00:00:15", ip="10.0.0.15/24" )

        switch6 = self.addSwitch( 's6', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        host16 = self.addHost( 'h16', cpu=1.0/20, mac="00:00:00:00:00:16", ip="10.0.0.16/24" )
        host17 = self.addHost( 'h17', cpu=1.0/20, mac="00:00:00:00:00:17", ip="10.0.0.17/24" )
        host18 = self.addHost( 'h18', cpu=1.0/20, mac="00:00:00:00:00:18", ip="10.0.0.18/24" )

        # Adding links

        self.addLink( host1, switch1 )
        self.addLink( host2, switch1 )
        self.addLink( host3, switch1 )

        self.addLink( host4, switch2 )
        self.addLink( host5, switch2 )
        self.addLink( host6, switch2 )

        self.addLink( host7, switch3 )
        self.addLink( host8, switch3 )
        self.addLink( host9, switch3 )

        self.addLink( host10, switch4 )
        self.addLink( host11, switch4 )
        self.addLink( host12, switch4 )

        self.addLink( host13, switch5 )
        self.addLink( host14, switch5 )
        self.addLink( host15, switch5 )

        self.addLink( host16, switch6 )
        self.addLink( host17, switch6 )
        self.addLink( host18, switch6 )

        self.addLink( switch1, switch2 )
        self.addLink( switch2, switch3 )
        self.addLink( switch3, switch4 )
        self.addLink( switch4, switch5 )
        self.addLink( switch5, switch6 )


def ip_generator():

    ip = ".".join(["10","0","0",str(randrange(1,19))])
    return ip

def startNetwork():

    #print "Starting Network"
    topo = MyTopo()
    #net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink, controller=None )
    #net.addController( 'c0', controller=RemoteController, ip='192.168.43.55', port=6653 )

    c0 = RemoteController('c0', ip='192.168.0.101', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=c0)

    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
    h9 = net.get('h9')
    h10 = net.get('h10')
    h11 = net.get('h11')
    h12 = net.get('h12')
    h13 = net.get('h13')
    h14 = net.get('h14')
    h15 = net.get('h15')
    h16 = net.get('h16')
    h17 = net.get('h17')
    h18 = net.get('h18')
    
    hosts = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18]
    
    h1.cmd('cd /home/mininet/webserver')
    h1.cmd('python -m SimpleHTTPServer 80 &')
    
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("                 Simulating ICMP (Ping) Flood")  
    print("--------------------------------------------------------------------------------")   
    src.cmd("timeout 20s hping3 -1 -V -d 120 -w 64 -p 80 --rand-source --flood {}".format(dst))  
    sleep(100)
        
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("                 Simulating UDP Flood")  
    print("--------------------------------------------------------------------------------")   
    src.cmd("timeout 20s hping3 -2 -V -d 120 -w 64 --rand-source --flood {}".format(dst))    
    sleep(100)
    
    src = choice(hosts)
    dst = ip_generator()    
    print("--------------------------------------------------------------------------------")
    print("                 Simulating TCP-SYN Flood")  
    print("--------------------------------------------------------------------------------")
    src.cmd('timeout 20s hping3 -S -V -d 120 -w 64 -p 80 --rand-source --flood 10.0.0.1')
    sleep(100)
    
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("                 Simulating LAND Attack")  
    print("--------------------------------------------------------------------------------")   
    src.cmd("timeout 20s hping3 -1 -V -d 120 -w 64 --flood -a {} {}".format(dst,dst))
    sleep(100)  
    print("--------------------------------------------------------------------------------")

    # CLI(net)
    net.stop()

if __name__ == '__main__':
    
    start = datetime.now()
    
    setLogLevel( 'info' )
    startNetwork()
    
    end = datetime.now()
    
    print(end-start)
