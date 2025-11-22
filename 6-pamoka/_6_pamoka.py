def ka():
    def dal(sk):
        sum = 0
        for i in str(sk):
            sum+=int(i)
        return sum
    aq=int(input("iveskite skaiciu "))
    w=dal(aq)
    print(w)
ka()

