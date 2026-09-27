import matplotlib.pyplot as plt

frutas = ["Manzana", "Banana", "Naranja", "Uva"]
ventas = [35, 48, 22, 30]

plt.bar(frutas, ventas, color="#EE8AD0")
plt.title("Frutas vendidas esta semana")
plt.xlabel("Fruta")
plt.ylabel("Cantidad")
plt.show()