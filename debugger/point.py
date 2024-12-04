# def point():
#     point1 = int(input("Give points from judge 1: "))
#     point2 = int(input("Give points from judge 2: "))
#     point3 = int(input("Give points from judge 3: "))
#     point4 = int(input("Give points from judge 4: "))
#     point5 = int(input("Give points from judge 5: "))

#     maxpoint = max(point1, point2, point3, point4, point5)
#     minpoint = min(point1, point2, point3, point4, point5)

#     sum = point1 + point2 + point3 + point4 + point5
#     point = sum - maxpoint - minpoint

#     print("Total points are:", point)

# point()


def style_point():
    i = 1
    rating_points = []
    while i < 6:
        point = int(input("Give points from judge " + str(i) + ": "))
        rating_points.append(point)
        i += 1
    
    maxpoint = max(rating_points)
    minpoint = min(rating_points)


    sumpoint = sum(rating_points) - maxpoint - minpoint
    print(sumpoint)

style_point()
