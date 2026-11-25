
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Free Space Path Loss
def fspl_db(d_km, f_mhz):
    """Free-space path loss in dB (distance in km, frequency in MHz)."""
    return 20 * np.log10(d_km) + 20 * np.log10(f_mhz) + 32.44


# Base station and mobile station parameters
Pt_dbm = 43.0
Gt_db = 15.0
Gr_db = 0.0

# Distances in kilometres
distances = [0.1, 0.5, 1, 2, 5, 10]

# Frequencies in MHz
frequencies = [900, 1800]

# Store results for plotting
fspl_values = {}
received_power_values = {}

# Calculate FSPL and received power
for f in frequencies:

    fspl_list = []
    power_list = []

    print(f"\nFrequency = {f} MHz")
    print(f"{'d (km)':>8}{'FSPL (dB)':>12}{'Pr (dBm)':>11}{'Pr (W)':>14}")

    for d in distances:

        # Calculate FSPL
        L = fspl_db(d, f)

        # Calculate received power in dBm
        Pr = Pt_dbm + Gt_db + Gr_db - L

        # Convert received power from dBm to Watts
        Pr_w = 10 ** (Pr / 10) / 1000

        fspl_list.append(L)
        power_list.append(Pr)

        print(f"{d:8.1f}{L:12.2f}{Pr:11.2f}{Pr_w:14.3e}")

    fspl_values[f] = fspl_list
    received_power_values[f] = power_list


# -----------------------------------
# GRAPH 1: FSPL vs DISTANCE
# -----------------------------------

plt.figure(figsize=(9, 5))

for f in frequencies:
    plt.plot(
        distances,
        fspl_values[f],
        marker='o',
        linewidth=2,
        label=f'{f} MHz'
    )

plt.xscale('log')
plt.xlabel('Distance (km)')
plt.ylabel('FSPL (dB)')
plt.title('Free-space path loss vs distance')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()


# -----------------------------------
# GRAPH 2: RECEIVED POWER vs DISTANCE
# -----------------------------------

plt.figure(figsize=(9, 5))

for f in frequencies:
    plt.plot(
        distances,
        received_power_values[f],
        marker='o',
        linewidth=2,
        label=f'{f} MHz'
    )

plt.xscale('log')
plt.xlabel('Distance (km)')
plt.ylabel('Pr (dBm)')
plt.title('Received power vs distance (Pt = 43 dBm, Gt = 15 dB)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Display both graphs
plt.show()
