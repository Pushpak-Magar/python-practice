x = object()
y = object()


x_list = [x] * 10
y_list = [y] * 30
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))


