
import os
import sys

from pyndn import Name, Data, HmacWithSha256Signature, KeyLocatorType
from pyndn.security import KeyChain
from pyndn.util import Blob
from pyndn import Face, Interest
import time, random
from threading import Thread
from pyndn.encoding import ProtobufTlv
from datetime import datetime
import signal

from basic_insertion import requestInsert
from test_register_route import registerRouteWithNameAndIp

pubsubPrefix = sys.argv[1]

repoName = sys.argv[2]

deviceID = sys.argv[3]

deviceIP = sys.argv[4]

routeToRegister0 = str(Name(pubsubPrefix + "/" + repoName + "/" + deviceID + "/" + "temperature"))
routeToRegister1 = str(Name(pubsubPrefix + "/" + repoName + "/" + deviceID + "/" + "humidity"))
routeToRegister2 = str(Name(pubsubPrefix + "/" + repoName + "/" + deviceID + "/" + "pressure"))
routeToRegister3 = str(Name(pubsubPrefix + "/" + repoName + "/" + deviceID + "/" + "resistance"))
routeToRegister4 = str(Name(pubsubPrefix + "/" + repoName + "/" + deviceID + "/" + "occupancy"))

registerRouteWithNameAndIp(routeToRegister0, str(deviceIP))
time.sleep(0.25)
registerRouteWithNameAndIp(routeToRegister1, str(deviceIP))
time.sleep(0.25)
registerRouteWithNameAndIp(routeToRegister2, str(deviceIP))
time.sleep(0.25)
registerRouteWithNameAndIp(routeToRegister3, str(deviceIP))
time.sleep(0.25)
registerRouteWithNameAndIp(routeToRegister4, str(deviceIP))
time.sleep(0.25)

os.system("dc-exp " + deviceID + " " + pubsubPrefix + " " + repoName)

