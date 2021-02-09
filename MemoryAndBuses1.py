import math

while True:
    use = input('Input the scenario you wish to see:')
    if use == '1' or use == '2':
        break
    else:
        print('Invalid input')

if use == '1':
    while True:
        try:
            print('Input the address bus width.')
            addressBusWidth = int(input('>>> '))
            break
        except ValueError:
            print('Invalid Input')

    while True:
        try:
            print('Input the data bus width.')
            dataBusWidth = int(input('>>> '))
            break
        except ValueError:
            print('Invalid Input')

    bitTierToString = [
        'b',
        'B',
        'kB',
        'MB',
        'GB',
        'TB'
    ]

    addressableMemory = (2**addressBusWidth) * dataBusWidth
    bitTier = 0
    if addressableMemory > 8:
        addressableMemory /= 8
        bitTier += 1

    while addressableMemory >= 1000 and bitTier < 5:
        addressableMemory /= 1000
        bitTier += 1

    print('Total addressable memory: {0} {1}'.format(int(addressableMemory), bitTierToString[bitTier]))
else:
    while True:
        try:
            print('Input the total RAM capacity.')
            ramCapacity = int(input('>>> '))
            break
        except ValueError:
            print('Invalid Input')

    dataBusWidths = []
    while True:
        while True:
            try:
                print('Input a data bus width. Current widths: {0}'.format(dataBusWidths))
                dataBusWidth = int(input('>>> '))
                dataBusWidths.append(dataBusWidth)
                break
            except ValueError:
                print('Invalid Input')
        print('Any more data bus widths needed? (y or n)')
        choice = input('>>> ').lower().strip()
        if choice == 'n':
            break
        else:
            pass

    for i in range(len(dataBusWidths)):
        addressBusWidth = math.log(ramCapacity / dataBusWidths[i])
        print('Data bus width: {0} bits | Address bus width: {1} bits'.format(dataBusWidths[i], int(addressBusWidth)))
