from gpiozero import LED, Buzzer # Import the necessary components
from time import sleep           # Import sleep for timing

# --- Configuration ---
# Assign the components to the physical GPIO pin numbers
# NOTE: Replace '17' and '18' with the actual GPIO pins you are using
LED_PIN = 17
BUZZER_PIN = 18

# Initialize the components
led = LED(LED_PIN)
buzzer = Buzzer(BUZZER_PIN)

# Define the delay time in seconds
DELAY_TIME = 0.5

print("Starting alternating LED and Buzzer...")

try:
    # --- Main Loop ---
    while True:
        # 1. LED ON, Buzzer OFF
        led.on()
        buzzer.off()
        print("LED ON / Buzzer OFF")
        sleep(DELAY_TIME)

        # 2. LED OFF, Buzzer ON
        led.off()
        buzzer.on()
        print("LED OFF / Buzzer ON")
        sleep(DELAY_TIME)

except KeyboardInterrupt:
    # Clean up the pins and exit gracefully when Ctrl+C is pressed
    print("\nProgram stopped. Cleaning up GPIO...")
    led.off()
    buzzer.off()