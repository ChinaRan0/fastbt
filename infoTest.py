import warnings
warnings.filterwarnings("ignore")

from rule import arl
from rule import viper
from rule import awvs
from rule import medusa
from rule import nessus
from rule import LangSrc
from rule import nemo
from rule import NextScan
from rule import Manjusaka
from rule import Hzichan
from rule import nps
from rule import nps2
from rule import ChatGPTnextWeb
from rule import DBJ
from rule import linbing
def finger(IPport):
    ip, port = IPport.split(":") 
    port=int(port) 
    arl.check(ip,port)
    viper.check(ip,port)
    awvs.check(ip,port)
    medusa.check(ip,port)
    nessus.check(ip,port)
    LangSrc.check(ip,port)
    nemo.check(ip,port)
    NextScan.check(ip,port)
    Manjusaka.check(ip,port)
    Hzichan.check(ip,port)
    nps.check(ip,port)
    nps2.check(ip,port)
    ChatGPTnextWeb.check(ip,port)
    DBJ.check(ip,port)
    linbing.check(ip,port)