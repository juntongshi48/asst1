import matplotlib.pyplot as plt

threads = [2, 3, 4, 5, 6, 7, 8]
speedup1 = [1.96, 1.64, 2.43, 2.48, 3.24, 3.37, 3.95]
speedup2 = [1.68, 2.21, 2.61, 2.92, 3.32, 3.72, 4.12]

speedup = speedup2

plt.plot(threads, speedup, marker='o', linestyle='-', linewidth=3)
plt.xlabel("#Threads")
plt.ylabel("Speedup")
plt.grid(True)
plt.show()

plt.savefig("speedup_vs_threads.png")