import ctypes
from enum import Enum
from enum import IntEnum
import re
import ctypes
from ctypes import c_uint8
from ctypes import c_int8
from ctypes import c_int16

from collections import namedtuple
from collections import OrderedDict


c_uint8 = ctypes.c_uint8

class rfDataType(Enum):
    JSON_NULL     = 0x00
    Boolean_True  = 0x01
    Boolean_False = 0x02
    int8          = 0x03
    uint8         = 0x04
    int16         = 0x05
    uint16        = 0x06
    int32         = 0x07
    uint32        = 0x08
    int64         = 0x09
    uint64        = 0x0A

class rfbitResetAllowableValues(IntEnum):
    On               = 0x01
    ForceOff         = 0x02
    GracefulShutdown = 0x04
    ForceReset       = 0x08
    NMI              = 0x10
    GracefulRestart  = 0x20
    ForceOn          = 0x40
    PushPowerButton  = 0x80
    
class rfbitMaskBootSrcTargAllowableValues(IntEnum):
 #   _None       = 0x0001
    Pxe        = 0x0002
    Floppy     = 0x0004
    Cd         = 0x0008
    Usb        = 0x0010
    Hdd        = 0x0020
    BIOSSetup  = 0x0040
    Utilities  = 0x0080
    Diags      = 0x0100
    UefiShell  = 0x0200
    UefiTarget = 0x0400
    SDCard     = 0x0800



class rfDataTypeStatusState(Enum):
    Enabled        = 1
    Disabled       = 2 
    StandbyOffline = 3
    StandbySpare   = 4
    InTest         = 5
    Starting       = 6 
    Absent         = 7 

class rfDataTypeStatusHealthRollup(Enum):
    OK       = 1
    Warning  = 2 
    Critical = 3 


class rfDataTypeStatusHealth(Enum):
    OK       = 1
    Warning  = 2 
    Critical = 3 


class Flags_bits( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("logout",     c_uint8, 1 ),  # asByte & 1
                ("userswitch", c_uint8, 1 ),  # asByte & 2
                ("suspend",    c_uint8, 1 ),  # asByte & 4
                ("idle",       c_uint8, 1 ),  # asByte & 8
               ]

class Flags( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                ("bit",    Flags_bits ),
                ("asByte", c_uint8    )
               ]

class Strflag_bits( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("StringLength", c_uint8, 7 ),  
               ]

class Status_bits( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("Health",                 c_uint8, 2 ),  
                ("HealthRollupStat",       c_uint8, 2 ),  
                ("State",           c_uint8, 4 ),  
               ]

class Strflag( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                ("bit",    Strflag_bits ),
                ("asByte", c_uint8    ),
                ("asWord", c_int16    )
               ]
class Status( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                ("bit",    Status_bits ),
                ("asByte", c_uint8    ),
                ("asWord", c_int16    )
               ]



rfEnumEccType = Enum(
    value = 'rfEnumEccType',
    names=[
        ('NoECC', 0x01), 
        ('SingleBitECC', 0x02), 
        ('MultiBitECC', 0x03), 
    ]
)

rfEnumDimmType= Enum(
    value = 'rfEnumDimmType',
    names=[
        ('DDR3', 0x01), 
        ('SingleBitECC', 0x02), 
        ('MultiBitECC', 0x03), 
    ]
)

rfEnumDimmTechnology = Enum(
    value = 'rfEnumDimmTechnology',
    names=[
        ('UDIMM', 0x01), 
        ('RDIMM', 0x02), 
        ('LR-DIMM', 0x03), 
    ]
)

def bootSrcAllwblVals(num):
    active = [val.name for val in rfbitMaskBootSrcTargAllowableValues.__members__.values() if num & val]
    return active

def rstAllwblVals(num):
    active = [val.name for val in rfbitResetAllowableValues.__members__.values() if num & val]
    return active


rstAllwblVals(0x0c)

print ("rfEnumDimmTecho type 1: %s" % rfEnumDimmTechnology(0x01))
print ("rfEnumDimmTecho type 1: %s" % rfEnumDimmTechnology(0x01).name)

