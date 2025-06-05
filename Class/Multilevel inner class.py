# create an outer class
class first:

    def __init__(self):
        # create an inner class object
        self.inner = self.secound_class()  #create an instance of the inner class

    def show(self):
        print('This is an outer class')

    # create a 1st inner class

    class secound_class:
        def __init__(self):
            # create an inner class of inner class object
            self.innerclassofinner = self.thrid_class() # the inner class of inner class

        def show(self):
            print('This is the inner class')

        # create a inner class 

        class thrid_class:
            def show(self):
                print('This is an inner class of inner class')


# create an outer class object
# i
f1 = first()
f1.show()

# create an inner class object
gfg1 = f1.secound_class
gfg1.show
print()

# create an inner class of inner class object
gfg2 = f1.inner.thrid_class
gfg2.show