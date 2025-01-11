import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#значения для графика
x = [0, 0.002, 0.004, 0.004, 0.006, 0.008, 0.008, 0.01, 0.01, 0.012, 0.012, 0.014, 0.016, 0.018, 0.02]
y = [3, 3, 3, -3, -3, -3, 3, 3, -3, -3, 0, 0, 0, 0, 0]

fig, ax = plt.subplots()

ax.plot(x, y, color = 'r', linewidth = 3)

#major - шаг сетки
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.002))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.001))
ax.yaxis.set_major_locator(ticker.MultipleLocator(3))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.grid(which='major',
        color = 'k')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

plt.title('Сигнал')
plt.xlabel('t')
plt.ylabel('U')

#размер окна вывода
fig.set_figwidth(10)
fig.set_figheight(5)

plt.show()
