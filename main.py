def calculate_performance_score(speed, efficiency):
    return (speed * 0.6) + (efficiency * 0.4)


if __name__ == "__main__":
    speed = 80
    efficiency = 90
    score = calculate_performance_score(speed, efficiency)
    print(f"Performance Score: {score}")
