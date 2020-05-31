import platform

print(platform.python_version())
print(platform.release())
print(platform.system())
print(dir(platform))
for i in dir(platform):
    print(i)


