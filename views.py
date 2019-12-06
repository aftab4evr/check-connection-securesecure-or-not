def get(self, request):
        if request.is_secure():
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nConnection is secure")
        else:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nConnection is not secure")
