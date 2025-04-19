import taptap
import os
import time

def download():
    url = taptap.taptap(165287)
    print(url)
    retries = 3
    wait_time = 10
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

    for i in range(retries + 1):
        command = f"wget -O phigros.apk --user-agent='{user_agent}' '{url}'"
        result = os.system(command)
        if result == 0:
            print("Download successful!")
            break
        else:
            print(f"Download failed (attempt {i+1}).")
            if i < retries:
                print(f"Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
            else:
                print("Max retries reached. Download failed.")

if __name__ == "__main__":
    download()
