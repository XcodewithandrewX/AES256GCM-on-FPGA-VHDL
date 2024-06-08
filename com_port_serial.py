import serial
import time

def write_and_read_hex_loopback(port, baudrate, hex_data, loop_count):
    try:
        # Open the serial port
        ser = serial.Serial(port, baudrate, timeout=1)
        
        print(f"Opened {port} at {baudrate} baud.")
        
        # Convert hex string to bytes
        data_to_write = bytes.fromhex(hex_data)
        
        for i in range(loop_count):
            # Write data to the serial port
            ser.write(data_to_write)
            print(f"Sent hex data:              {hex_data}")
            
            time.sleep(15)  # Wait for the data to be transmitted and looped back
            
            # Read data from the serial port
            if ser.in_waiting > 0:
                data_received = ser.read(ser.in_waiting)
                # Convert bytes to hex string
                hex_received = data_received.hex()
                print(f"Received hex data:          {hex_received}")
            
            time.sleep(1)  # Delay to make the loop more observable

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        if ser.is_open:
            ser.close()
            print(f"Closed connection to {port}.")

if __name__ == "__main__":
    # Example usage
    port = 'COM6'  
    baudrate = 9600
    hex_data = 'feffe9928665731c6d6a8f9467308308feffe9928665731c6d6a8f9467308308cafebabefacedbaddecaf88800000200d9313225f88406e5a55909c5aff5269a86a7a9531534f7da2e4c303d8a318a721c3c0c95956809532fcf0e2449a6b525b16aedf5aa0de657ba637b391aafd255' 
    loop_count = 1  # Number of times to loop

    write_and_read_hex_loopback(port, baudrate, hex_data, loop_count)
