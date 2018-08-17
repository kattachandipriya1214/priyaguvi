time = float(input(" "))


time = time % (24 * 3600)

hour = time // 3600

time %= 3600

minutes = time // 60


minutes= time

print(" %d:%d" % ( hour, minutes))
