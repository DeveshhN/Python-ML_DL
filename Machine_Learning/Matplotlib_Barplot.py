import matplotlib.pyplot as plt

def main():
    language = ["C","C++","Java","Python"]
    students = [30,40,35,55]

    plt.bar(
        language,
        students,
        width=0.3,
        edgecolor = "black",
        linewidth  = 1,
        alpha = 0.8,
        label = "Students"         #Legend Text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("Students")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()