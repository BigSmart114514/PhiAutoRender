import taptap
import os

if __name__ == "__main__":
    url = taptap.taptap(165287)
    print(url)
    os.system(f"wget -O phigros.apk {url}")
