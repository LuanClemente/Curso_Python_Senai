X = 50

def func1():
    X = 10
    print("Sou a função 1")
    print(X)

def func2():
    X = 20
    print("Sou a função 2")

def func3():
    X = 30
    print("Sou a função 3")

def main():

    print("Sou a função principal")

    func1()
    func2()
    func3()

    print(X)
    
if __name__ == "__main__":
    main()