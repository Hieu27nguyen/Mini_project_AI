import matplotlib.pyplot as plt

# Example 1: Pie Chart for Flight Delay Causes
def create_pie_chart():
    labels = ['Weather', 'Air Traffic Control', 'Technical Issues', 'Others']
    sizes = [40, 25, 20, 15]  # Example percentages
    colors = ['skyblue', 'orange', 'green', 'red']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Causes of Flight Delays')
    plt.savefig('flight_delays_pie_chart.png')  # Save the chart as an image file
    plt.show()

# Example 2: Line Graph for Projected Delay Reduction
def create_line_graph():
    years = [2024, 2025, 2026, 2027]
    delays_before_ai = [20, 19, 18, 17]  # Delays per 100 flights before AI implementation
    delays_after_ai = [20, 15, 10, 7]    # Hypothetical data after AI implementation

    plt.plot(years, delays_before_ai, label='Before AI', marker='o')
    plt.plot(years, delays_after_ai, label='After AI', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Delays per 100 Flights')
    plt.title('Reduction in Flight Delays with AI Implementation')
    plt.legend()
    plt.savefig('reduction_in_flight_delays.png')  # Save the chart as an image file
    plt.show()

if __name__ == "__main__":
    create_pie_chart()  # Generate the pie chart
    create_line_graph()  # Generate the line graph
