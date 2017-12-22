import os
fsize = os.path.getsize(r"goldimage-ssd")
fsize = fsize / (1024 * 1024)
android_os = r"4096"
fsize = int(fsize - 10)
print(fsize)
cmp_os = r"dd.exe if=goldimage-ssd of=\\.\physicaldrive1 bs=1M count = " + android_os
os.system(cmp_os)
cmp_back_gpt = r"dd.exe if=goldimage-ssd of=\\.\physicaldrive1 bs=1M skip=14335  seek=" + str(fsize)
os.system(cmp_back_gpt)
os.system(r"time /t")
