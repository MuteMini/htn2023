import asyncio
from websockets.server import serve
import numpy as np
import base64
import cv2
import keyboard

from module import findpostion

# From https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

async def prt(websocket):
    async for message in websocket:
        frame = data_uri_to_cv2_img(message)

        result = findpostion(frame)
        print(result)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
     

        # if len(result) > 0:
            # match result[0]:
            #     case 'Pointing_Up':
            #         keyboard.press('up')
            #     case 'Thumb_Down':
            #         keyboard.press('left')
            #     case 'Victory':
            #         keyboard.press('f')
            #     case 'Open_Palm':
            #         keyboard.press('p')
            #     case 'Thumb_Up':
            #         keyboard.press('right')
            #     case 'Closed_Fist':
            #         keyboard.press('z')
            #     case 'ILoveYou':
            #         keyboard.press('down')

async def main():
    async with serve(prt, "127.0.0.1", 3000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())