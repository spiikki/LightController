from collections import deque

class lightBuffer():
    def __init__(self):
        self.buffer = [(0, 0, 0)]
        self.rotation = False

    def set(self, value):
        print(value)
        self.buffer = [(value[0], value[2], value[1])]

    def tween(self, start, end, frames):
        redFrameDelta = start[0]-end[0]
        greenFrameDelta = start[2]-end[2]
        blueFrameDelta = start[1]-end[1]

        redIncrement = -redFrameDelta / (frames-1)
        greenIncrement = -greenFrameDelta / (frames-1)
        blueIncrement = -blueFrameDelta / (frames-1)

        for frame in range(0,frames):
            self.buffer.append((
                int(round(start[0]+redIncrement*frame,0)),
                int(round(start[2]+greenIncrement*frame,0)),
                int(round(start[1]+blueIncrement*frame,0)),
            ))
        print(self.buffer)

    def getBuffer(self):
        return self.buffer

    def clearBuffer(self):
        self.buffer = []

    def getFrame(self, index):
        return self.buffer[index]

    def toggleRotation(self, value):
        self.rotation = value
        pass

    def rotate(self, steps):
        if self.rotation:
            tmp = deque(self.buffer)
            tmp.rotate(steps)
            self.buffer = list(tmp)

#    def __add__(self):
#        
