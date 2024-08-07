import board
import digitalio
import storage

# If this key is held during boot, don't run the code which hides the storage and disables serial
# To use another key just count its row and column and use those pins
# You can also use any other pins not already used in the matrix and make a button just for accesing your storage
col = digitalio.DigitalInOut(board.GP8)
row = digitalio.DigitalInOut(board.GP10)

col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
    storage.disable_usb_drive()

row.deinit()
col.deinit()
