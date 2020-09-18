# Coroutine.

def Searcher():
    import time
    print("Starting.....")
    book = "Execution of coroutine is similar to the generator. When we call coroutine nothing happens, it runs only in response to the next() and send() method. This can be seen clearly in above example, as only after calling __next__() method, out coroutine starts executing. After this call, execution advances to the first yield expression, now execution pauses and wait for value to be sent to corou object. When first value is sent to it, it checks for prefix and print name if prefix present. After printing name it goes through loop until it encounters name = (yield) expression again."
    time.sleep(3)
    print(".....Ended")

    while True:
        text = (yield)
        if text in book:
            print("Your Text is in Book.")
        else:
            print("Your Text is not in Book.")

search = Searcher()
next(search)

search.send("similar56")
search.send("When")
search.close()