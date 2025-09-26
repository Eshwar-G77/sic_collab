from gpiozero import LED, Buzzer
from time import sleep
from signal import pause # Used to keep the script running indefinitely

# --- Configuration ---
LED_PIN = 17    # Use the BCM (GPIO) number, e.g., GPIO 17 (Physical pin 11)
BUZZER_PIN = 27 # Use the BCM (GPIO) number, e.g., GPIO 27 (Physical pin 13)
DELAY_TIME = 1  # Time in seconds for each state

# Initialize the devices
led = LED(LED_PIN)
buzzer = Buzzer(BUZZER_PIN)

print("Starting LED and Buzzer alternative cycle...")
print(f"LED is on GPIO {LED_PIN}, Buzzer is on GPIO {BUZZER_PIN}")

try:
    while True:
        # --- State 1: LED ON, Buzzer OFF ---
        led.on()
        buzzer.off()
        print("LED ON, Buzzer OFF")
        sleep(DELAY_TIME)

        # --- State 2: LED OFF, Buzzer ON ---
        led.off()
        buzzer.on()
        print("LED OFF, Buzzer ON")
        sleep(DELAY_TIME)

except KeyboardInterrupt:
    # Clean up GPIO settings when Ctrl+C is pressed
    print("\nProgram stopped. Cleaning up GPIO.")
    led.off()
    buzzer.off()
    pass # Exits the program
#This is comment was added at end to test