#coding: utf-8

class Car(object):
    __slots__ = ("length","width","owner","__dict__")

    def __init__ (self, length, width, owner=None):
        self.owner = owner
        self.length = length
        self.width

#只有在slots的属性才可以访问到，如果没有
    def __getattr__(self, name):
        print "getattr ",name
        assert name in self.__slots__,"not hava this property"
        return self.__dict__.get(name, None)
    

    def __setattr__(self, name, value):
        print "setattr", name
        if name != 'owner':
            assert value>0, name + "length must > 0"
        assert name in self.__slots__,"not hava this property"
        self.__dict__[name] = value

    def __delattr__(self,name):
        print "del attr",name
        assert name in self.__slots__,"not hava this property"
        if name == "owner":
            self.__dict__[name] = None

if __name__ == '__main__':
    a = Car(120, 220, u'小王')
   