hexptrn="^0x8[0-9a-fA-f]$"
ip="0x83"
if re.search(hexptrn, ip):
  print ("found a match %s" % ip)
ip="0x08"
if re.search(hexptrn, ip):
  print ("found a search %s" % ip)
ip="0x80"
if re.search(hexptrn, ip):
  print ("found a search %s" % ip)
ip="0x8"
if re.search(hexptrn, ip):
  print ("found a search %s" % ip)
ip="0x8a"
if re.search(hexptrn, ip):
  print ("found a search %s" % ip)
ip="0x800"
if re.search(hexptrn, ip):
  print ("found a match %s" % ip)
ip="0x8ff"
if re.search(hexptrn, ip):
  print ("found a search %s" % ip)

rfDataDef={ 0x00: ('JSON NULL', 0),  0x01: ('Boolean TRUE', 0),  0x02: ('Boolean FALSE', 0),  0x03: ('int8', 1),  0x04: ('uint8', 1),  0x05: ('JSON NULL', 0),  0x06: ('JSON NULL', 0),  0x07: ('JSON NULL', 0),  0x08: ('JSON NULL', 0)}

#rfDataDef= Enum(
#    value = 0x00,
#    names=[
#        ('JSON NULL', 0), 
#    ]
#    value = '0x01',
#    names=[
#        ('Boolean TRUE', 0), 
#    ]
#)
#rfDataDef=[
#        (0x00, 'JSON NULL', 0),
#        (0x01, 'Boolean TRUE', 0),
#        (0x02, 'Boolean FALSE', 0),
#        (0x03, c_int8, 1)
#    ]
#
#py3.4 does not allow "0" prefixes on numbers

###Named Tuples Test####

#JSON NULL
rfDataDef = namedtuple('rfDataDef', ['value', 'datatype','datalength'])
json_null=rfDataDef(0x00, 'JSON_NULL', 0)
print (json_null[0], json_null[1], json_null[2])

#uint8
rfuint8=rfDataDef(0x04, 'uint8', 1)
#if 0x04, next popped token would be ctypes.unint8[1](token)

#BootSrcTargAllowableValues
bootsrcAllwVals=rfDataDef(0x22, 'BootSrcTargAllowableValues', {'bootSrcAllwblVals': bootSrcAllwblVals})
bootsrc=bootsrcAllwVals[2]['bootSrcAllwblVals'](0x0c)
print ("printing bootsrc %s" % bootsrc)

#Status(Struct)
status = Status()
status.asByte = 0x5e  # ->01011100
#healthstate=rfDataDef(0x20, 'Status', 1)
#print ("Health: %d" % healthstate[2]['state'](0x5e))
print ("Health: %s" % rfDataTypeStatusHealth(2))
print( "Health: %s"      % rfDataTypeStatusHealth(status.Health))

#Get length of String Variable >0x80
strflag=Strflag()
strflag.asByte=0x9a  # ->10011010
print("String length is %s" % strflag.StringLength)
#healthstate=rfDataDef(0x20, 'Status', 1)
#print ("Health: %d" % healthstate[2]['state'](0x5e))
print ("Health: %s" % rfDataTypeStatusHealth(2))
print( "Health: %s"      % rfDataTypeStatusHealth(status.Health))

#TODO: Calculate length of string and entire API to check() if it is valid
#Calculate all string lengths
#Calculate all error/unsupported tokens
#Add remaining token lengths
#Should equal


###########################
###########################
###########################

###Start: rfMemoryInfo API####

#TODO Change all property values to double quotes
#TODO should BootSrcTargAllowableValues be a string of values or a list?
#TODO must convert DataTypes (NumOfDIMMS) to Enums
#TODO add "0x7c" and give it the value of "Property does not exist for this BMC"
#TODO Code Exceptions
#TODO check return values for json/dict should they all be strings or in native format (int)?
    #print("token=%s" % token)
    #print("dataType=%s" % dataType)
    #print("value=%d" % value)

