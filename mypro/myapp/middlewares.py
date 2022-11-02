def my_middlewares(get_response):
    print("one time initialization")
    def my_function(request):
        print("before view")
        response=get_response(request)
        print("this is after response")
        return response
    return my_function

class MyMiddlewares:
    def __init__(self,get_response):
        print("one time initialisation of class")
        self.get_response=get_response
    def __call__(self,request):
        print("this is before views")
        response=self.get_response(request)
        print("this is after view")
        return response
