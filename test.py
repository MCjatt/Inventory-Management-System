import keyboard

def on_barcode_scan(event):
    barcode = event.name
    print("Scanned barcode:", barcode)
    # Do something with the scanned barcode

keyboard.on_release_key('enter', on_barcode_scan)  # Listen for Enter key press

keyboard.wait('esc')  # Wait for the 'esc' key to exit the program
on_barcode_scan()