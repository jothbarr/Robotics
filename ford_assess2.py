class Circle:
    def __init__(self, xPosition, yPosition, radius):
        self.__xPosition = xPosition
        self.__yPosition = yPosition
        self.__radius = radius
    
    def print(self):
        print("\tX = %1.1f Y = %1.1f Radius = %1.1f" % (self.__xPosition, self.__yPosition, self.__radius))
    
    def isInside(self, xPoint, yPoint):
        distance = ((xPoint - self.__xPosition)**2 + (yPoint - self.__yPosition)**2)**0.5
        if self.__radius==0:
            return 2
        elif distance>self.__radius:
            return 0
        elif distance <= self.__radius:
            return 1
    
    @staticmethod
    def translateReturnCode(returnCode):
        if returnCode == 0:
            return "outside circle"
        elif returnCode == 1:
            return "within region"
        else:
            return "undefined"

# Instantiate an array of circles
circles = [Circle(1.0, 1.0, 1.0),
           Circle(-2.0, 1.0, 0.5),
           Circle(3.0, -1.0, 5.0),
           Circle(-4.0, -2.0, 0.0)]

# Call Circle::print for each object
for circle in circles:
    circle.print()
    
# Evaluate the list of points
points = [(0.5, 0.5), (1.0, 1.0), (1.0, 0.5), (2.0, -2.0), (-2.0, 1.0)]
for circle in circles:
    for point in points:
        returnValue = circle.isInside(point[0], point[1])
        print("\t%s %.2f, %.2f" % (circle.translateReturnCode(returnValue), point[0], point[1]))