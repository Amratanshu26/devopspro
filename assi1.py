x = [1, 2, 3, 4, 5]
y = [100, 130, 140, 160, 170]

n = len(x)
sum_x = sum(x)
sum_y = sum(y)
N = sum(xi * yi for xi, yi in zip(x, y))
D = sum(xi ** 2 for xi in x)


m = (n * N - sum_x * sum_y) / (n * D - sum_x ** 2)

print(f"Slope (m): {m}")

