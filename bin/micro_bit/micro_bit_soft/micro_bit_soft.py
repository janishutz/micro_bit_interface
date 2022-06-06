import microbit


microbit.uart.init(19200)
while True:
    m = microbit.uart.read(1)
    if m is not None:
        microbit.display.scroll(str(m))
    else:
        microbit.display.clear()
