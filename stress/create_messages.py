from datetime import datetime
import random
import struct

from ICD_for_demo_emulator import icd_params
icd_params = icd_params()
message_counter = 777000
chunk_number = 100000

class create_messages:
    def create_TRACK_MESSAGE(self):
        input_list_parser = []
        input_bytes_parser = b''

        # insert  3 UINT32 0 -> 12 bytes
        for j in range(3):
            x = random.randint(0, 100)
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>I', x)

        # insert  3 UINT32 12 -> 15 bytes
        for j in range(1):
            x = icd_params.TRACKS_MESSAGE_SIZE
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>I', x)

        # insert  1 UINT64 16 -> 23 bytes
        for j in range(1):
            x = random.randint(0, 100)
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>Q', x)

        # insert  4 UINT16 24 -> 31 bytes
        for j in range(4):
            x = random.randint(0, 100)
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>H', x)

        # insert  7 UINT16 32 -> 45 bytes
        time_now = datetime.now()
        year = time_now.year
        input_list_parser.append(year)
        input_bytes_parser += struct.pack('>H', year)

        month = time_now.month
        input_list_parser.append(month)
        input_bytes_parser += struct.pack('>H', month)

        day_of_month = time_now.day
        input_list_parser.append(day_of_month)
        input_bytes_parser += struct.pack('>H', day_of_month)

        hour = time_now.hour
        input_list_parser.append(hour)
        input_bytes_parser += struct.pack('>H', hour)

        minute = time_now.minute
        input_list_parser.append(minute)
        input_bytes_parser += struct.pack('>H', minute)

        second = time_now.second
        input_list_parser.append(second)
        input_bytes_parser += struct.pack('>H', second)

        milliseconds = int(time_now.microsecond/pow(10, 3))
        input_list_parser.append(milliseconds)
        input_bytes_parser += struct.pack('>H', milliseconds)

        # insert 1 UINT16 46 -> 47 bytes
        for j in range(1):
            x = random.randint(0, 100)
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>H', x)

        # now information is for each trackID
        # assuming 10 tracks in the message
        for i in range(10):
            # insert 2 UINT32 48 -> 55 bytes
            for j in range(2):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 2 REAL64 56 -> 71 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>d', x)

            # insert 2 REAL32 72 -> 79 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 4 REAL64 80 -> 111 bytes
            for j in range(4):
                x = random.uniform(-100, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>d', x)

            # insert 3 REAL32 112 -> 123 bytes
            for j in range(3):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 1 UINT32 124 -> 127 bytes
            for j in range(1):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 10 REAL32 128 -> 167 bytes
            for j in range(10):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 2 UINT16 168 -> 171 bytes
            for j in range(2):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>H', x)

            # insert 2 REAL32 172 -> 179 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 1 UINT32 180 -> 183 bytes
            for j in range(1):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 24 REAL32 184 -> 279 bytes
            for j in range(24):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

        return input_list_parser, input_bytes_parser

    def create_TRACK_EXTENDED_message(self, range_of_trackID):
        input_list_parser = []
        input_bytes_parser = b''
        global message_counter
        global chunk_number
        # insert  1 UINT32 0 -> 3 bytes
        for j in range(1):
            x = message_counter
            input_list_parser.append(x)
            message_counter += 1
            input_bytes_parser += struct.pack('>I', x)

        # insert  1 UINT32 4 -> 7 bytes
        for j in range(1):
            x = 20
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>I', x)

        # insert  1 UINT32 7 -> 11 bytes
        for j in range(1):
            x = 0
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>I', x)

        # insert  1 UINT32 12 -> 15 bytes
        for j in range(1):
            x = icd_params.TRACKS_EXTENDED_MESSAGE_SIZE
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>I', x)

        # insert  1 UINT64 16 -> 23 bytes
        for j in range(1):
            x = chunk_number
            chunk_number += 1
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>Q', x)

        # insert  3 UINT16 24 -> 27 bytes
        for j in range(2):
            x = random.randint(0, 100)
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>H', x)

        # insert  1 UINT16 28 -> 29 bytes
        for j in range(1):
            x = 0
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>H', x)

        # insert  1 UINT16 30 -> 31 bytes
        for j in range(1):
            x = 10
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>H', x)

        # insert  7 UINT16 32 -> 45 bytes
        time_now = datetime.now()
        year = time_now.year
        input_list_parser.append(year)
        input_bytes_parser += struct.pack('>H', year)

        month = time_now.month
        input_list_parser.append(month)
        input_bytes_parser += struct.pack('>H', month)

        day_of_month = time_now.day
        input_list_parser.append(day_of_month)
        input_bytes_parser += struct.pack('>H', day_of_month)

        hour = time_now.hour
        input_list_parser.append(hour)
        input_bytes_parser += struct.pack('>H', hour)

        minute = time_now.minute
        input_list_parser.append(minute)
        input_bytes_parser += struct.pack('>H', minute)

        second = time_now.second
        input_list_parser.append(second)
        input_bytes_parser += struct.pack('>H', second)

        milliseconds = int(time_now.microsecond / pow(10, 3))
        input_list_parser.append(milliseconds)
        input_bytes_parser += struct.pack('>H', milliseconds)

        # insert  1 UINT16 46 -> 47 bytes
        for j in range(1):
            x = 0
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>H', x)

        # now information is for each trackID
        # assuming 10 tracks in the message
        for i in range(10):
            # insert 1 UINT32 48 -> 51 bytes
            for j in range(1):
                x = random.randint(0, range_of_trackID-1)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 1 UINT32 51 -> 55 bytes
            for j in range(1):
                x = 0
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 2 REAL64 56 -> 71 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>d', x)

            # insert 2 REAL32 72 -> 79 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 4 REAL64 80 -> 111 bytes
            for j in range(4):
                x = random.uniform(-100, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>d', x)

            # insert 3 REAL32 112 -> 123 bytes
            for j in range(3):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 1 UINT32 124 -> 127 bytes
            for j in range(1):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 10 REAL32 128 -> 167 bytes
            for j in range(10):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 2 UINT16 168 -> 171 bytes
            for j in range(2):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>H', x)

            # insert 2 REAL32 172 -> 179 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 1 UINT32 180 -> 183 bytes
            for j in range(1):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 24 REAL32 184 -> 279 bytes
            for j in range(24):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

        # create extra information, TRACK_EXTENDED_message
        for i in range(10):
            # insert 10 REAL32 2368 -> 2407 bytes
            for j in range(10):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 1 UINT32 2408 -> 2411 bytes
            for j in range(1):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

        return input_list_parser, input_bytes_parser

    def create_TRACK_EXTENDED_message_2(self):
        input_list_parser = []
        input_bytes_parser = b''

        # insert  4 UINT32 0 -> 15 bytes
        for j in range(4):
            x = random.randint(0, 100)
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>I', x)

        # insert  1 UINT64 16 -> 23 bytes
        for j in range(1):
            x = random.randint(0, 100)
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>Q', x)

        # insert  12 UINT16 24 -> 47 bytes
        for j in range(12):
            x = random.randint(0, 100)
            input_list_parser.append(x)
            input_bytes_parser += struct.pack('>H', x)

        # now information is for each trackID
        # assuming 10 tracks in the message
        for i in range(10):

            # insert 2 UINT32 48 -> 55 bytes
            for j in range(2):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 2 REAL64 56 -> 71 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>d', x)

            # insert 2 REAL32 72 -> 79 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 4 REAL64 80 -> 111 bytes
            for j in range(4):
                x = random.uniform(-100, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>d', x)

            # insert 3 REAL32 112 -> 123 bytes
            for j in range(3):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 1 UINT32 124 -> 127 bytes
            for j in range(1):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 10 REAL32 128 -> 167 bytes
            for j in range(10):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 2 UINT16 168 -> 171 bytes
            for j in range(2):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>H', x)

            # insert 2 REAL32 172 -> 179 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 1 UINT32 180 -> 183 bytes
            for j in range(1):
                x = random.randint(0, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>I', x)

            # insert 24 REAL32 184 -> 279 bytes
            for j in range(24):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

        # create extra information, TRACK_EXTENDED_message
        # assuming there are 10 trackID in a message
        for i in range(10):
            # insert 3 REAL32 2368 -> 2379 bytes
            for j in range(3):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 2 REAL64 2380 -> 2395 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>d', x)

            # insert 1 REAL32 2396 -> 2399 bytes
            for j in range(1):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

            # insert 2 REAL64 2400 -> 2415 bytes
            for j in range(2):
                x = random.uniform(-100, 100)
                input_list_parser.append(x)
                input_bytes_parser += struct.pack('>d', x)

            # insert 1 REAL32 2416 -> 2471 bytes
            for j in range(1):
                x = random.uniform(-100, 100)
                x1 = struct.pack('>f', x)
                x2 = struct.unpack('>f', x1)[0]
                input_list_parser.append(x2)
                input_bytes_parser += struct.pack('>f', x)

        return input_list_parser, input_bytes_parser
