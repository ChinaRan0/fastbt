import socket
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import infoTest
def is_port_open(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1):
            return True
    except (socket.timeout, socket.error):
        return False

def scan_ports(target_ip, port_list, num_threads=10):
    open_ports = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(is_port_open, target_ip, port): port for port in port_list}

        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            try:
                if future.result():
                    open_ports.append(port)
            except Exception as e:
                print(f"Error scanning port {port}: {e}")

    return open_ports


def main(ipInput):
    target_ip = ipInput
    port_list = [80, 443, 8080, 22, 3389,5003,8888,3443,5000,6000,7000,8081,5005,3200,8001,8834,8082,8083,8084,8085]  # 探测端口列表
    open_ports = scan_ports(target_ip, port_list)
    zichanList=[]                           #存储列表
    if open_ports:
        # print(f"Open ports on {target_ip}: {open_ports}")
        for it in open_ports:
            zichanList.append(f"{target_ip}:{it}")
            print(f"{target_ip}:{it}")

    if len(zichanList) != 0:
        for zichan in zichanList:
            infoTest.finger(zichan)


    else:
        print(f"No open ports found on {target_ip}")

if __name__ == "__main__":
    print("由 知攻善防实验室 ChinaRan404 开发")
    print("仅用于在可以ip巨量时使用,ip较少还是建议手动判断.")
    print("1.常驻模式")
    print("2.文件批量模式")
    mode = input("请输入数字:")
    mode = int(mode)
    if mode == 1:
        while 1 :
            ipInput = input("ip:")
            
            main(ipInput)

    if mode == 2:
        print("请将目标文件村存放至target.txt,敲回车继续")
        import os 
        os.system("pause")
        f = open("target.txt",'r')
        ff =f .read().splitlines()
        f.close
        for fileopen in ff:
            main(fileopen)
            
