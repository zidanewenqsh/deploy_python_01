
class A():
    def __init__(self):
        pass
    def run(self):
        print("run")
        self.say("run")
    @staticmethod
    def say(world):
        print(world)
if __name__ == '__main__':
    a=A()
    word = "hello"
    a.say(word)
    a.run()