# L=[1,2,3,4,5]
# r=[]
# for i in range(3):
# 	r.append(L[i])

# print(r)
 
 # 应该是块级作用域吧

 # num=2;

# age = 20

# if age >= 18:
#     print('your age is', age)
#     print('adult')

# 除了def/class/lambda 之外，别的改变不了作用域，也即是说if 是无效的啦

# age=0

# if True:
# 	num=1

# print(num)

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
#     print('2015-3-25')


# now()
class Student(object):
	pass

bart=Student()
bart.name='xiaoming'
print(bart.name)