#Request 0x30 0xc8 0x01 0x05 0x4d 0x00 0x00 0x00 0x01
#data=["0x05", "0x4d", "0x00", "0x00", "0x00", "0x4d", "0x00", "0x01", "0x0f", "0x04", "0x01", "0x3d", "0x02", "0x3c", "0x03", "0x7c", "0x04", "0x02", "0x7c", "0x04", "0x40", "0x04", "0x48", "0x08", "0x00", "0x40", "0x00", "0x00", "0x06", "0x6a", "0x0a", "0x8e", "0x44", "0x49", "0x4d", "0x4d", "0x2e", "0x53", "0x6f", "0x63", "0x6b", "0x65", "0x74", "0x2e", "0x41", "0x31", "0x87", "0x53", "0x61", "0x6d", "0x73", "0x75", "0x6e", "0x67", "0x88", "0x30", "0x33", "0x30", "0x31", "0x37", "0x33", "0x38", "0x30", "0x90", "0x4d", "0x33", "0x39", "0x33", "0x41", "0x32", "0x4b", "0x34", "0x33", "0x42", "0x42", "0x31", "0x2d", "0x43", "0x54", "0x44", "0x20", "0x15",]
#d1=[int(i,16) for i in data]
#print (d1)

resp={'data': [5, 77, 0, 0, 0, 77, 0, 1, 15, 4, 1, 61, 2, 60, 3, 124, 4, 2, 124, 4, 64, 4, 72, 8, 0, 64, 0, 0, 6, 106, 10, 142, 68, 73, 77, 77, 46, 83, 111, 99, 107, 101, 116, 46, 65, 49, 135, 83, 97, 109, 115, 117, 110, 103, 136, 48, 51, 48, 49, 55, 51, 56, 48, 144, 77, 51, 57, 51, 65, 50, 75, 52, 51, 66, 66, 49, 45, 67, 84, 68, 32, 21]}

print ("data[9] %s" % resp['data'][9])
print ("data %s" % resp['data'][:])

#TODO are we sure about positions in API's data structure? i.e ipmiRespData[7] == ResponseVersion???
d=OrderedDict()
#d={}
print ("data %s" % resp['data'][:])

rfDataDef=[(0x04, "Index"), (0x3d, "DIMMType"), (0x3C, "ECCTypes"), (0x3e, "DIMMTechnology"), (0x4, "Rank"), (0x4, "MinVoltage X 100"), (0x4, "DataWidthBits"), (0x4, "TotalWidth"), (0x08, "SizeMB"), (0x6, "SpeedMHz"), (0x80, "SocketLocator"), (0x80, "Manufacturer"), (0x80, "SerialNumber"), (0x80, "PartNumber"), (0x20, "Status")]
print(rfDataDef)
token_list=resp['data'][9:]
print(token_list)

