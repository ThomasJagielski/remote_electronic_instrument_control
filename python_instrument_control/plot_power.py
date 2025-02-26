import matplotlib.pyplot as plt

# Function to parse the file and extract data
def parse_data(filename):
    vcca_data = {"top_a_power": [], "top_a_current": [], "top_a_voltage": []}
    vccd18_data = {"bottom_a_power": [], "bottom_a_current": [], "bottom_a_voltage": []}

    with open(filename, 'r') as file:
        for line in file:
            if "BOARD1_VCCA" in line:
                parts = line.split(',')
                for part in parts:
                    if "top_a_power" in part:
                        vcca_data["top_a_power"].append(float(part.split('=')[1].strip()))
                    elif "top_a_current" in part:
                        vcca_data["top_a_current"].append(float(part.split('=')[1].strip()))
                    elif "top_a_voltage" in part:
                        vcca_data["top_a_voltage"].append(float(part.split('=')[1].strip()))
            elif "BOARD1_VCCD18" in line:
                parts = line.split(',')
                for part in parts:
                    if "bottom_a_power" in part:
                        vccd18_data["bottom_a_power"].append(float(part.split('=')[1].strip()))
                    elif "top_a_current" in part:
                        vccd18_data["bottom_a_current"].append(float(part.split('=')[1].strip()))
                    elif "bottom_a_voltage" in part:
                        vccd18_data["bottom_a_voltage"].append(float(part.split('=')[1].strip()))
    
    return vcca_data, vccd18_data

# Function to plot the data using subplots for top_a and bottom_a
def plot_data_subplots(vcca_data, vccd18_data):
    fig, axs = plt.subplots(2, 1, figsize=(10, 12))

    # Plotting VCCA data (top_a_power vs index) in the first subplot
    axs[0].plot(range(len(vcca_data["top_a_current"])), vcca_data["top_a_power"], label="VCCA (Power vs Index)", color="tab:blue", marker='.')
    axs[0].set_xlabel("Index")
    axs[0].set_ylabel("Power (W)", color="tab:blue")
    axs[0].tick_params(axis="y", labelcolor="tab:blue")
    axs[0].set_title("VCCA - Power vs Index")
    
    # # Adding voltage for VCCA in the first subplot
    # ax2 = axs[0].twinx()
    # ax2.plot(range(len(vcca_data["top_a_current"])), vcca_data["top_a_current"], label="VCCA Current (A)", color="tab:red", marker='.')
    # ax2.set_ylabel("Current (A)", color="tab:red")
    # ax2.tick_params(axis="y", labelcolor="tab:red")
    
    # Plotting VCCD18 data (bottom_a_power vs index) in the second subplot
    axs[1].plot(range(len(vccd18_data["bottom_a_current"])), vccd18_data["bottom_a_power"], label="VCCD18 (Power vs Index)", color="tab:green", marker='.')
    axs[1].set_xlabel("Index")
    axs[1].set_ylabel("Power (W)", color="tab:green")
    axs[1].tick_params(axis="y", labelcolor="tab:green")
    axs[1].set_title("VCCD18 - Power vs Index")

    # # Adding voltage for VCCD18 in the second subplot
    # ax2_2 = axs[1].twinx()
    # ax2_2.plot(range(len(vccd18_data["bottom_a_current"])), vccd18_data["bottom_a_current"], label="VCCD18 Current (A)", color="tab:orange", marker='.')
    # ax2_2.set_ylabel("Current (A)", color="tab:orange")
    # ax2_2.tick_params(axis="y", labelcolor="tab:orange")

    # Adjust layout
    fig.tight_layout()
    
    # Show plot
    # plt.show()
    plt.savefig("./power_plot.png")


def plot_power_measurements(vcca_data, vccd18_data, output_filename):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plotting top_a_power from VCCA on the first axis (left)
    ax1.plot(range(len(vcca_data["top_a_power"])), vcca_data["top_a_power"], label="VCCA Power", color="tab:blue", marker='o')
    ax1.set_xlabel("Index")
    ax1.set_ylabel("VCCA Power (W)", color="tab:blue")
    ax1.tick_params(axis='y', labelcolor="tab:blue")
    
    # Creating the second y-axis for the bottom_a_power from VCCD18
    ax2 = ax1.twinx()
    ax2.plot(range(len(vccd18_data["bottom_a_power"])), vccd18_data["bottom_a_power"], label="VCCD18 Power", color="tab:green", marker='s')
    ax2.set_ylabel("VCCD18 Power (W)", color="tab:green")
    ax2.tick_params(axis='y', labelcolor="tab:green")

    # Title and layout adjustments
    plt.title("Top and Bottom Power Measurements (VCCA & VCCD18)")
    fig.tight_layout()

    # Save the plot to file
    plt.savefig(output_filename)

    # Optionally, close the plot to free up memory
    plt.close()

# Main function to execute the script
if __name__ == "__main__":
    filename = "power_measurement.txt"  # Replace with your actual file name
    # vcca_data, vccd18_data = parse_data(filename)
    # plot_data_subplots(vcca_data, vccd18_data)
    output_filename = "power_measurements_plot.png"  # Replace with desired output filename (can be .png, .pdf, etc.)
    
    vcca_data, vccd18_data = parse_data(filename)
    plot_power_measurements(vcca_data, vccd18_data, output_filename)
    print(f"Plot saved to {output_filename}")
