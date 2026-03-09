# id,product,price,quantity
# [1,Pen,1.5,100]
# [2,Notebook,3.0,60]
# [3,Eraser,0.5,200]
# [4,Marker,2.0,80]
# [5,Stapler,5.5,30]


import csv

with open('./items.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    headers = ["id", "product", "price", "quantity"]
    csv_writer.writerow(headers)

    data = [[1, "Pen", 1.5, 100],
            [2, "Notebook", 3.0, 60],
            [3, "Eraser", 0.5, 200],
            [4, "Marker", 2.0, 80],
            [5, "Stapler", 5.5, 30]
            ]
    csv_writer.writerows(data)

    print("Data written succesfully...!")
