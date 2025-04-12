import taptap
import os

if __name__ == "__main__":
    url = taptap.taptap(165287)
    print(url)
    os.system("wget %s" % url)
    os.system("mv *.apk phigros.apk")