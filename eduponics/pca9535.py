
"""
PCA955
------------------------
16Bit IO Expander
GitHub: https://github.com/ldreesden/pca955
Author: L. Drees
Version: 1.0
Date:05/12/2022
Based on datasheet: https://www.nxp.com/docs/en/data-sheet/PCA9555.pdf
"""


from machine import I2C, Pin
import time

InputPort0 = 0x00
InputPort1 = 0x01
OutputPort0 = 0x02
OutputPort1 = 0x03
PolInversionPort0 = 0x04
PolInversionPort1 = 0x05
ConfigPort0 = 0x06
ConfigPort1 = 0x07


class PCA9555:
    """PCA955 Driver
    16Bit IO extender
    i2c communication
    """

    def __init__(self, i2c, address=0x27):
        """
        Args:
            i2cBus: SoftI2C(Pin(*SCLpin*),Pin(*SDApin*))
            address: i2c address in hex (0x20 by default)
        """
        self.i2c = i2c
        self.address = address
        self.pinStats=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.pinValues=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    def inputPins(self,inputPin):
        """
        Args:
            inputPin(int): 0-7 = IO0_0 - IO0_7 ; 8-15 = IO1_0-IO1_7 
        """
        self.pinStats[inputPin]=1
        stats=0
        if inputPin <= 7:
            for i in range(8):
                stats+=self.pinStats[i]<<i
            stats=int(hex(stats),0)
            self.i2c.writeto_mem(self.address,ConfigPort0,bytes([stats]))
        else:
            for i in range(8):
                stats+=self.pinStats[i+8]<<i
            stats=int(hex(stats),0)
            self.i2c.writeto_mem(self.address,ConfigPort1,bytes([stats]))
        

    def outputPins(self,outputPin):
        """
        Args:
            outputPin(int): 0-7 = IO0_0 - IO0_7 ; 8-15 = IO1_0-IO1_7 
        """
        self.pinStats[outputPin]=0
        stats=0
        if outputPin <= 7:
            for i in range(8):
                stats+=self.pinStats[i]<<i
            stats=int(hex(stats),0)
            self.i2c.writeto_mem(self.address,ConfigPort0,bytes([stats]))
        else:
            for i in range(8):
                stats+=self.pinStats[i+8]<<i
            stats=int(hex(stats),0)
            self.i2c.writeto_mem(self.address,ConfigPort1,bytes([stats]))


    def writePin(self,pin, value):
        """
        Args:
            Pin(int): 0-7 = IO0_0 - IO0_7 ; 8-15 = IO1_0-IO1_7 
            value(int): 0 = off ; 1 = on
        """
        self.pinValues[pin]=value
        vals=0
        if self.pinStats[pin]:
            print('ATTENTION Pin '+str(pin)+' at i2c address '+str(self.address)+' is configed as INPUT')
            return
        elif pin <= 7:
            for i in range(8):
                vals+=self.pinValues[i]<<i
            vals=int(hex(vals),0)
            self.i2c.writeto_mem(self.address,OutputPort0,bytes([vals]))
        else:
            for i in range(8):
                vals+=self.pinValues[i+8]<<i
            vals=int(hex(vals),0)
            self.i2c.writeto_mem(self.address,OutputPort1,bytes([vals]))
        print(vals)


    def readPin(self, pin):
        """Issue a measurement.
        Args:
            writeAddress (int): address to write to
        :return:
        """
        comeback = bytearray(1)
        if not self.pinStats[pin]:
            print('ATTENTION Pin '+str(pin)+' at i2c address '+str(self.address)+' is configed as OUTPUT')
            return
        elif pin <=7:
            comeback =self.i2c.readfrom_mem(self.address,InputPort0,1)
        else:
            self.i2c.readfrom_mem(self.address,InputPort1,2)
        raw = (comeback[0] >> (pin % 8)) & 1
        return
    
    def pin(self,pin, mode, value):
        # define all the pins for the mosfets
        mcp_pins_sheet = {
            8:0,
            9:1,
            10:2,
            11:3
        }
        self.writePin(mcp_pins_sheet[pin],value)

class Relays():

    def __init__(self, i2c, address=0x20):

        self.i2c = i2c
        self.address = address
        self.pca = PCA9555(self.i2c)

        # set pins to low, close the relays
        self.pca.outputPins(8)

    def open(self,pin):
        # open relay by pin number 0-3
        if(pin == 0):
            self.pca.writePin(8,1)
        elif(pin == 1):
            self.pca.writePin(9,1)
        elif(pin == 2):
            self.pca.writePin(10,1)
        elif(pin == 3):
            self.pca.writePin(11,1)

    def close(self,pin):
        # close relay by pin number 0-3
        if(pin == 0):
            self.pca.writePin(8,0)
        elif(pin == 1):
            self.pca.writePin(9,0)
        elif(pin == 2):
            self.pca.writePin(10,0)
        elif(pin == 3):
            self.pca.writePin(11,0)

    def open_all(self):
        # open all relays
        self.pca.writePin(8,1)
        self.pca.writePin(9,1)
        self.pca.writePin(10,1)
        self.pca.writePin(11,1)

    def close_all(self):
        # close all relays
        self.pca.writePin(8,0)
        self.pca.writePin(9,0)
        self.pca.writePin(10,0)
        self.pca.writePin(11,0)

