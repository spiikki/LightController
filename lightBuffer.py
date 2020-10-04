class lightbuffer():
    def __init__(self):
        self.buffer = []

    def tween(self, start, end, frames):
        redFrameDelta = start[0]-end[0]
        greenFrameDelta = start[1]-end[1]
        blueFrameDelta = start[2]-end[2]

        redIncrement = -redFrameDelta / (frames-1)
        greenIncrement = -greenFrameDelta / (frames-1)
        blueIncrement = -blueFrameDelta / (frames-1)

        for frame in range(0,frames):
            self.buffer.append((
                int(round(start[0]+redIncrement*frame,0)),
                int(round(start[1]+greenIncrement*frame,0)),
                int(round(start[2]+blueIncrement*frame,0)),
            ))
        print(self.buffer)

    def getBuffer(self):
        return self.buffer

    def clearBuffer(self):
        self.buffer = []

    def getFrame(self, index):
        return self.buffer[index]