while token_list:  

    #print(rfDataDef)
    print(token_list)
    token=hex(token_list.pop(0))
    value,dataType=rfDataDef.pop(0) 

    d["ResponseVersion"]=resp['data'][7]# 1st byte of raw 
    d["NumOfParams"]=resp['data'][8]# 2nd byte of raw 
    if token == '0x7c':
        # print("token found was %s", token)
        d[dataType]=None

    if token == '0x3d':
        # print("token found was %s", token)
        if dataType == "DIMMType": 
            d["DIMMType"]=rfEnumDimmType(token_list.pop(0)).name

    if token == '0x3c':
        # print("token found was %s", token)
        if dataType == "ECCTypes": 
            d["ECCTypes"]=rfEnumEccType(token_list.pop(0)).name
    
    if token == '0x3e':
        # print("token found was %s", token)
        if dataType == "DIMMTechnology": 
            d["DIMMTechnology"]=rfEnumDimmTechnology(token_list.pop(0)).name

    if token == '0x21':
        # print("token found was %s", token)
        d["ResetAllowableValues"]=rstAllwblVals( token_list.pop(0) )

    if token == '0x4':
        # print("token found was %s" % token)
        if dataType == "Index": 
            d["Index"]=ctypes.c_uint8(token_list.pop(0)).value
        if dataType == "Rank": 
            d["Rank"]=ctypes.c_uint8(token_list.pop(0)).value
        if dataType == "MinVoltage X 100": 
            d["MinVoltage X 100"]=ctypes.c_uint8(token_list.pop(0)).value
        if dataType == "DataWidthBits": 
            d["DataWidthBits"]=ctypes.c_uint8(token_list.pop(0)).value
        if dataType == "TotalWidth": 
            d["TotalWidth"]=ctypes.c_uint8(token_list.pop(0)).value

    if token == '0x8':
        if dataType == "SizeMB": 
            bt4=token_list.pop(0)
            bt3=token_list.pop(0)
            bt2=token_list.pop(0)
            bt1=token_list.pop(0)
            d["SizeMB"]=ctypes.c_uint32(bt1<<32| bt3<<16 |bt2<<8 |bt1).value

    if token == '0x20':
        if dataType == "Status": 
            status = Status()
            status.asByte=int(hex(token_list.pop(0)),16)# ->10011010
            #d["Status"]={"State":rfDataTypeStatusState(status.State), "Health":None, "HealthRollup":rfDataTypeStatusHealthRollup(status.HealthRollupStat)} 
            d["Status"]={"State":rfDataTypeStatusState(status.State).name, "Health":rfDataTypeStatusHealth(status.Health).name, "HealthRollup":rfDataTypeStatusHealthRollup(status.HealthRollupStat).name}

    if token == '0x6':
        if dataType == "SpeedMHz": 
            lsb=token_list.pop(0)
            msb=token_list.pop(0)
            d["SpeedMHz"]=ctypes.c_uint16(msb<<8 | lsb).value


    hexptrn="^0x[8-9][0-9a-fA-f]$"
    # print("token=%s" % token)
    if re.search(hexptrn, token):
        # print("STRING token found was %s" % token)
        if dataType == "SocketLocator": 
                    strflag=Strflag()
                    #just always keep token as hex "number" not hex string
                    strflag.asByte=int(token,16)# ->10011010
                    # print("String length is %s" % strflag.StringLength)
                    #print("token_list is %s" % token_list)
                    intlist=token_list[:strflag.StringLength-1]
                    strlist=''.join(chr(i) for i in intlist)
                    #print("strlist is %s" % strlist)
                    d["SocketLocator"]=strlist
                    #print("range %s" % strflag.StringLength)
                    for x in range(strflag.StringLength):
                        token_list.pop(0)
                        #print("token_list %s" % token_list)
    
        if dataType == "Manufacturer": 
                    strflag=Strflag()
                    strflag.asByte=int(token,16)# ->10011010
                    #print("String length is %s" % strflag.StringLength)
                    #print("token_list is %s" % token_list)
                    intlist=token_list[:strflag.StringLength-1]
                    strlist=''.join(chr(i) for i in intlist)
                    #print("strlist is %s" % strlist)
                    d["Manufacturer"]=strlist
                    #print("range %s" % strflag.StringLength)
                    for x in range(strflag.StringLength):
                        token_list.pop(0)
                        #print("token_list %s" % token_list)

        if dataType == "SerialNumber": 
                    strflag=Strflag()
                    strflag.asByte=int(token,16)# ->10011010
                    #print("String length is %s" % strflag.StringLength)
                    #print("token_list is %s" % token_list)
                    intlist=token_list[:strflag.StringLength-1]
                    strlist=''.join(chr(i) for i in intlist)
                    #print("strlist is %s" % strlist)
                    d["SerialNumber"]=strlist
                    #print("range %s" % strflag.StringLength)
                    for x in range(strflag.StringLength):
                        token_list.pop(0)
                        #print("token_list %s" % token_list)

        if dataType == "PartNumber": 
                    strflag=Strflag()
                    strflag.asByte=int(token,16)# ->10011010
                    #print("String length is %s" % strflag.StringLength)
                    #print("token_list is %s" % token_list)
                    intlist=token_list[:strflag.StringLength-1]
                    strlist=''.join(chr(i) for i in intlist)
                    #print("strlist is %s" % strlist)
                    d["PartNumber"]=strlist
                    #print("range %s" % strflag.StringLength)
                    for x in range(strflag.StringLength):
                        token_list.pop(0)
                        #print("token_list %s" % token_list)
