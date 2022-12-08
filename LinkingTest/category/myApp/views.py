from django.shortcuts import render
from django.db import connection

#1. select avg(hd) from PC
#2. select p.maker, avg(l.speed) as speedAvg from Product p, Laptop l where p.model = l.model group by p.maker order by p.maker asc
#3. select p.maker, p.model, price from Product p, Laptop l where p.model = l.model and type_='laptop' and maker IN (select maker from Product p1, Laptop p2 where p1.model = p2.model group by p1.maker having count(p1.maker) = 1)
#4. select p.maker, p.model, pr.price from Product p, Printer pr where p.model=pr.model and p.type_='printer' and pr.price IN (select max(price) from Product p1, Printer p2 where p1.model = p2.model group by p1.maker)

def display(request):
    outputOfQuery1 = []
    outputOfQuery2 = []
    outputOfQuery3 = []
    outputOfQuery4 = []
    with connection.cursor() as cursor:

        sqlQuery1 = "select avg(hd) from PC;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()

        sqlQuery2 = "select p.maker, avg(l.speed) as speedAvg from Product p, Laptop l where p.model = l.model group by p.maker order by p.maker asc"
        cursor.execute(sqlQuery2)
        fetchResultQuery2 = cursor.fetchall()

        sqlQuery3 = "select p.maker, p.model, price from Product p, Laptop l where p.model = l.model and type_='laptop' and maker IN (select maker from Product p1, Laptop p2 where p1.model = p2.model group by p1.maker having count(p1.maker) = 1)"
        cursor.execute(sqlQuery3)
        fetchResultQuery3 = cursor.fetchall()

        sqlQuery4 = "select p.maker, p.model, pr.price from Product p, Printer pr where p.model=pr.model and p.type_='printer' and pr.price IN (select max(price) from Product p1, Printer p2 where p1.model = p2.model group by p1.maker)"
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()

        connection.commit()
        connection.close()


        for temp in fetchResultQuery1:
            eachRow = {'HDAverage': temp[0]}
            outputOfQuery1.append(eachRow)

        for temp in fetchResultQuery2:
            eachRow = {'maker': temp[0], 'speedAverage': temp[1]}
            outputOfQuery2.append(eachRow)

        for temp in fetchResultQuery3:
            eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
            outputOfQuery3.append(eachRow)

        for temp in fetchResultQuery4:
            eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
            outputOfQuery4.append(eachRow)

    return render(request, 'myApp/index.html',{"output1": outputOfQuery1, "output2":outputOfQuery2, "output3":outputOfQuery3, "output4":outputOfQuery4} )
