class AreaVolume:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.1415926 * self.radius * self.radius

    def getVolume(self):
        return 4 / 3 * 3.1415926 * self.radius * self.radius * self.radius


if __name__ == "__main__":
    radius = float(input("请输入半径："))
    areaVolume = AreaVolume(radius)
    print("球面积：{:.2f}".format(areaVolume.getArea()))
    print("球体体积：{:.2f}".format(areaVolume.getVolume()))
