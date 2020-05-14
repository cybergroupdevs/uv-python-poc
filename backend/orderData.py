import xmltodict
import json
import u2py

filename = u2py.File('TRANSACTION')

#############################################################################
############################# TRANSACTION-1 #################################
#############################################################################

#phone
data = "532-704-9867"
filename.writev("6855*74*7648",2,data)

#tranDate
data = "180719"
filename.writev("6855*74*7648",3,data)

#taxAmt
data = "7.8"
filename.writev("6855*74*7648",8,data)

#item
data = bytes("327GFF217","utf-8")+u2py.VM+bytes("291DGG750","utf-8")
filename.writev("6855*74*7648",9,data)

#svChanged
data = bytes("43.48","utf-8")+u2py.VM+bytes("12.12","utf-8")
filename.writev("6855*74*7648",11,data)

#mrkdn
data = bytes("279.2","utf-8")+u2py.VM+bytes("371.1","utf-8")
filename.writev("6855*74*7648",12,data)

#description
data = bytes("Bog Dubautia","utf-8")+u2py.VM+bytes("Tailcup Lupine","utf-8")
filename.writev("6855*74*7648",14,data)

#type
data = "BCRD"	#BCRD
filename.writev("6855*74*7648",15,data)

#returnTrans
data = "1203*51*7876"
filename.writev("6855*74*7648",33,data)

#ccName
data = "ETHYL SPERWELL"
filename.writev("6855*74*7648",35,data)

#r2rReserNo
data = "720653703"
filename.writev("6855*74*7648",43,data)

#shipMethod
data = "UNDA"	#UNDA
filename.writev("6855*74*7648",46,data)

#shipComment
data = "26091"
filename.writev("6855*74*7648",49,data)

#shipFName
data = "ETHYL"
filename.writev("6855*74*7648",51,data)

#shipLName
data = "SPERWELL"
filename.writev("6855*74*7648",52,data)

#shipAddr
data = "011 Derek Point"
filename.writev("6855*74*7648",53,data)

#shipCity
data = "Austin"
filename.writev("6855*74*7648",54,data)

#shipState
data = "Texas"
filename.writev("6855*74*7648",55,data)

#shipZip
data = "57236"
filename.writev("6855*74*7648",56,data)

#shipDate
data = "180492"
filename.writev("6855*74*7648",57,data)

#mbaOrderId
data = "942909664*5"
filename.writev("6855*74*7648",58,data)

#attemptType
data = "BCRD"	#BCRD
filename.writev("6855*74*7648",69,data)

#attemptAmt
data = "156.72"
filename.writev("6855*74*7648",70,data)

#acctMethod
data = "5"
filename.writev("6855*74*7648",71,data)

#authMethod
data = "E"
filename.writev("6855*74*7648",72,data)

#maskedAccNo
data = "571483******2656"
filename.writev("6855*74*7648",82,data)

#shipCarrier
data = bytes("UPS","utf-8")+u2py.VM+bytes("UPS","utf-8")
filename.writev("6855*74*7648",104,data)

#shipTrackNo
data = bytes("895297049165","utf-8")+u2py.VM+bytes("765545862171","utf-8")
filename.writev("6855*74*7648",105,data)

#sigMethod
data = "E"
filename.writev("6855*74*7648",129,data)

#pfPoints
data = "183"
filename.writev("6855*74*7648",155,data)

#############################################################################
############################# TRANSACTION-2 #################################
#############################################################################

#phone
data = "320-836-4504"
filename.writev("5286*28*2729",2,data)

#tranDate
data = "180719"
filename.writev("5286*28*2729",3,data)

#taxAmt
data = "7.8"
filename.writev("5286*28*2729",8,data)

#item
data = bytes("327GFF217","utf-8")+u2py.VM+bytes("291DGG750","utf-8")
filename.writev("5286*28*2729",9,data)

#svChanged
data = bytes("43.48","utf-8")+u2py.VM+bytes("12.12","utf-8")
filename.writev("5286*28*2729",11,data)

#mrkdn
data = bytes("279.2","utf-8")+u2py.VM+bytes("371.1","utf-8")
filename.writev("5286*28*2729",12,data)

#description
data = bytes("Bog Dubautia","utf-8")+u2py.VM+bytes("Tailcup Lupine","utf-8")
filename.writev("5286*28*2729",14,data)

