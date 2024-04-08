import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="RPK@tennis08"
)

mycursor=db.cursor()
mycursor.execute("CREATE DATABASE Partners")
mycursor.execute("CREATE TABLE Partners (PartnerID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), OrgType VARCHAR(100), PointofContact VARCHAR(255), Email VARCHAR(255), Phone VARCHAR(22), Address VARCHAR(255))")

def AddPartner(name,org,person,email,phone,address):
    mycursor.execute("INSERT INTO Partners (Name, OrgType, PointofContact, Email, Phone, Address) VALUES (%s,%s,%s,%s,%s,%s)", (name,org,person,email,phone,address))
    db.commit()

AddPartner("Business1","Retail","Jeff Bezos","jbezos@gmail.com","+18745654323","10 Valley Street")
AddPartner("Business2","Healthcare","John Smith","jsmith@gmail.com","+14438349959","8014 Lane Street")
AddPartner("Business3","Transportation","Elon Musk","emusk@gmail.com","+15508709323","932 Bigges Lane")
AddPartner("Business4","Public","Hayden West","hwest@gmail.com","+18374526363","8760 Hall Avenue")
AddPartner("Business5","Manufactoring","Philip Marks","pmark@gmail.com","+14423045474","Avenue Lane")
AddPartner("Business6","Agriculture","Desmond Johnson","djohnson@hotmail.com","+12334236574","5 Whitway Street")
AddPartner("Business7","Real Estate","Earl Jones","ejones@outlook.org","+51234567890","823 Harvard Road")
AddPartner("Business8","Technology","Dylan Patel","dpatel@mail.org","+0987654321","7383 Gustavo Street")
AddPartner("Business9","Ecommerce","Amy Moultrie","amoultrie@gmail.com","+14832840978","1000 Fring Street")
AddPartner("Business10","Craft","Ben Dover","bdover@oprotonmail.com","+27655558888","9876 Road Street")
AddPartner("Business11","Marketing","Michael Cox","mcox@gmail.com","+12345437685","96 Hermanos Avenue")
AddPartner("Business12","Telecommunication","John Backes","jb@gmail.com","+12876543454","12 Baker Street")
AddPartner("Business13","Agriculture","Philip Johnson","pjohn@gmail.com","+36543458756","1345 Indiana Road")
AddPartner("Business14","Healthcare","Demarcus Cousins","dcousins@hotmail.com","+15025578914","1381 Baker Street")
AddPartner("Business15","Retail","John Johnson","jj@gmail.com","+15843456575","18 Street Street")
AddPartner("Business16","Ecommerce","Jack Hemmingway","jhemmingway@protonmail.com","+15437890675","132 Louisville Road")
AddPartner("Business17","Mining","Percy Cassus","pc@gmail.com","+13245643232","8 Field Road")
AddPartner("Business18","Retail","Wayne Col","wcol@gmail.com","+13244325676","64 Tennis Road")
AddPartner("Business19","Ecommerce","Bruce Pol","bpol@hotmail.com","+34856078565","8232 Hardy Lane")
AddPartner("Business20","Real Estate","Rodger Medvedev","rwm@gmail.com","+27654859485","1222 Rocky Lane")
AddPartner("Business21","Retail","John Jack","jj@gmail.com","+15842456575","10 Street Lane")
AddPartner("Business22","Ecommerce","Jack Hault","jh@protonmail.com","+15237890675","132 Lexington Road")
AddPartner("Business23","Mining","Percy Cash","pc@gmail.com","+14545643232","9 Field Lane")
AddPartner("Business24","Retail","Wayne East","we@gmail.com","+13288325676","64 Basketball Road")
AddPartner("Business25","Ecommerce","Bruce Wayne","bw@hotmail.com","+34856658565","8242 Hardy Lane")

def Search(cat, query):
    mycursor.execute("SELECT * FROM Partners WHERE %s LIKE '%%s%'", (cat,query))