print(d)

    
       # send response
       # return(rc,completionCode, True, resp)
###End: rfMemoryInfo API###

###########################
###########################
###########################

###rfSystemInfo API###
resp={'data': [2, 48, 0, 0, 0, 48, 0, 1, 9, 34, 255, 4, 33, 191, 4, 2, 154, 73, 110, 116, 101, 108, 32, 32, 77, 111, 100, 101, 108, 32, 56, 53, 32, 83, 116, 101, 112, 112, 105, 110, 103, 32, 50, 6, 32, 2, 4, 2, 4, 1, 4, 2, 124]}
print ("data[9] %s" % resp['data'][9])
print ("data %s" % resp['data'][:])
####Try Processing####
#resp=['0x02', '0x30', '0x00', '0x00', '0x00', '0x30', '0x00', '0x01', '0x09', '0x22', '0xff', '0x04', '0x21', '0xbf', '0x04', '0x02', '0x9a', '0x49', '0x6e', '0x74', '0x65', '0x6c', '0x20', '0x20', '0x4d', '0x6f', '0x64', '0x65', '0x6c', '0x20', '0x38', '0x35', '0x20', '0x53', '0x74', '0x65', '0x70', '0x70', '0x69', '0x6e', '0x67', '0x20', '0x32', '0x06', '0x20', '0x00', '0x04', '0x02', '0x04', '0x01', '0x04', '0x02', '0x7c']

#rfSysInfoRCDS={'0x22': bootSrcAllwVals, '0x21': resetAllowableValues}

##Check for tokens and sizes to be sure they match and save in structure
#TODO: Make Ordered collection for Error/Debug 
d=OrderedDict()
d['ResponseVersion']=0x01
d['NumOfParams']=0x09
#d={}
print ("data %s" % resp['data'][:])

token_list=resp['data'][9:]
print(token_list)
rfDataDef=[(0x22, "BootSrcTargAllowableValues"), (0x21, "ResetAllowableValues"), (0x04, "ProcessorCount"), (0x80, "ProcessorModel"), (0x06, "Total SystemMemorySize(GB)"), (0x4, "NumOfDIMMs"), (0x4, "NumOfNICs"), (0x4, "NumOfSimpleStorageCntrlr"), (0x4, "NumOfStorageCntrlr")]
print(rfDataDef)
#We could fill another ordered dictionary with the tuple values of (token, name) e.g. (0x22, 'BootSrcTargAllowableValues')
while token_list:  


    token=hex(token_list.pop(0))
    value,dataType=rfDataDef.pop(0) 

