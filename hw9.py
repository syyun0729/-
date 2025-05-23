class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def show(self):
        print(f'({self.__x}, {self.__y})')

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)  
        self.rb = Point(x2, y2)  

    def show(self):
        x1, y1 = self.lt.get()
        x2, y2 = self.rb.get()
        print(f'좌측상단 꼭지점이 ({x1}, {y1})이고 우측하단 꼭지점이 ({x2}, {y2})인 사각형입니다.')

    def getWidth(self):
        x1, _ = self.lt.get()
        x2, _ = self.rb.get()
        return x2 - x1

    def getHeight(self):
        _, y1 = self.lt.get()
        _, y2 = self.rb.get()
        return y2 - y1

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())


def test():
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()
    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')


if __name__ == '__main__':
    test()
