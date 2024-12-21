class Temperature:
    def __init__(self, temperature, is_celsius=True):
        self.temperature = temperature
        self.is_celsius = is_celsius

    def ToFahrenheit(self):
        if self.is_celsius:
            return self.temperature * 9 / 5 + 32
        return self.temperature

    def ToCelsius(self):
        if not self.is_celsius:
            return (self.temperature - 32) * 5 / 9
        return self.temperature


if __name__ == "__main__":
    temp = Temperature(float(input("请输入摄氏温度：")))
    print(
        "摄氏温度 = {:.1f}，华氏温度 = {:.1f}".format(temp.temperature, temp.ToFahrenheit()))

    tmp = Temperature(float(input("请输入华氏温度：")), False)
    print(
        "摄氏温度 = {:.1f}，华氏温度 = {:.1f}".format(tmp.ToCelsius(), tmp.temperature))