#TODO Change all property values to double quotes
#TODO should BootSrcTargAllowableValues be a string of values or a list?
#TODO must convert DataTypes (NumOfDIMMS) to Enums
#TODO add "0x7c" and give it the value of "Property does not exist for this BMC"
#TODO Code Exceptions
#TODO check return values for json/dict should they all be strings or in native format (int)?
    #print("token=%s" % token)
    #print("dataType=%s" % dataType)
    #print("value=%d" % value)

    if token == '0x7c':
        print("token found was 0x7c")
        d[dataType]="Property does not exist for this BMC"

    if token == '0x22':
        print("token found was 0x22")
    if dataType == "BootSrcTargAllowableValues": 
        d["BootSrcTargAllowableValues"]=bootSrcAllwblVals(token_list.pop(0) + token_list.pop(0) )

    #print(d)

    if token == '0x21':
        print("token found was 0x21")
        d["ResetAllowableValues"]=rstAllwblVals( token_list.pop(0) )

    #print(d)

    if token == '0x4':
        print("token found was %s" % token)
        if dataType == "ProcessorCount": 
            d["ProcessorCount"]=ctypes.c_uint8(token_list.pop(0)).value
        if dataType == "NumOfDIMMs": 
            d["NumOfDIMMs"]=ctypes.c_uint8(token_list.pop(0)).value
        if dataType == "NumOfNICs": 
            d["NumOfNICs"]=ctypes.c_uint8(token_list.pop(0)).value
        if dataType == "NumOfSimpleStorageCntrlr": 
            d["NumOfSimpleStorageCntrlr"]=ctypes.c_uint8(token_list.pop(0)).value
        if dataType == "NumOfStorageCntrlr": 
            d["NumOfStorageCntrlr"]=ctypes.c_uint8(token_list.pop(0)).value

    #print(d)

    hexptrn="^0x[8-9][0-9a-fA-f]$"
    #print("token=%s" % token)
    if re.search(hexptrn, token):
        print("token found was %s" % token)
        if dataType == "ProcessorModel": 
            strflag=Strflag()
            strflag.asByte=0x9a  # ->10011010
            #print("String length is %s" % strflag.StringLength)
            #print("token_list is %s" % token_list)
            intlist=token_list[:strflag.StringLength-1]
            strlist=''.join(chr(i) for i in intlist)
            #print("strlist is %s" % strlist)
            d["ProcessorModel"]=strlist
            #print("range %s" % strflag.StringLength)
            for x in range(strflag.StringLength):
                token_list.pop(0)
                #print("token_list %s" % token_list)


    #print(d)
    #print("token=%s" % token)
    if token == '0x6':
        print("token found was %s" % token)
        if dataType == "Total SystemMemorySize(GB)": 
            lsb=token_list.pop(0)
            msb=token_list.pop(0)
            #print("hex is %s" % (msb<<8 | lsb) )
    #TODO cast to uint16
            d["Total SystemMemorySize(GB)"]=ctypes.c_uint16(msb<<8 | lsb).value

                #"20 00 should be interpreted as uint16("00 20")
            #print("binfint %i, binfint %i" % (token_list.pop(0), token_list.pop(0)) )

print(d)

    
#token=hex(token_list.pop())
#bSTAV1=bootsrcAllwVals[2]['bootSrcAllwblVals'](hex(token_list.pop()))

#   #Check against ordered lis named tuples
#   token
   

##
#while token_list:
#    token=hex(token_list.pop())

#Need dynamic processing
#resp_dict['BootSrcTargAllowableValues']=d['0x22']
#print(resp_dict)
#resp_dict['ResetAllowableValues']=
#resp_dict['ProcessorCount']=
#resp_dict['ProcessorModel']=
#resp_dict['Total SystemMemorySize(GB)']=
#resp_dict['NumOfDIMMs']=
#resp_dict['NumOfNICs']=
#resp_dict['NumOfSimpleStorageCntrlr']=
#resp_dict['NumOfStorageCntrlr']=
#while there are still tokens from token_list
##pop the next token
##if this token exists in rSysInfoRCDS
##
#while token_list:
#    token=hex(token_list.pop())
##print ("rfEnumDimmTecho type 1: %s" % rfEnumDimmTechnology(0x01).name)
#    #if [rfDataRef.(value) for value in rfSysInfoRCDS]:
#    if [ token in rfDataDef
#    value=rfDataRef
#        if token == value:
#            for x in range rfDataDef.name(value):
#               
#
#
#print("dict %s " % resp_dict={})



#This is the data we get back from ipmilib
#respMem={'data': [05, 4d, 00, 00, 00, 4d, 00, 01, 0f, 04, 01, 3d, 02, 3c, 03, 7c, 04, 02, 7c, 04, 40, 04, 48, 08, 00, 40, 00, 00, 06, 6a, 0a, 8e, 44, 49, 4d, 4d, 2e, 53, 6f, 63, 6b, 65, 74, 2e, 41, 31, 87, 53, 61, 6d, 73, 75, 6e, 67, 88, 30, 33, 30, 31, 37, 33, 38, 30, 90, 4d, 33, 39, 33, 41, 32, 4b, 34, 33, 42, 42, 31, 2d, 43, 54, 44, 20, 15,]}
respMem=['0x05', '0x4d', '0x00', '0x00', '0x00', '0x4d', '0x00', '0x01', '0x0f', '0x04', '0x01', '0x3d', '0x02', '0x3c', '0x03', '0x7c', '0x04', '0x02', '0x7c', '0x04', '0x40', '0x04', '0x48', '0x08', '0x00', '0x40', '0x00', '0x00', '0x06', '0x6a', '0x0a', '0x8e', '0x44', '0x49', '0x4d', '0x4d', '0x2e', '0x53', '0x6f', '0x63', '0x6b', '0x65', '0x74', '0x2e', '0x41', '0x31', '0x87', '0x53', '0x61', '0x6d', '0x73', '0x75', '0x6e', '0x67', '0x88', '0x30', '0x33', '0x30', '0x31', '0x37', '0x33', '0x38', '0x30', '0x90', '0x4d', '0x33', '0x39', '0x33', '0x41', '0x32', '0x4b', '0x34', '0x33', '0x42', '0x42', '0x31', '0x2d', '0x43', '0x54', '0x44', '0x20', '0x15',]

