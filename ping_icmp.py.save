from scapy.all import ICMP, IP, sr1
import matplotlib.pyplot as plt
import time

def icmp_ping(target_ip, count=4):
    rtts = []
    with open("icmp_results.txt", "w") as f:
        for i in range(count):
            pkt = IP(dst=target_ip)/ICMP()
            start_time = time.time()
            reply = sr1(pkt, timeout=2, verbose=0)
            end_time = time.time()
            
            if reply:
                rtt = (end_time - start_time) * 1000  # ms
                rtts.append(rtt)
                f.write(f"Reply from {reply.src}: time={rtt:.2f} ms\n")
                print(f"Reply from {reply.src}: time={rtt:.2f} ms")
            else:
                rtts.append(None)
                f.write("Request timed out.\n")
                print("Request timed out.")
    return rtts

def plot_rtts(rtts):
    times = [i + 1 for i in range(len(rtts))]
    filtered_rtts = [rtt if rtt is not None else 0 for rtt in rtts]

    plt.plot(times, filtered_rtts, marker='o', linestyle='-', color='blue')
    plt.title("ICMP Ping Results")
    plt.xlabel("Ping #")
    plt.ylabel("Response Time (ms)")
    plt.grid(True)
    plt.xticks(times)
    plt.ylim(0, max(filtered_rtts) + 10)
    plt.show()

if __name__ == "__main__":
    ip_destino = input("Introduce la IP a la que deseas hacer ping: ")
    resultados = icmp_ping(ip_destino, count=4)
    plot_rtts(resultados)
