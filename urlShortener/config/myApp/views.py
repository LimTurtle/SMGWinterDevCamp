from django.shortcuts import render
from django.db import connection


def display(request):
    return render(request, 'myApp/index.html')

def result(request):
    if request.POST.get("Create"):
        createStatus = True
        try:
            with connection.cursor() as cursor:
                sqlQueryCreate = "create table Product(" \
                                 	"maker CHAR(2)," \
                                     "model INT PRIMARY KEY," \
                                     "type_ CHAR(10) );"

                cursor.execute(sqlQueryCreate)

                sqlQueryCreate = "create table PC("\
                                     "model INT PRIMARY KEY,"\
                                     "speed DOUBLE,"\
                                     "ram INT,"\
                                     "hd INT,"\
                                     "price INT );"
                cursor.execute(sqlQueryCreate)

                sqlQueryCreate = "create table Laptop("\
                                     "model INT PRIMARY KEY,"\
                                     "speed DOUBLE,"\
                                     "ram INT,"\
                                     "hd INT,"\
                                     "price INT,"\
                                     "screen DOUBLE );"
                cursor.execute(sqlQueryCreate)

                sqlQueryCreate = "create table Printer("\
                                     "model INT PRIMARY KEY,"\
                                     "price INT,"\
                                     "color BOOL,"\
                                     "type_ CHAR(10) );"
                cursor.execute(sqlQueryCreate)
                connection.commit()
                connection.close()
            return render(request, 'myApp/result.html', {"testValue": "Create 성공", "createStatus": createStatus})
        except:
            return render(request, 'myApp/result.html', {"testValue": "Create 실패", "createStatus": createStatus})

    elif request.POST.get("Insert"):
        insertStatus = True
        try:
            with connection.cursor() as cursor:
                sqlQueryInsert = "insert into Product (maker, model, type_) " \
                        "values ('A', '1001', 'pc'), ('A', '1002', 'pc')," \
                        "('A', '1003', 'pc'), ('A', '2004', 'laptop')," \
                        "('A', '2005', 'laptop'), ('A', '2006', 'laptop')," \
                        "('B', '1004', 'pc'), ('B', '1005', 'pc')," \
                        "('B', '1006', 'pc'), ('B', '2007', 'laptop')," \
                        "('C', '1007', 'pc'), ('D', '1008', 'pc')," \
                        "('D', '1009', 'pc'), ('D', '1010', 'pc')," \
                        "('D', '3004', 'printer'), ('D', '3005', 'printer')," \
                        "('E', '1011', 'pc'), ('E', '1012', 'pc')," \
                        "('E', '1013', 'pc'), ('E', '2001', 'laptop')," \
                        "('E', '2002', 'laptop'), ('E', '2003', 'laptop')," \
                        "('E', '3001', 'printer'), ('E', '3002', 'printer')," \
                        "('E', '3003', 'printer'), ('F', '2008', 'laptop')," \
                        "('F', '2009', 'laptop'), ('G', '2010', 'laptop')," \
                        "('H', '3006', 'printer'), ('H', '3007', 'printer');"
                cursor.execute(sqlQueryInsert)

                sqlQueryInsert = "insert into PC (model, speed, ram, hd, price) " \
                        "values ('1001', '2.66', '1024', '250', '2114'), " \
                        "('1002', '2.10', '512', '250', '995'), " \
                        "('1003', '1.42', '512', '80', '478'), " \
                        "('1004', '2.80', '1024', '250', '649'), " \
                        "('1005', '3.20', '512', '250', '630'), " \
                        "('1006', '3.20', '1024', '320', '1049'), " \
                        "('1007', '2.20', '1024', '200', '510'), " \
                        "('1008', '2.20', '2048', '250', '770'), " \
                        "('1009', '2.00', '1024', '250', '650'), " \
                        "('1010', '2.80', '2048', '300', '770'), " \
                        "('1011', '1.86', '2048', '160', '959'), " \
                        "('1012', '2.80', '1024', '160', '649'), " \
                        "('1013', '3.06', '512', '80', '529');"
                cursor.execute(sqlQueryInsert)

                sqlQueryInsert = "insert into Laptop (model, speed, ram, hd, screen, price) " \
                        "values ('2001', '2.00', '2048', '240', '20.1', '3673'), " \
                        "('2002', '1.73', '1024', '80', '17.0', '949'), " \
                        "('2003', '1.80', '512', '60', '15.4', '549'), " \
                        "('2004', '2.00', '512', '60', '13.3', '1150'), " \
                        "('2005', '2.16', '1024', '120', '17.0', '2500'), " \
                        "('2006', '2.00', '2048', '80', '15.4', '1700'), " \
                        "('2007', '1.83', '1024', '120', '13.3', '1429'), " \
                        "('2008', '1.60', '1024', '100', '15.4', '900'), " \
                        "('2009', '1.60', '512', '80', '14.1', '680'), " \
                        "('2010', '2.00', '2048', '160', '15.4', '2300'); "
                cursor.execute(sqlQueryInsert)

                sqlQueryInsert = "insert into Printer (model, color, type_, price) " \
                        "values ('3001', true, 'ink-jet', '99'), " \
                        "('3002', false, 'laser', '239'), " \
                        "('3003', true, 'laser', '899'), " \
                        "('3004', false, 'ink-jet', '120'), " \
                        "('3005', false, 'laser', '120'), " \
                        "('3006', true, 'ink-jet', '100'), " \
                        "('3007', true, 'laser', '200'); "
                cursor.execute(sqlQueryInsert)
                connection.commit()
                connection.close()
            return render(request, 'myApp/result.html', {"testValue": "Insert 성공", "insertStatus": insertStatus})
        except:
            return render(request, 'myApp/result.html', {"testValue": "Insert 실패", "insertStatus": insertStatus})

    elif request.POST.get("Prob1"):
        outputOfQuery1 = []
        with connection.cursor() as cursor:

            sqlQuery1 = "select avg(hd) from PC;"
            cursor.execute(sqlQuery1)
            fetchResultQuery1 = cursor.fetchall()

            connection.commit()
            connection.close()

            for temp in fetchResultQuery1:
                eachRow = {'HDAverage': temp[0]}
                outputOfQuery1.append(eachRow)

        return render(request, 'myApp/result.html', {"output1": outputOfQuery1})


    elif request.POST.get("Prob2"):
        outputOfQuery2 = []
        with connection.cursor() as cursor:

            sqlQuery2 = "select p.maker, avg(l.speed) as speedAvg from Product p, Laptop l where p.model =" \
                        " l.model group by p.maker order by p.maker asc"
            cursor.execute(sqlQuery2)
            fetchResultQuery2 = cursor.fetchall()

            connection.commit()
            connection.close()

            for temp in fetchResultQuery2:
                eachRow = {'maker': temp[0], 'speedAverage': temp[1]}
                outputOfQuery2.append(eachRow)

        return render(request, 'myApp/result.html', {"output2": outputOfQuery2})

    elif request.POST.get("Prob3"):
        outputOfQuery3 = []
        with connection.cursor() as cursor:

            sqlQuery3 = "select p.maker, p.model, price from Product p, Laptop l where p.model = " \
                        "l.model and type_='laptop' and maker IN (select maker from Product p1, Laptop p2 where p1.model = p2.model group by p1.maker having count(p1.maker) = 1)"
            cursor.execute(sqlQuery3)
            fetchResultQuery3 = cursor.fetchall()
            connection.commit()
            connection.close()

            for temp in fetchResultQuery3:
                eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
                outputOfQuery3.append(eachRow)

        return render(request, 'myApp/result.html', {"output3": outputOfQuery3})

    elif request.POST.get("Prob4"):
        outputOfQuery4 = []
        with connection.cursor() as cursor:
            sqlQuery4 = "select p.maker, p.model, pr.price from Product p, Printer pr where p.model=pr.model and p.type_" \
                        "='printer' and pr.price IN (select max(price) " \
                        "from Product p1, Printer p2 where p1.model = p2.model group by p1.maker)"
            cursor.execute(sqlQuery4)
            fetchResultQuery4 = cursor.fetchall()

            connection.commit()
            connection.close()

            for temp in fetchResultQuery4:
                eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
                outputOfQuery4.append(eachRow)

        return render(request, 'myApp/result.html', {"output4": outputOfQuery4})