#type
data = "CASH"	#CASH
filename.writev("5286*28*2729",15,data)

#returnTrans
data = "1203*51*7876"
filename.writev("5286*28*2729",33,data)

#ccName
data = "YORGO DONAWAY"
filename.writev("5286*28*2729",35,data)

#r2rReserNo
data = "720653703"
filename.writev("5286*28*2729",43,data)

#shipMethod
data = "Ground" #Ground
filename.writev("5286*28*2729",46,data)

#shipComment
data = "26091"
filename.writev("5286*28*2729",49,data)

#shipFName
data = "ETHYL"
filename.writev("5286*28*2729",51,data)

#shipLName
data = "SPERWELL"
filename.writev("5286*28*2729",52,data)

#shipAddr
data = "011 Derek Point"
filename.writev("5286*28*2729",53,data)

#shipCity
data = "Austin"
filename.writev("5286*28*2729",54,data)

#shipState
data = "Texas"
filename.writev("5286*28*2729",55,data)

#shipZip
data = "57236"
filename.writev("5286*28*2729",56,data)

#shipDate
data = "180492"
filename.writev("5286*28*2729",57,data)

#mbaOrderId
data = "942909664*5"
filename.writev("5286*28*2729",58,data)

#attemptType
data = "AMEX" #AMEX
filename.writev("5286*28*2729",69,data)

#attemptAmt
data = "156.72"
filename.writev("5286*28*2729",70,data)

#acctMethod
data = "5"
filename.writev("5286*28*2729",71,data)

#authMethod
data = "E"
filename.writev("5286*28*2729",72,data)

#maskedAccNo
data = "571483******2656"
filename.writev("5286*28*2729",82,data)

#shipCarrier
data = bytes("UPS","utf-8")+u2py.VM+bytes("UPS","utf-8")
filename.writev("5286*28*2729",104,data)

#shipTrackNo
data = bytes("895297049165","utf-8")+u2py.VM+bytes("765545862171","utf-8")
filename.writev("5286*28*2729",105,data)

#sigMethod
data = "E"
filename.writev("5286*28*2729",129,data)

#pfPoints
data = "183"
filename.writev("5286*28*2729",155,data)


#############################################################################
############################# TRANSACTION-3 #################################
#############################################################################

#phone
data = "565-684-7423"
filename.writev("8720*99*8238",2,data)

#tranDate
data = "180719"
filename.writev("8720*99*8238",3,data)

#taxAmt
data = "7.8"
filename.writev("8720*99*8238",8,data)

#item
data = bytes("327GFF217","utf-8")+u2py.VM+bytes("291DGG750","utf-8")
filename.writev("8720*99*8238",9,data)

#svChanged
data = bytes("43.48","utf-8")+u2py.VM+bytes("12.12","utf-8")
filename.writev("8720*99*8238",11,data)

#mrkdn
data = bytes("279.2","utf-8")+u2py.VM+bytes("371.1","utf-8")
filename.writev("8720*99*8238",12,data)

#description
data = bytes("Bog Dubautia","utf-8")+u2py.VM+bytes("Tailcup Lupine","utf-8")
filename.writev("8720*99*8238",14,data)

#type
data = "AMEX"	#AMEX
filename.writev("8720*99*8238",15,data)

#returnTrans
data = "1203*51*7876"
filename.writev("8720*99*8238",33,data)

#ccName
data = "YORGO DONAWAY"
filename.writev("8720*99*8238",35,data)

#r2rReserNo
data = "720653703"
filename.writev("8720*99*8238",43,data)

#shipMethod
data = "UNDA" #UNDA
filename.writev("8720*99*8238",46,data)

#shipComment
data = "26091"
filename.writev("8720*99*8238",49,data)

#shipFName
data = "ETHYL"
filename.writev("8720*99*8238",51,data)

#shipLName
data = "SPERWELL"
filename.writev("8720*99*8238",52,data)

#shipAddr
data = "011 Derek Point"
filename.writev("8720*99*8238",53,data)

#shipCity
data = "Austin"
filename.writev("8720*99*8238",54,data)

#shipState
data = "Texas"
filename.writev("8720*99*8238",55,data)

#shipZip
data = "57236"
filename.writev("8720*99*8238",56,data)