y=[int(num,16) for num in respMem]
print(y)

respMem={'data': [5, 77, 0, 0, 0, 77, 0, 1, 15, 4, 1, 61, 2, 60, 3, 124, 4, 2, 124, 4, 64, 4, 72, 8, 0, 64, 0, 0, 6, 106, 10, 142, 68, 73, 77, 77, 46, 83, 111, 99, 107, 101, 116, 46, 65, 49, 135, 83, 97, 109, 115, 117, 110, 103, 136, 48, 51, 48, 49, 55, 51, 56, 48, 144, 77, 51, 57, 51, 65, 50, 75, 52, 51, 66, 66, 49, 45, 67, 84, 68, 32, 21]}
print ("data[9] %s" % respMem['data'][9])

  
flags = Flags()
flags.asByte = 0x2  # ->0000 0010

flags = Flags()
flags.asWord = 0x0202  # ->0000 0010
print ("Word %d" % flags.asWord)

print( "logout: %i"      % flags.bit.logout   )
# `bit` is defined as anonymous field, so its fields can also be accessed directly:
print( "logout: %i"      % flags.logout     )
print( "userswitch:  %i" % flags.userswitch )
print( "suspend   :  %i" % flags.suspend    )
print( "idle  : %i"      % flags.idle       )

flags = Flags()
flags.asByte = 0x5  # ->0101

print( "logout: %i"      % flags.bit.logout   )
# `bit` is defined as anonymous field, so its fields can also be accessed directly:
print( "logout: %i"      % flags.logout     )
print( "userswitch:  %i" % flags.userswitch )
print( "suspend   :  %i" % flags.suspend    )
print( "idle  : %i"      % flags.idle       )

status = Status()
status.asByte = 0x5e  # ->01011100

print ("Health: %s" % rfDataTypeStatusHealth(2))
print( "Health: %i"      % status.Health)
print( "Health: %s"      % rfDataTypeStatusHealth(status.Health))
print( "HealthRollupStat: %i"      % status.HealthRollupStat)
print( "HealthRollupStat: %s"      % rfDataTypeStatusHealthRollup(status.HealthRollupStat))
print( "State: %i"      % status.State)
print( "State: %s"      % rfDataTypeStatusState(status.State))

#Convert from integer number to hex
intnum=48
print('{:x}'.format(intnum))

#print( "HealthOK: %i"      % status.bit.Health_OK)
#print( "HealthWarning: %i"      % status.Health_Warning)
#print( "HealthCritical: %i"      % status.Health_Critical)
#print( "HealthRollupStat_OK: %i"      % status.HealthRollupStat_OK)
#print( "HealthRollupStat_Warning: %i"      % status.HealthRollupStat_Warning)
#print( "HealthRollupStat_Critical: %i"      % status.HealthRollupStat_Critical)
#print( "State_Enabled: %i"      % status.State_Enabled)
#print( "State_Disabled: %i"      % status.State_Disabled)
#print( "State_StandbyOffline: %i"      % status.State_StandbyOffline)
#print( "State_StandbySpare: %i"      % status.State_StandbySpare)
#print( "State_InTest: %i"      % status.State_InTest)
#print( "State_Starting: %i"      % status.State_Starting)
#print( "State_Absent: %i"      % status.State_Absent)
# ` is defined as anonymous field, so its fields can also be accessed directly:


