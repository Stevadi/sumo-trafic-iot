import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import os

def parse_tripinfo(file):
    if not os.path.exists(file):
        print(f"❌ File {file} not found.")
        return [], []
    tree = ET.parse(file)
    root = tree.getroot()

    durations = []
    waitings = []

    for trip in root.findall('tripinfo'):
        durations.append(float(trip.get('duration')))
        waitings.append(float(trip.get('waitingTime')))

    return durations, waitings

def main():
    print("Choose tripinfo file that want to get analysis:")
    print("1. tripinfo_adaptive.xml (adaptive lamp)")
    print("2. tripinfo_control.xml (manual/automatic control)")
    print("3. tripinfo_qlearning.xml (Q-Learning)")
    pilihan = input("Insert number [1/2/3] (default 1): ").strip()
    if option == "2":
        file = "tripinfo_control.xml"
    elif option == "3":
        file = "tripinfo_qlearning.xml"
    else:
        file = "tripinfo_adaptive.xml"
    durations, waitings = parse_tripinfo(file)

    if not durations:
        print("❌ No data in tripinfo.xml")
        return

    avg_duration = sum(durations) / len(durations)
    avg_waiting = sum(waitings) / len(waitings)

    print(f"✅ Average duration: {avg_duration:.2f} second")
    print(f"✅ Average waiting: {avg_waiting:.2f} second")

    # Visualisasi
    labels = ['Average Duration', 'Average Waiting']
    values = [avg_duration, avg_waiting]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['skyblue', 'salmon'])
    plt.title("Simulation result statistic")
    plt.ylabel("Detik")
    plt.tight_layout()
    os.makedirs("images", exist_ok=True)
    plt.savefig("images/simulation_result.png")
    plt.show()

if __name__ == "__main__":
    main()
