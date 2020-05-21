from zeep import Client

cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
cliente2 = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')
cliente3 = Client(wsdl='https://cvnet.cpd.ua.es/servicioweb/publicos/pub_gestdocente.asmx?wsdl')

print( cliente.service.Add(3,7))
print( cliente.service.Subtract(5,2))
print( cliente.service.Multiply(3,5))
print( cliente.service.Divide(10,2))


print( cliente2.service.NumberToDollars(3.54))
print( cliente2.service.NumberToWords(35))

print(cliente3.service.wsasidepto("C", "2011-12", "B142", "" ))