#shipDate
data = "180492"
filename.writev("8720*99*8238",57,data)

#mbaOrderId
data = "942909664*5"
filename.writev("8720*99*8238",58,data)

#attemptType
data = "CASH" #CASH
filename.writev("8720*99*8238",69,data)

#attemptAmt
data = "156.72"
filename.writev("8720*99*8238",70,data)

#acctMethod
data = "5"
filename.writev("8720*99*8238",71,data)

#authMethod
data = "E"
filename.writev("8720*99*8238",72,data)

#maskedAccNo
data = "571483******2656"
filename.writev("8720*99*8238",82,data)

#shipCarrier
data = bytes("UPS","utf-8")+u2py.VM+bytes("UPS","utf-8")
filename.writev("8720*99*8238",104,data)

#shipTrackNo
data = bytes("895297049165","utf-8")+u2py.VM+bytes("765545862171","utf-8")
filename.writev("8720*99*8238",105,data)

#sigMethod
data = "E"
filename.writev("8720*99*8238",129,data)

#pfPoints
data = "183"
filename.writev("8720*99*8238",155,data)

#############################################################################
############################# TRANSACTION-4 #################################
#############################################################################

#phone
data = "171-586-9229"
filename.writev("5778*71*6250",2,data)

#tranDate
data = "180719"
filename.writev("5778*71*6250",3,data)

#taxAmt
data = "7.8"
filename.writev("5778*71*6250",8,data)

#item
data = bytes("327GFF217","utf-8")+u2py.VM+bytes("291DGG750","utf-8")
filename.writev("5778*71*6250",9,data)

#svChanged
data = bytes("43.48","utf-8")+u2py.VM+bytes("12.12","utf-8")
filename.writev("5778*71*6250",11,data)

#mrkdn
data = bytes("279.2","utf-8")+u2py.VM+bytes("371.1","utf-8")
filename.writev("5778*71*6250",12,data)

#description
data = bytes("Bog Dubautia","utf-8")+u2py.VM+bytes("Tailcup Lupine","utf-8")
filename.writev("5778*71*6250",14,data)

#type
data = "AMEX"	#AMEX
filename.writev("5778*71*6250",15,data)

#returnTrans
data = "1203*51*7876"
filename.writev("5778*71*6250",33,data)

#ccName
data = "YORGO DONAWAY"
filename.writev("5778*71*6250",35,data)

#r2rReserNo
data = "720653703"
filename.writev("5778*71*6250",43,data)

#shipMethod
data = "UNDA" #UNDA
filename.writev("5778*71*6250",46,data)

#shipComment
data = "26091"
filename.writev("5778*71*6250",49,data)

#shipFName
data = "ETHYL"
filename.writev("5778*71*6250",51,data)

#shipLName
data = "SPERWELL"
filename.writev("5778*71*6250",52,data)

#shipAddr
data = "011 Derek Point"
filename.writev("5778*71*6250",53,data)

#shipCity
data = "Austin"
filename.writev("5778*71*6250",54,data)

#shipState
data = "Texas"
filename.writev("5778*71*6250",55,data)

#shipZip
data = "57236"
filename.writev("5778*71*6250",56,data)

#shipDate
data = "180492"
filename.writev("5778*71*6250",57,data)

#mbaOrderId
data = "942909664*5"
filename.writev("5778*71*6250",58,data)

#attemptType
data = "CASH" #CASH
filename.writev("5778*71*6250",69,data)

#attemptAmt
data = "156.72"
filename.writev("5778*71*6250",70,data)

#acctMethod
data = " " #NO VALUE
filename.writev("5778*71*6250",71,data)

#authMethod
data = " " #NO VALUE
filename.writev("5778*71*6250",72,data)

#maskedAccNo
data = "571483******2656"
filename.writev("5778*71*6250",82,data)

#shipCarrier
data = bytes("UPS","utf-8")+u2py.VM+bytes("UPS","utf-8")
filename.writev("5778*71*6250",104,data)

#shipTrackNo
data = bytes("895297049165","utf-8")+u2py.VM+bytes("765545862171","utf-8")
filename.writev("5778*71*6250",105,data)

#sigMethod
data = " " #NO VALUE
filename.writev("5778*71*6250",129,data)

#pfPoints
data = "183"
filename.writev("5778*71*6250",155,data)

