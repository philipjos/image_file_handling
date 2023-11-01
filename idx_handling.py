import sys

path = sys.argv[1]
try:
    with open(path, "rb") as file:
        verification = int.from_bytes(file.read(2), byteorder="big")
        if verification != 0:
            print("Note: Invalid verification. Should always be 0.")
        
        type = int.from_bytes(file.read(1), byteorder="big")
        unsigned_byte_case = 8
        if type != unsigned_byte_case:
            print("Note: This implementation only idx with unsigned byte type.")

        dim = int.from_bytes(file.read(1), byteorder="big")
        if dim != 3:
            print("Note: This implementation only supports 3d idx.")
        
        size = []
        total_size = 1
        for i in range(0, dim):
            dim_size = int.from_bytes(file.read(4), byteorder="big")
            size.append(dim_size)
            total_size *= dim_size

        print("Data size: ")
        print(size)

        data = []
        logging_i = 0
        logging_example_bytes = 100
        logging_offset = 14
        logging_frequency = (total_size - logging_offset) / logging_example_bytes
        logging_frequency = logging_frequency if logging_frequency == int(logging_frequency) else int(logging_frequency) + 1
        for i in range(0, size[0]):
            element = []
            for j in range(0, size[1]):
                row = []
                for k in range(0, size[2]):
                    byte_int = int.from_bytes(file.read(1), byteorder="big")
                    row.append(byte_int)
                    if (logging_i - logging_offset) % logging_frequency == 0:
                        print(f"Element {i} - row {j} - col {k} - Example byte: {byte_int}")
                    logging_i += 1
                element.append(row)
            data.append(element)
        
        print("Data read complete.")
        print("Elements in data: " + str(len(data)))           
except Exception as e:
    print(e)