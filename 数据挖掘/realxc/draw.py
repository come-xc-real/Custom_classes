import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, data):
        self.data = data
        import matplotlib
        matplotlib.rc("font", family='YouYuan')

    def draw(self):
        bars = plt.bar(self.data.keys(), self.data.values())

        for bar, name in zip(bars, self.data.keys()):
            bar.set_label(name)

        plt.legend()
        plt.title('Histogram')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()
